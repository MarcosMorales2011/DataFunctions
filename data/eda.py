"""Lambdata - a collection of Data Science helper functions"""

# Accessing libraries through pipenv
import pandas as pd
import numpy as np


# Deque class
class Deque:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

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


# Dataframe class
class MyDataFrame(pd.DataFrame):
    # Initiate the object
    def __init__(self, data):
        dt_col = []
        change_col = []
        dtr = data

    # Set the datetime column
    def set_dtcol(self, col):
        dt_col = col

    # Set the column we'll change (currently used for outliers)
    def set_ccol(self, col):
        change_col = col

    # Method to change the column to three separate datetimes
    def date_three_col(self):
        a = pd.DatetimeIndex(self).year
        b = pd.DatetimeIndex(self).month
        c = pd.DatetimeIndex(self).day
        return a, b, c

    # returns all missing values
    def all_nulls(self):
        return self.dtr.isnull().sum().sum()

    # Gets rid of outliers on ccol
    def outliers(self):
        return self.change_col[
            self.change_col.between(self.change_col.quantile(0.01), self.change_col.quantile(0.99))
        ]

    # TODO: print statement


if __name__ == '__main__':
    df = pd.DataFrame({"Dates": ["May 02, 1995", "July 25, 1995", "January 01, 2020", "June 15, 1990"]})
    r = MyDataFrame(df)
