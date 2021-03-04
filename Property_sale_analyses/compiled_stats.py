import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
df_property_1 = pd.read_csv("cleaned1_property_sales.csv")

sns.stripplot(x = "SALEDATE", y = "PRICE", data = df_property_1)
