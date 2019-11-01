# Data Dictionary

Field Name|Data in field|Data Type
:--- | :--- | :---
**customer_id**|Unique identifier *Turned into index*|object
**gender**|'Male' or 'Female'|category
**is_male**|True if is gender = 'Male'|bool
**is_female**|True  if gender = 'Female'|bool
**senior_citizen**|True  if customer is a senior citizen|bool
**partner**|True  if customer has a partner|bool
**dependents**|True  if customer has dependents|bool
**family**|True if customer has a partner and/or has dependents|bool
**partner_deps**|Categorical, 'has' or 'no' for partner and dependents|category
**tenure**|Number of months customer has been active; remains static once customer has churned|Int64
**tenure_years**|Number of complete years customer has been active; remains static once customer has churned|Int64
**contract_renews**|Number of times customer has exceeded their term length if not month-to-month|Int64
**remaining_months**|Months remaining on current contract|int64
**thru_first_month**|True if customer has a tenure greater than 1|bool
**thru_first_quarter**|True if customer has a tenure greater than 2|bool
**thru_first_half**|True if customer has a tenure greater than 5|bool
**thru_first_year:**|True if customer has a tenure greater than 11|bool
**thru_first_term**|True if customer has exceeded a full term of their contract|bool
**phone_service**|True if customer has phone service|bool
**multiple_lines**|True if customer has multiple lines|bool
**phone_service_id**|Categorical, numeric ID for type of phone service|category
**phone_service_type**|Categorical, description of phone service type|category
**internet_service_type_id**|Categorical, numeric ID for type of phone service|category
**internet_service_type**|Categorical, description of internet service type|category
**internet_service**|True if customer has an internet service type|bool
**has_dsl**|True if customer has DSL internet service|bool
**has_fiber**|True if customer has Fiber Optic internet service|bool
**online_security**|True if custmer registerd for online security|bool
**online_backup**|True if customer registered for online backup|bool
**online_security_backup**|True if customer registered for online security and/or online backup|bool
**device_protection**|True if customer registered for device protections|bool
**tech_support**|True if customer registered for tech support|bool
**streaming_tv**|True if customer registered for streaming TV channels|bool
**streaming_movies**|True if customer registered for streaming movies|bool
**streaming_services**|True if customer registered for streaming TV channels and/or movies|bool
**streaming_dsl**|True if customer has DSL internet service and registered for streaming TV channels and/or movies|bool
**streaming_fiber**|True if customer has DSL internet service and registered for streaming TV channels and/or movies|bool
**contract_type_id**|Categorical, numeric ID for type of contract (1 = month-to-month, 2 = annual, 3 = two-year)|category
**contract_type**|Categorical, descriptive ID for type of contract|category
**on_contract**|True if customer has an annual or two-year contract|bool
**contract_duration**|Customer's contractual term in months (1, 12, or 24)|int64
**paperless_billing**|True if customer registered for paperless billing|bool
**payment_type_id**|Categorical, numeric ID for method of payment|category
**payment_type**|Categorical, description of method of payment and indicator if payment method is automatic|category
**auto_pay**|True if customer payment type is defined as automatic|bool
**manual_mtm**|True if payment is not automatic and customer is not on contract|bool
**monthly_charges**|Current monthly charges for customer|float
**avg_monthly_variance**|Calculated difference between projected monthly rate based on total charges and stated monthly rate|float
**churn**|True if customer has churned. *Target variable.*|bool
