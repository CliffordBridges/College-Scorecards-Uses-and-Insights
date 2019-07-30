#!/usr/bin/env python
# coding: utf-8

# In[3]:


def create_logistic_regression(df, predictor_columns, predicted_column):
    """
    Creates a logistic regression from input column names to predictor column
    
    Parameters
    ----------
    df: pandas dataframe
        the dataframe's columns should include the predictor_columns and predicted_column
    
    predictor_columns: list
        Should be a subset of columns from df. 
        Should have empty intersection with predicted_column
    
    predicted_column: string
        Should be an element in the list of columns from df. 
        Should not be included in predictor_columns
        
    Returns
    -------
    logreg: logistic regression already trained on training data from predictor columns
    
    Note: This function will change the given dataframe
    """
    
    # Create dataframes( or series) with predictors and  predicted values
    X = df[predictor_columns]
    y = df[predicted_column]
    
    # Create Train and Test Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    # Create a logistic regression model
    logreg = LogisticRegression(fit_intercept=False, C=1e12, solver='lbfgs')
    
    # Fit the model to the training data
    try:
        model_log = logreg.fit(X_train, y_train)
    except:
        model_log = logreg.fit(np.array(X_train).reshape(-1,1), y_train)
        
    # Add a new column to the given data frame with predicted values
    try:
        df_play['Predicted_'+predicted_column] = logreg.predict(X)
    except:
        df_play['Predicted_'+predicted_column] = logreg.predict(np.array(X).reshape(-1,1))
    
    return logreg


# In[ ]:




