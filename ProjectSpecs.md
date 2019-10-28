# Classification Project

## Why are our customers churning?
*Some questions I have include:*

- *Could the month in which they signed up influence churn? i.e. if a cohort is identified by tenure, is there a cohort or cohorts who have a higher rate of churn than other cohorts?* (Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total customers))
- *Are there features that indicate a higher propensity to churn? like type of internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?*
- *Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point? If so, what is that point for what service(s)?*
- *If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?*

## Deliverables:

1. I will need a report (ipynb) answering the question, "Why are our customers churning?" I want to see the analysis you did to answer my questions and lead to your findings. Please clearly call out the questions and answers you are analyzing. E.g. If you find that month-to-month customers churn more, I won't be surprised, but I am not getting rid of that plan. The fact that they churn is not because they can, it's because they can *and* they are motivated to do so. I want some insight into *why* they are motivated to do so. I realize you will not be able to do a full causal experiment, but I hope to see some solid evidence of your conclusions.

2. I will also need you to deliver to me a csv with the customer_id, probability of churn, and the prediction of churn (1=churn, 0=not_churn). 

3. I also need 1-3 google slides *(plus title)* that illustrates how your model works, including the features being used, so that I can deliver this to the SLT when they come with questions about how these values were derived. 

    **Please make sure you include how likely your model is to give a high probability of churn when churn doesn't occur, to give a low probability of churn when churn occurs, and to accurately predict churn.**

    *(Note: Zach likes diagrams!)*

4. I'll schedule some time to meet with you on Wednesday morning so that you can present to me your findings with you slides prepared.

5. Finally, our development team will need a .py file that will take in a new dataset, (in the exact same form of the one you acquired from `telco_churn.customers`) and perform all the transformations necessary to run the model you have developed on this new dataset to provide probabilities and predictions.

## Specification

Detailed instructions for each section are below.

In general, make sure you document your work. You don't need to explain what every line of code is doing, but you should explain what and why you are doing. For example, if you drop a feature from the dataset, you should explain why you decided to do so, or why that is a reasonable thing to do. If you transform the data in a column, you should explain why you are making that transformation.

In addition, you should not present numers in isolation. If your code outputs a number, be sure you give some context to the number.

### Specific Deliverables:
- a **jupyter notebook** where your work takes place
- a **csv file** that predicts churn for each customer
- **`acquire.py`**, **`prepare.py`**, **`model.py`** (you may decide to separate tasks into others, such as `preprocessing.py` or `features.py`)
- a **google slide presentation** summarizing your model
- a **`README.md`** file that contains a link to your google slides presentation, and instructions for how to use your python script(s)

### Project Planning

1. summary of project and goals

2. task out how you will work through the pipeline, in as much detail as you need to keep on track.

3. incluce data dictionary **<-- note this**

4. clearly state your starting hypotheses (and add the testing of these to your task list)

### Acquisition

1. **`Acquire.py`**
    - Acquire data from the customers table from the telco_churn database on the codeup data science database server.
    - You will want to join some tables as part of your query.
    - This data should end up in a pandas data frame.

2. **Notebook**
    - run `acquire.py`
    - summarize data (.info(), .describe(), .value_counts(), ...)
    - plot distributions of individual variables

**Removed**
*Write a function, `peekatdata(dataframe)`, that takes a dataframe as input and computes and returns the following:*
    - *creates dataframe object `head_df` (df of the first 5 rows) and prints contents to screen*
    - *creates dataframe object `tail_df` (df of the last 5 rows) and prints contents to screen*
    - *creates tuple object `shape_tuple` (tuple of (nrows, ncols)) and prints tuple to screen*
    - *creates dataframe object `describe_df` (summary statistics of all numeric variables) and prints contents to screen.*
    - *prints to screen the information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage.*

### Data Prep

1. **`Prepare.py`**
    - split data to train/test
    - Handle Missing Values
    - Handle erroneous data and/or outliers you wish to address
    - encode variables as needed
    - scale data as needed
    - new feature that represents tenure in years
    - create single variable representing the information from `phone_service` and `multiple_lines`
    - do the same using `dependents` and `partner`
    - other ways to merge variables, such as `streaming_tv` & `streaming_movies`, `online_security` & `online_backup`

