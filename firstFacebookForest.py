# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:32:30 2015

@author: bmcdonnell
"""

import csv as csv
import numpy as np
import pandas as pd
from my_csv_reader import timed_csv_reader

train = []
train_csv_file_obj = csv.reader(open('train.csv', 'rb'))
for row in train_csv_file_obj:
    train.append(row)
    
test = []
test_csv_file_obj = csv.reader(open('test.csv', 'rb'))
for row in test_csv_file_obj:
    test.append(row)

