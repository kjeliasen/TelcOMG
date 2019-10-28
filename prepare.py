# Exercises
# The end product of this exercise should be the specified functions in a 
# python script named prepare.py. Do these in your 
# classification_exercises.ipynb first, then transfer to the prepare.py file.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler


import acquire as acq

from debug import local_settings, timeifdebug, timeargsifdebug, frame_splain

from acquire import get_telco_data


###############################################################################
### establish DFO class                                                     ###
###############################################################################

class DFO(): 
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

###############################################################################
### preparation functions                                                   ###
###############################################################################

@timeifdebug
def encode_col(df, col, **kwargs):
    '''
    encode_col(df, col, **kwargs)
    RETURNS: df, encoder
    '''
    encoder = LabelEncoder()
    encoder.fit (df[[col]])
    df[[col]] = encoder.transform(df[[col]])
    return df, encoder


@timeifdebug
def simpute(df, column, missing_values=np.nan, strategy='most_frequent', splain=local_settings.splain, **kwargs):
    '''
    simpute(df, column, missing_values=np.nan, strategy='most_frequent', splain=local_settings.splain, **kwargs)
    RETURNS: df
    '''
    df[[column]] = df[[column]].fillna(missing_values)
    imp_mode = SimpleImputer(missing_values=missing_values, strategy=strategy)
    df[[column]] = imp_mode.fit_transform(df[[column]])
    return df


###############################################################################
### split-scale functions                                                   ###
###############################################################################

### Test Train Split ##########################################################
# train, test = train_test_split(df, train_size = .80, random_state = 123)
@timeifdebug
def split_my_data(df, target_column, train_pct=.75, random_state=None, **kwargs):
    X = df.drop([target_column], axis=1)
    y = pd.DataFrame(df[target_column])
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_pct, random_state=random_state)
    return X_train, X_test, y_train, y_test


@timeifdebug
def split_my_data_whole(df, train_pct=.75, random_state=None, **kwargs):
    train, test = train_test_split(df, train_size=train_pct, random_state=random_state)
    return train, test


### Transform Data ############################################################
@timeifdebug
def scalem(scaler, train, test, **kwargs):
    # transform train
    scaler.fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    # transform test
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train_scaled, test_scaled


@timeifdebug
def scale_inverse(train_scaled, test_scaled, scaler, **kwargs):
    # If we wanted to return to original values:
    # apply to train
    train_unscaled = pd.DataFrame(scaler.inverse_transform(train_scaled), columns=train_scaled.columns.values).set_index([train_scaled.index.values])
    # apply to test
    test_unscaled = pd.DataFrame(scaler.inverse_transform(test_scaled), columns=test_scaled.columns.values).set_index([test_scaled.index.values])
    return train_unscaled, test_unscaled


### Standard Scaler ###########################################################
@timeifdebug
def standard_scaler(train, test, copy=True, with_mean=True, with_std=True, **kwargs):
    # create object & fit
    scaler = StandardScaler(copy=copy, with_mean=with_mean, with_std=with_std).fit(train)
    # scale'm
    train_scaled, test_scaled = scalem(scaler=scaler, test=test, train=train)
    return scaler, train_scaled, test_scaled


### Uniform Scaler ############################################################
@timeifdebug
def uniform_scaler(train, test, n_quantiles=100, output_distribution='uniform', random_state=123, copy=True, **kwargs):
    # create scaler object and fit to train
    scaler = QuantileTransformer(n_quantiles=n_quantiles, output_distribution=output_distribution, random_state=random_state, copy=True).fit(train)
    # scale'm
    train_scaled, test_scaled = scalem(scaler=scaler, test=test, train=train)
    return scaler, train_scaled, test_scaled


### Gaussian (Normal) Scaler ##################################################
@timeifdebug
def gaussian_scaler(train, test, method='yeo-johnson', standardize=False, copy=True, **kwargs):
    # create scaler object using yeo-johnson method and fit to train
    scaler = PowerTransformer(method=method, standardize=standardize, copy=copy).fit(train)
    # scale'm
    train_scaled, test_scaled = scalem(scaler=scaler, test=test, train=train)
    return scaler, train_scaled, test_scaled


### MinMax Scaler #############################################################
@timeifdebug
def min_max_scaler(train, test, copy=True, feature_range=(0,1), **kwargs):
    # create scaler object and fit to train
    scaler = MinMaxScaler(copy=copy, feature_range=feature_range).fit(train)
    # scale'm
    train_scaled, test_scaled = scalem(scaler=scaler, test=test, train=train)
    return scaler, train_scaled, test_scaled


### Robust Scaler #############################################################
@timeifdebug
def iqr_robust_scaler(train, test, quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True, **kwargs):
    # create scaler object and fit to train
    scaler = RobustScaler(quantile_range=quantile_range, copy=copy, with_centering=with_centering, with_scaling=with_scaling).fit(train)
    # scale'm
    train_scaled, test_scaled = scalem(scaler=scaler, test=test, train=train)
    return scaler, train_scaled, test_scaled


###############################################################################
### Telco Churn Dat                                                         ###
###############################################################################

