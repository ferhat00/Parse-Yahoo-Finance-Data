# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 14:37:28 2017

@author: Ferhat
"""
import pandas as pd
import numpy as np
import os
import time
from datetime import datetime
from yahoo_finance import Share

data = pd.read_csv('companylist.csv')

x = []
df = pd.DataFrame(columns = ['Symbol','Get Open','Get Price','Market Cap', 'Div Yield'])

i = 0
for i in range (0,10):
    
    yahoo = Share(data.loc[i,"Symbol"])

    
    
    df=df.append({'Symbol':data.loc[i,"Symbol"],'Get Open':yahoo.get_open(),'Get Price':yahoo.get_price(),'Market Cap':yahoo.get_market_cap(),'Div Yield':yahoo.get_dividend_yield()},ignore_index = True)
    
    
    
    df.to_csv('out.csv')   