#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import pandas_profiling
import os
import matplotlib.pyplot as plt
import seaborn as sns

#from matplotlib import scatter_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import Lasso, Ridge, LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split


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
    
    # Scale the data using Robust Scaler
    scale = RobustScaler()
    transformed = scale.fit_transform(X)
    X = pd.DataFrame(transformed, columns = X.columns)
    
    # Create Train and Test Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    # Create a logistic regression model
    logreg = LogisticRegression(fit_intercept=False, C=1e12, solver='lbfgs')
    
    # Fit the model to the training data
    try:
        model_log = logreg.fit(X_train, y_train)
    except:
        model_log = logreg.fit(np.array(X_train).reshape(-1,1), y_train)
        
    # Add new columns to the given data frame with predicted values and probability of correct predictions
    try:
        df['Predicted_'+predicted_column] = logreg.predict(X)
        df['ProbCorrect_Predicted_'+predicted_column] = logreg.predict_proba(X)[:,1]
    except:
        df['Predicted_'+predicted_column] = logreg.predict(np.array(X).reshape(-1,1))
        df['ProbCorrect_Predicted_'+predicted_column] = logreg.predict_proba(np.array(X).reshape(-1,1))[:,1]
    
    return logreg



def back_fill_from_year(df, year):
    """
    Fills every school's LOCALE and CURROPER values with its year values if it exists. 
    Otherwise, remains np.NaN
    
    Parameters:
    -----------
    df: dataframe
    
    year: int
        year to choose backfill values
       
    Returns:
    --------
    df: dataframe
        df has been altered by the backfilled values
    """
    fill_values = {np.NaN: np.NaN}
    for name in df.loc[df.year==year].INSTNM:
        fill_values[name] = {'LOCALE': df.loc[(df.INSTNM==name)&(df.year==year)].LOCALE, 
                             'CURROPER': df.loc[(df.INSTNM==name)&(df.year==year)].CURROPER}
    
    for name in df.loc[df.year!=year].INSTNM:
        if fill_values.get(name):
            pass
        else:
            fill_values[name]={'LOCALE': np.NaN, 'CURROPER': np.NaN}
    
    df.LOCALE = df.INSTNM.map(lambda name: fill_values.get(name)['LOCALE'])
    df.CURROPER = df.INSTNM.map(lambda name: fill_values.get(name)['CURROPER'])

    return df
