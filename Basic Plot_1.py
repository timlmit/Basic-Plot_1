#All useful libraries
import pandas as pd
import plotnine
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np

from pandas.plotting import scatter_matrix
from pandas.plotting import andrews_curves
from pandas.plotting import autocorrelation_plot
from matplotlib import pyplot as plt
from datetime import datetime, timedelta


#Basic Plot
ts = pd.Series(np.random.randn(200), index=pd.date_range("1/1/2021", periods =200))

ts = ts.cumsum()

ts.plot (c="r")

plt.title("Basic Plot")

plt.show()