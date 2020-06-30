# =============================================================================
# https://www.dataquest.io/blog/pandas-python-tutorial/
# =============================================================================

import pandas as pd
reviews = pd.read_csv(r'C:\Users\athiq.ahmed\Desktop\Other\Python code\Datasets\ign.csv');reviews.head()
reviews.shape

#Indexing datframes with pandas
reviews.head()
reviews.iloc[0:5,:]
reviews.iloc[:5,:]   ## the first 5 rows, and all of the columns for those rows.
reviews.iloc[:,:]    ## the entire dataframe
reviews.iloc[5:,5:]  ## rows from position 5 onwards, and columns from position 5 onwards.
reviews.iloc[:,0]    ## the first column, and all of the rows for the column.
reviews.iloc[9,:]    ## the 10th row, and all of the columns for that row.


reviews = reviews.iloc[:,1:]
reviews.head()


#Indexing using labels in pandas
reviews.loc[0:5,:] ## We can work with labels using the pandas.DataFrame.loc method, which allows us to index using labels instead of positions.
reviews.index



