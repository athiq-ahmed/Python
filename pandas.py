# =============================================================================
# http://pandas.pydata.org/pandas-docs/version/0.15/10min.html#min
# =============================================================================
#1.Object creation
#2.Viewing data
#3.Selection

#Importing the required libraries

import pandas as pd
import numpy as np

# =============================================================================
# object creation
# =============================================================================
#Creating a Series by passing a list of values, letting pandas create a default integer index
series = pd.Series([1,2])
series_agan = pd.Series([1,2,3,4,np.nan])

# Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns.
dates = pd.date_range('20131010',periods=5)

df = pd.DataFrame(np.random.randn(5,2),index=dates,columns=list('AB'))
df = pd.DataFrame([1,2,3,4,5],[1,2,3,4,4],columns=['Athiq'])


a = np.random.randn(1,10)
a = np.random.random_sample(12)

array = []
dictionary = {}

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df1 = pd.DataFrame({'A': 1,
                          'B': 'Ahmed',
                          'C': 'Chk'},index=[0])

# =============================================================================
# Viewing data
# =============================================================================
df.head(n=2)    #to get the top rows(default = 5)
df.tail()       #to get the bottom rows(default =5)
df.index        #Display the index,columns, and the underlying numpy data
df.columns      #to get the column names of the dataframe
list(df)        #to get the column names of the dataframe
df.dtypes       #to get the column types
df.describe()   #to get the quick summary of the dataframe
df.mean()       #to get the mean value
df.T            #transpose the values
df.sort_index(axis=1,ascending = False)     #sorting by index
df.sort_values(by='A',ascending = False)    #sorting by respective column

# =============================================================================
# Selection
# =============================================================================
df['A']         #Selecting a single column
df.A            #Selecting a single column
df[0:2]         #Selecting via [], which slices the rows
df['2010/01/01':'2010/01/03']
df[0:1]
df.loc[dates[0]]

df.iloc[0:3,0:4]      #Selection by position
df.iloc[[1,3],[1,4]]  #Selection by position
df.iloc[0:3,:]
df[df.A > 0]         #Boolean indexing
df[df>0]             #where operation

df = df.drop(columns = 'E', axis =1)
df2 = df.copy()
df2['E']=['one','two','three','four','five']
df2[df2['E'].isin(['one','two'])]  #using the .isin method

# Setting
s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))  #Defining a list of series
df2['F']=s1                 #Adding one more column to dataframe df2

# Missng values
df2.iloc[0:2,4] = 1         #Replacing the values with 1
df2.dtypes                  #Identifying the data types
df2.dropna(how='any')       #drop the observations where missing values are present
df2.fillna(value=5)         #fill the observations where missing values are present
pd.isnull(df2)              #one more technique to identify missing values using pandas.isnull(dataframe)


# Operations
df = df.fillna(5)
df.mean()
df.sum(1)

s=pd.Series([1,2,3,np.nan,4],index=dates).shift(2)
df.sub(s,axis='index')

# Apply
df.apply(np.cumprod)
df.apply(lambda x: x.max() - x.min())

# Histogramming
s =pd.Series(np.random.randint(0,10,size=5))
s.value_counts()
s.sum()

# String methods
s = pd.Series(['A','B','C','a','b',np.nan])
s.str.lower()

# =============================================================================
# Merge
# =============================================================================

# Concat
df = pd.DataFrame(np.random.randn(10,5))
pieces = [df[:3],df[3:7],df[7:]]
pd.concat(pieces)

# Join
left = pd.DataFrame({'key':['foo','foo'], 'lval':[1,2]})
right = pd.DataFrame({'key' : ['foo','foo'],'rval' : [3,4]})
pd.merge(left,right,on='key')

# Append
df = pd.DataFrame(np.random.randn(10,4),columns = ['A','B','C','D'])
s = df.iloc[3]
df.append(s,ignore_index=True)

# =============================================================================
# Grouping
# =============================================================================