2. **Notebook**
    - Explore missing values and document takeaways/action plans for handling them.
        - should you remove the observations with a missing value for that variable? *(remove row)*
        - should you remove the variable altogether? *(remove column)*
        - is missing equivalent to 0 (or some other constant value) in the specific case of this variable?
        - should you replace the missing values with a value it is most likely to represent, like mean/median/mode?
    - Document your takeaways.
    - explore data types and adapt types or data values as needed to have numeric represenation of each attribute.
    - run `prepare.py`

**Removed**
1. *Write a function, `df_value_counts(dataframe)`, that takes a dataframe as input and computes and returns the values by frequency for each column. The function should decide whether or not to bin the data for the value counts.*

3. *Transform `churn` such that "yes" = 1 and "no" = 0*

7. *Figure out a way to capture the information contained in `streaming_tv` and `streaming_movies` into a single variable of dtype int. Transform the data and place in a new column `streaming_services`.*

8. *Figure out a way to capture the information contained in `online_security` and `online_backup` into a single variable of dtype int. Transform the data and place in a new column `online_security_backup`.*

11. *Numeric Scaling: scale the monthly_charges and total_charges data. Make sure that the parameters for scaling are learned from the training data set.*

### Data Exploration

Answer the key questions, your hypotheses, and figure out the drivers of churn.

1. Could the month in which they signed up influence churn? i.e. if a cohort is identified by tenure, is there a cohort or cohorts who have a higher rate of churn than other cohorts? (Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total customers)). **(Definitely answer this question)**

2. Are there features that indicate a higher propensity to churn? like type of internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?

3. Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point? If so, what is that point for what service(s)? **(Definitely answer this question)**

4. If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable? **(Definitely answer this question)**

5. Controlling for services (`phone_id`, `internet_service_type_id`, `online_security_backup`, `device_protection`, `tech_support`, and `contract_type_id`), is the mean monthly_charges of those who have churned significantly different from that of those who have not churned? (Use a t-test to answer this.)

6. How much of `monthly_charges` can be explained by `internet_service_type`? *(hint: correlation test.)* State your hypotheses and your conclusion clearly.

7. How much of `monthly_charges` can be explained by `internet_service_type` + phone service type (0, 1, or multiple lines). State your hypotheses and your conclusion clearly.

8. Create visualizations exploring the interactions of variables (independent with independent and independent with dependent). The goal is to identify features that are related to churn, identify any data integrity issues, understand 'how the data works'. For example, we may find that all who have online services also have device protection. In that case, we don't need both of those. (The visualizations done in your analysis for questions 1-5 count towards the requirements below)

9. What can you say about each variable's relationship to churn, based on your initial exploration? If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.

10. Summarize your conclusions, provide clear answers to the specific questions, and summarize any takeaways/action plan from the work above.

**Removed**

8. *Create visualizations exploring the interactions of variables (independent with independent and independent with dependent). The goal is to identify features that are related to churn, identify any data integrity issues, understand 'how the data works'. For example, we may find that all who have online services also have device protection. In that case, we don't need both of those.* 
*(The visualizations done in your analysis for questions 1-5 count towards the requirements below)*
    - *Each independent variable (except for `customer_id`) should be visualized in at least two plots, and at least 1 of those compares the independent variable with the dependent variable.*
    - *For each plot where x and y are independent variables, add a third dimension (where possible), of churn represented by color.*
    - *Use subplots when plotting the same type of chart but with different variables.*
    - *Adjust the axes as necessary to extract information from the visualizations (adjusting the x & y limits, setting the scale where needed, etc.)*
    *Add annotations to at least 5 plots with a key takeaway from that plot.*
    - *Use plots from matplotlib, pandas and seaborn.*
    - *Use each of the following:*
        - *`sns.heatmap`*
        - *`pd.crosstab` (along with `sns.heatmap`)*
        - *`pd.scatter_matrix`*
        - *`sns.barplot`*
        - *`sns.swarmplot`*
        - *`sns.pairplot`*
        - *`sns.jointplot`*
        - *`sns.relplot` or `plt.scatter`*
        - *`sns.distplot` or `plt.hist`*
        - *`sns.boxplot`*
        - *`plt.plot`*
    - *Use at least one more type of plot that is not included in the list above.*

### Modeling
1. Feature Selection: Are there any variables that seem to provide limited to no additional information? If so, remove them.

2. Train (fit, transform, evaluate) multiple different models, varying the model type and your meta-parameters.

3. Compare evaluation metrics across all the models, and select the best performing model.

4. Test the final model (transform, evaluate) on your out-of-sample data (the testing data set). Summarize the performance. Interpret your results.