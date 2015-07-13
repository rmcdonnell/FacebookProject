# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:32:30 2015

@author: bmcdonnell
"""

import numpy as np
import pandas as pd
from my_csv_reader import timed_csv_reader
#train_df = pd.read_csv('data/train.csv', header=0) 
#test_df = pd.read_csv('data/test.csv', header=0) 
#bids_df = pd.read_csv('data/bids.csv', header=0) 

train = timed_csv_reader('data/train.csv', 'rb')
    
test = timed_csv_reader('data/test.csv', 'rb')

bids = timed_csv_reader('data/bids.csv', 'rb')

print train[0]
try:
    print bids[0]
except:
    pass
#test:['bidder_id', 'payment_account', 'address', 'outcome\n']
    
#bids:['bid_id', 'bidder_id', 'auction', 'merchandise', 'device', 'time', 
#    'country', 'ip', 'url\n']