@timeifdebug
def prep_telco_churn_data(splain=local_settings.splain, **kwargs):
    '''
    prep_titanic(splain=local_settings.splain, **kwargs)
    RETURNS: df, encoder, scaler
    
    
    # Titanic Data

    # 1. Use the function you defined in acquire.py to load the titanic data set.
    # 2. Handle the missing values in the embark_town and embarked columns.
    # 3. Remove the deck column.
    # 4. Use a label encoder to transform the embarked column.
    # 5. Scale the age and fare columns using a min max scaler. Why might this be 
    # beneficial? When might you not want to do this?
    # 6. Create a function named prep_titanic that accepts the untransformed 
    # titanic data, and returns the data with the transformations above applied.

    # Note: drop columns updated to deck, embarked, passenger_id in explore
    # Note: encoding changed to embark_town
    '''
    df = get_telco_data(splain=splain)
    df.set_index('customer_id')
    df_dtypes = pd.DataFrame(df.dtypes).rename(columns={0:'dtype'}).reset_index()
    category_cols=[
        'partner_deps_id',
        'partner_deps',
        'gender',
        'contract_type_id',
        'internet_service_type_id',
        'internet_service_type',
        'contract_type',
        'payment_type_id',
        'payment_type'
    ]
    for row in np.arange(len(df_dtypes)):
        if df_dtypes.loc[row, 'index'] in category_cols:
            df_dtypes.loc[row, 'dtype'] = 'category'

    dict_dtypes = {}
    for row in np.arange(len(df_dtypes)):
        dict_dtypes[df_dtypes.loc[row,'index']] = df_dtypes.loc[row, 'dtype'] 
    df = df.astype(dict_dtypes)
    
    dfo = prep.set_dfo(dfo_df=df, y_column='churn', splain=True)
    #df.drop(columns=['deck', 'embarked','passenger_id'], inplace=True)
    #df = simpute(df=df, column='embark_town', splain=splain)
    #df, encoder = encode_col(df=df, col='embark_town')
    #scaler = MinMaxScaler()
    #scaler.fit(df[['age','fare']])
    #df[['age','fare']] = scaler.transform(df[['age','fare']])
    return df, #encoder, scaler



@timeifdebug
def xy_df(dataframe, y_column):
    '''
    xy_df(dataframe, y_column)
    RETURNS X_df, y_df

    Pass in one dataframe of observed data and the name of the target column. Returns dataframe of all columns except the target column and dataframe of just the target column.

    If y_column is a list, more than one column can be separated.
    '''
    X_df = dataframe.drop([y_column], axis=1)
    frame_splain(X_df, title='X')
    y_df = pd.DataFrame(dataframe[y_column])
    frame_splain(y_df, title='y')
    return X_df, y_df


@timeifdebug
def df_join_xy(X, y):
    '''
    df_join_xy(X, y)
    RETURNS dataframe X.join(y)

    Allows reconfigurations of X and y based on train or test and scaled or unscaled    
    '''
    join_df = X.join(y)
    frame_splain(join_df, 'join df')
    return join_df


@timeifdebug
def pairplot_train(dataframe, show_now=True):
    '''
    FUNCTION
    RETURNS:
    '''
    plot = sns.pairplot(dataframe)
    if show_now:
        plt.show()
    else:
        return plot


@timeifdebug
def heatmap_train(dataframe, show_now=True):
    '''
    FUNCTION
    RETURNS:
    '''
    plt.figure(figsize=(7,5))
    cor = dataframe.corr()
    plot = sns.heatmap(cor, annot=True, cmap=plt.cm.RdBu_r)
    if show_now:
        plt.show()
    else:
        return plot




@timeifdebug
def set_dfo(dfo_df, y_column, splain=local_settings.splain, **kwargs):
    '''
    set_dfo(dfo_df=get_base_df(), y_column='taxable_value', train_pct=.75, randomer=None, scaler_fn=standard_scaler, **kwargs)
    RETURNS: dfo object with heaping piles of context enclosed
    
    scaler_fn must be a function
    dummy val added to train and test to allow for later feature selection testing
    '''
    dfo = DFO()
    dfo.df = dfo_df
    dfo.y_column = y_column
    return dfo


@timeifdebug
def split_dfo(dfo, train_pct=.7, randomer=None, splain=local_settings.splain, **kwargs):
    '''
    scale_dfo(dfo, scaler_fn=standard_scaler, **kwargs)
    RETURNS: dfo object with heaping piles of context enclosed
    
    scaler_fn must be a function
    dummy val added to train and test to allow for later feature selection testing
    '''
    dfo.randomer = randomer
    dfo.train_pct = train_pct
    dfo.train, dfo.test = split_my_data(df=target_df, random_state=randomer)
    dfo.train_index = dfo.train.index
    frame_splain(dfo.train, 'DFO Train')
    dfo.test_index = dfo.test.index
    frame_splain(dfo.train, 'DFO Test')
    return dfo


@timeifdebug
def scale_dfo(dfo, scaler_fn=standard_scaler, splain=local_settings.splain, **kwargs):
    '''
    scale_dfo(dfo, scaler_fn=standard_scaler, **kwargs)
    RETURNS: dfo object with heaping piles of context enclosed
    
    scaler_fn must be a function
    dummy val added to train and test to allow for later feature selection testing
    '''
    dfo.scaler, dfo.train_scaled, dfo.test_scaled = scaler_fn(train=dfo.train, test=dfo.test)
    dfo.train['dummy_val']=1
    dfo.train_scaled['dummy_val']=1
    dfo.X_train, dfo.y_train = xy_df(dataframe=dfo.train, y_column=y_column)
    dfo.X_test, dfo.y_test = xy_df(dataframe=dfo.test, y_column=y_column)
    dfo.X_train_scaled, dfo.y_train_scaled = xy_df(dataframe=dfo.train_scaled, y_column=y_column)
    dfo.X_test_scaled, dfo.y_test_scaled = xy_df(dataframe=dfo.test_scaled, y_column=y_column)
    return dfo


