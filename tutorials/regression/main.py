# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import datasets
import warnings
warnings.filterwarnings("ignore")

pd.set_option('display.max_columns', None)

# ================================================================== #
#                         01. Data                                   #
# ================================================================== #

# Housing Dataset
housing = datasets.fetch_california_housing(as_frame=True)

# Loading data
data = housing.frame

# X features and y labels
X = housing.data
y = housing.target
