"""Lambdata - a collection of Data Science helper functions"""

# Accessing libraries through pipenv
import pandas as pd
import numpy as np

list_2 = [12, 52, 2234, 334/2]
def date_three_col(dr):
  r = pd.to_datetime(dr)
  a = pd.DatetimeIndex(dr).year
  b = pd.DatetimeIndex(dr).month
  c = pd.DatetimeIndex(dr).day
  return a, b, c

def all_nulls(dr):
  return dr.isnull().sum().sum()

def outliers(X):
  return X[X.between(X.quantile(0.01), X.quantile(0.99))]
