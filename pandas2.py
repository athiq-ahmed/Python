# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:18:02 2018

@author: Athiq.Ahmed
"""

# =============================================================================
# Exploring Series
# =============================================================================
#   One dimensional array like object
#   Capable of holding any data type
#   Has an index


import pandas as pd
import numpy as np

#create a series
pd.Series(np.random.randn(5),index=['a','b','c','d','e'])

s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
s[0]
s[:3]


# =============================================================================
# Exploring Dataframe
# =============================================================================
#   Two dimensional tabular data structure
#   Capable of holding any/many data types
#   Index and columns

df = pd.DataFrame(s,columns=['Column1'])
df['Column1']
df['Column2'] = df['Column1'] + 4
df.sort_values(by='Column1',ascending= False)
df[df.Column2 >3]

df.apply(lambda x : min(x) + max(x))
df.Column1.min() + df.Column1.max()

df.describe()


# =============================================================================
# Exploring dataset
# =============================================================================

