# College-Scorecards-Uses-and-Insights

[College ScoreCard](https://collegescorecard.ed.gov/data/) raw data lives here.

## Contents

- [Introduction](#Introduction)
- [Analysis](#Analysis)
    - [Data Collection](#Data-Collection)
    - [Data Cleaning](#Data-Cleaning)
    - [Exploratory Data Analysis](#Exploratory-Data-Analysis)
    - [Regression](#Regression)
- [Summary of Files](#Files-summary)


## Introduction

The College ScoreCard data tracks nearly 2000 parameters for almost all colleges and universities in the United States and its territories which are or have been operational since the 1996-1997 academic year. 
These parameters are meant to summarize cost, graduation rates, employment rates, loan rates, and default rates for each college or university in order to help applicants and their gaurdians make more informed decisions. 
The goal of this project is to begin drawing connections in the data that may help applicants understand the vast number of parameters which may affect their higher education. 
Specifically, this project 
1. uses a linear regression to identify relationships between tuition costs and instructional expenditures, 
2. uses a logistic regression to show student default rates are correlated with institutional ownership, and 
3. uses time series to predict average tuition costs through 2028.


## Analysis

### Data Collection

The raw data from [College ScoreCard](https://collegescorecard.ed.gov/data/) is very large; the zip file is 256 MB, containing 1 CSV for each (academic) year since 1996. 
Due to the size, this repo only contains a .pkl containing the following parameters: INSTNM, HIGHDEG, CONTROL, REGION, LOCALE, CURROPER, TUITFTE, INEXPFTE, CDR3, LO_INC_DEBT_N, MD_INC_DEBT_N, HI_INC_DEBT_N, ICLEVEL, and year. 
This .pkl is in [data](https://github.com/CliffordBridges/College-Scorecards-Uses-and-Insights/tree/ridge_regression/data).

### Data Cleaning

Through the years since 1996, more and more information has been tracked about colleges and universities. 
This leads to increasing number of ```NaN``` values as we go backwards through time in the data. 
Some of these values can be filled, such as whether or not the insitution is currently operational, while many other parameters can not, such as 3 year default rates for students in 1997. 
Due to this, the cleaning in the project involves dropping many rows or focusing on recent data. 
All cleaning can be found in the appropriate notebook in [notebooks](https://github.com/CliffordBridges/College-Scorecards-Uses-and-Insights/tree/ridge_regression/notebooks).

### Exploratory Data Analysis

With such a high natural variance in most of the features like tuition cost, faculty pay, etc., we found difficulties in identifying trends upon visualizing the data. 
For this reason, we chose several intuitively related features to begin this analysis.

### Regression



## Summary of Files

All details from regression analysis are in the technical notebook in the [notebooks](https://github.com/CliffordBridges/College-Scorecards-Uses-and-Insights/tree/ridge_regression/notebooks) folder. 
The pickle file containing the data on which anaylis was run is in the [data](https://github.com/CliffordBridges/College-Scorecards-Uses-and-Insights/tree/ridge_regression/data) folder.

