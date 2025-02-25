import numpy as np
import pandas as pd


def values(func, start, end, step):
    index = np.arange(start, end + step, step)
    return pd.Series(map(func, index), index=index, dtype='float64')


def min_extremum(data):
    return min(data[data == data.min()].index)


def max_extremum(data):
    return max(data[data == data.max()].index)