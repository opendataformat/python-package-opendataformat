# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:13:55 2024

@author: thartl
"""

import pickle
import pandas as pd
import tempfile
import unittest

import opendataformat as odf
import os

#sys.path.append('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/opendataformat')
#import odf2pd as odf

os.chdir('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/Testscripts')

data = odf.read_odf('testdata/data.zip')
with open('testdata/data.pkl', 'wb') as f:
    pickle.dump(data, f)

data_with_default = odf.read_odf('testdata/data_with_default.zip')
with open('testdata/data_with_default.pkl', 'wb') as f:
    pickle.dump(data_with_default, f)


data_with_missings = odf.read_odf('testdata/data_with_missings.zip')
with open('testdata/data_with_missings.pkl', 'wb') as f:
    pickle.dump(data_with_missings, f)




#with open('testdata/data.pkl', 'rb') as f:
#    df = pickle.load(f)

#with open('testdata/data_with_default.pkl', 'rb') as f:
#    df = pickle.load(f)
    
#with open('testdata/data_with_missings.pkl', 'rb') as f:
#    df = pickle.load(f)
    
    
