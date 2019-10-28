###############################################################################
### regression imports                                                      ###
###############################################################################

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import pandas_profiling as pdspro


###############################################################################
### local imports                                                           ###
###############################################################################

from env import host, user, password
from debug import local_settings, timeifdebug, timeargsifdebug, frame_splain



###############################################################################
### get db url                                                              ###
###############################################################################

@timeifdebug  # <--- DO NOT RUN ARGS DEBUG HERE! Will pass password info.
def get_db_url(user=user, password=password, host=host, database='employees'):
    '''
    get_db_url(user=user, password=password, host=host, database='zillow')
    RETURNS login url for selected mysql database
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


###############################################################################
### classification functions                                                ###
###############################################################################

@timeifdebug
def paste_df(splain=local_settings.splain, **kwargs):
    '''
    fn
    RETURNS:
    '''
    return check_df(pd.read_clipboard(), splain=splain, **kwargs)


@timeifdebug
def excel_df(excel_path, splain=local_settings.splain, **kwargs):
    '''
    fn
    RETURNS:
    '''
    return check_df(pd.read_excel(excel_path), splain=splain, **kwargs)


@timeifdebug
def google_df(sheet_url, splain=local_settings.splain, **kwargs):
    '''
    fn
    RETURNS:
    '''
    csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    return check_df(pd.read_csv(csv_export_url), splain=splain, **kwargs)


@timeifdebug
def csv_df(csv, splain=local_settings.splain, **kwargs):
    '''
    csv_df(csv, splain=local_settings.splain, **kwargs)
    RETURNS: dataframe

    Reads a csv file into a dataframe, then sends the dataframe to check_df().
    '''
    csv = pd.read_csv(csv)
    return check_df(csv, splain=splain, **kwargs)


@timeifdebug
def sql_df(sql, db, splain=local_settings.splain, **kwargs):
    '''
    sql_df(sql, db, splain=local_settings.splain, **kwargs)
    RETURNS: dataframe

    Reads a csv file into a dataframe, then sends the dataframe to check_df().
    '''
    db_url = get_db_url(database=db)
    return check_df(pd.read_sql(sql, db_url), splain=splain)

@timeifdebug
def check_df(dataframe, *args, splain=local_settings.splain, **kwargs):
    '''
    check_df(dataframe, splain=local_settings.splain, **kwargs)
    RETURNS: dataframe

    This function receives any dataframe, replaces null values with np.nan 
    and passes it through frame_splain(). If splain is true, frame_splain()
    will produce a report on the dataframe.
    '''
    dataframe.fillna(value=np.nan, inplace=True)
    frame_splain(dataframe, splain=splain, **kwargs)
    return dataframe


@timeifdebug
def get_telco_data(splain=local_settings.splain, **kwargs):
    '''
    get_telco_data(splain=local_settings.splain, **kwargs)
    RETURNS: dataframe

    The telco_churn dataset required for churn project. This function passes 
    through sql_df() and check_df().
    '''
    sql = '''
    select
        cust.`customer_id`,
        cust.`gender`,
        case when cust.`gender` = 'Male' then 1 else 0 end is_male,
        cust.`senior_citizen`,
        case when cust.`partner` = 'Yes' then 1 else 0 end partner,
        case when cust.`dependents` = 'Yes' then 1 else 0 end dependents,
        case when cust.`partner` = 'Yes' or cust.`dependents` = 'Yes' then 1 else 0 end family,
        2 * case when cust.`partner` = 'Yes' then 1 else 0 end + case when cust.`dependents` = 'Yes' then 1 else 0 end partner_deps_id,
        concat(
            case when cust.`partner` = 'Yes' then 'Has ' else 'No ' end,
            'partner, ',
            case when cust.`dependents` = 'Yes' then 'has ' else 'no ' end,
            'dependents') partner_deps,
        cust.`tenure`,
        case when cust.`phone_service` = 'Yes' then 1 else 0 end phone_service,
        case when cust.`multiple_lines` = 'Yes' then 1 else 0 end multiple_lines,
        case when cust.`phone_service` = 'Yes' then 1 else 0 end + case when cust.`multiple_lines` = 'Yes' then 1 else 0 end phone_service_id,
        case when cust.`phone_service` = 'Yes' then case when cust.`multiple_lines` = 'Yes' then 'Multiple Lines' else 'Single Line' end else 'No Phone' end phone_service_type,
        cust.`internet_service_type_id`,
        ist.`internet_service_type`,
        case when cust.`internet_service_type_id` = 3 then 0 else 1 end internet_service,
        case when cust.`internet_service_type_id` = 1 then 1 else 0 end has_dsl,
        case when cust.`internet_service_type_id` = 2 then 1 else 0 end has_fiber,
        case when cust.`online_security` = 'Yes' then 1 else 0 end online_security,
        case when cust.`online_backup` = 'Yes' then 1 else 0 end online_backup,
        case when cust.`online_security` = 'Yes' or cust.`online_backup` = 'Yes' then 1 else 0 end online_security_backup,
        case when cust.`device_protection` = 'Yes' then 1 else 0 end device_protection,
        case when cust.`tech_support` = 'Yes' then 1 else 0 end tech_support,
        case when cust.`streaming_tv` = 'Yes' then 1 else 0 end streaming_tv,
        case when cust.`streaming_movies` = 'Yes' then 1 else 0 end streaming_movies,
        case when cust.`streaming_tv` = 'Yes' or `streaming_movies` = 'Yes' then 1 else 0 end streaming_services,
        cust.`contract_type_id`,
        ct.`contract_type`,
        case when cust.`contract_type_id` = 1 then 0 else 1 end on_contract,
        case when cust.`contract_type_id` = 1 then 1 else case when cust.`contract_type_id` = 2 then 12 else 24 end end contract_duration,
        case when cust.`paperless_billing` = 'Yes' then 1 else 0 end paperless_billing,
        cust.`payment_type_id`,
        pt.`payment_type`,
        case when pt.`payment_type` like '%%auto%%' then 1 else 0 end auto_pay,
        cust.`monthly_charges`,
        case when cust.`total_charges` = '' then 0 else cast(cust.`total_charges` as decimal(11,2)) end total_charges,
        ((cust.`monthly_charges` * cust.`tenure`) - case when cust.`tenure` = 0 then 0 else cast(cust.`total_charges` as decimal(11,2)) end) / cust.`monthly_charges` tenure_remainder,
        case when cust.`churn` = 'Yes' then 1 else 0 end churn
    from 
        customers cust
    left join 
        contract_types ct
        using(`contract_type_id`)
    left join 
        internet_service_types ist
        using(`internet_service_type_id`)
    left join 
        payment_types pt
        using(`payment_type_id`)
    '''
    return sql_df(sql=sql,db='telco_churn', splain=splain, **kwargs)


