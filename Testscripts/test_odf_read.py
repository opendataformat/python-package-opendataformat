# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:18:21 2024

@author: thartl
"""

import pandas as pd
import zipfile
import opendataformat as odf
import os

#sys.path.append('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/odf')
#import odf

os.chdir("C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/Testscripts")
  
    
    
df = odf.read_odf("testdata/data.zip")

print(df)