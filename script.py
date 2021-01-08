from FinanceAPI import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from urllib.request import urlopen

with open('Secret_Key.txt') as f:
    key = f.read()

f = FinanceAPI()
f.registerKey_(key)

apple_dict=f.build_dict('AAPL')

df = f.build_dataframe(['TSLA','NVDA','AAPL','MSFT'])

df = f.df
df_large_cap = df[df['Market Cap']>200e9]
df_large_cap[['companyName','Market Cap']]


