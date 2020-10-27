"""Lambdata - a collection of Data Science helper functions"""

# Accessing libraries through pipenv
import pandas as pd
import numpy as np


class Deque():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop(-1)

    def size(self):
        return len(self.items)


def date_three_col(dr):
    r = pd.to_datetime(dr)
    a = pd.DatetimeIndex(dr).year
    b = pd.DatetimeIndex(dr).month
    c = pd.DatetimeIndex(dr).day
    return a, b, c


def all_nulls(dr):
    return dr.isnull().sum().sum()


def outliers(X):
    return X[
      X.between(X.quantile(0.01), X.quantile(0.99))]
