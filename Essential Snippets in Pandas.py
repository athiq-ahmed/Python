# =============================================================================
# https://jeffdelaney.me/blog/useful-snippets-in-pandas/
# =============================================================================
#1. Importing a CSV File
import pandas as pd
import numpy as np

url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv'
tips = pd.read_csv(url);tips.head()
tips_col = pd.read_csv(url,usecols=['total_bill','tip']);tips_col.head(5)

#2. Exploring Data in a DataFrame
        #df.head()       # first five rows
        #df.tail()       # last five rows
        #df.sample(5)    # random sample of rows
        #df.shape        # number of rows/columns in a tuple
        #df.describe()   # calculates measures of central tendency
        #df.info()       # memory footprint and datatypes

df = tips.copy()
df.head()
df.tail()
df.sample(5)
df.describe()
df.info()


#3. Adding a New Column to a DataFrame
df['new_column'] = 23

full_price = (df.total_bill + df.tip)
df['original_price'] = full_price

#Column in certain order
df.insert(0,'original_price',full_price)
df.insert(1,'new_columnm','1')
df.head()

#4. Select a Specific “Cell” Value
df.loc[0:2]
df.ix[0,'tip']

#5.Filtering DataFrames with Conditional Logic
filter = df[df['tip'] > 5]
filter = df[(df['tip'] > 5) & (df['sex']=='Male')]
filter.head()

#6. Sorting a DataFrame by a Certain Column
chk = df.sort_values('total_bill',axis=0,ascending = False)
chk.head()

#7. Apply a Function to Every Row in a Column
def example1(col):
    total_bill2 = col * 100
    return total_bill2
df['total_bill_n'] = df.total_bill.apply(example1)
df.head(3)


#8. Add a New Column with Conditional Logic
df['new_logic'] = np.where(df['sex']== 'Male',"M",df['sex'])
df.head(5)

#9. Finding the Mean or Standard Deviation of Multiple Columns or Rows
df.total_bill.mean()
df.total_bill.std()

#10. Converting a DataFrame to a Numpy Array
    #Converting the the values in a DataFrame to an array is simple
df.values

    #If you want to preserve the table presentation
df.as_matrix


#11. Combining DataFrames with Concatenation
df1 = pd.DataFrame({'key': ['A', 'B', 'C'],
                    'key2': [1,2,3]})
df1
df2 = pd.DataFrame({'key': ['B','E','C'],
                    'key4': np.random.randn(3)
                    })
df2

pd.concat([df1,df2],axis = 0) #vertically
pd.concat([df1,df2],axis = 1) #horizontally

#12. Combining DataFrames based on an Index Key
merge_Df = pd.merge(df1,df2,how = 'inner',on='key')
merge_Df

#13. Converting Dates to their own Day, Week, Month, Year Columns
df.head()
from datetime import datetime
from datetime import timedelta

date_1 = datetime.today().strftime('%Y-%M-%D');date_1
date_1 = datetime.today().strftime('%D');date_1
date_2 = datetime.now();date_2
new_date = date_1 + timedelta(days=10);new_date
date_2.month
date_2.year

#14. Finding NaNs in a DataFrame
df.isna().sum().sum() #Count the total number of NaNs present
df.isna().sum()       #List the NaN count for each column

#15. Filling NaNs or Missing Data
data = df.fillna('Athiq')
data = df.dropna(axis=0)

#16. Extracting Features by Grouping Columns
import numpy as np
df.groupby('sex').size()
df.groupby('sex')['total_bill'].agg(np.mean)
df.groupby('sex')['total_bill'].agg({'total_bill': [np.mean,np.std]})


#17.Creating Bins
bins = [0,20,25,30]
names =['Cheap','Normal','Expensive']
df['price_point'] = pd.cut(df.total_bill,bins,labels=names);df.head(3)
df.groupby('price_point').size()

#18. Creating a new Column by Looping
def new_condition(param):
    for row in df.tip:
        if param < 5:
            return 'Less then 5'
        elif param >=5 and param <=8:
            return 'Less then 8'
        else:
            return 'Greater then 8'

df['new_loop'] = df.tip.apply(new_condition);df.head(5)
chk = df[df.tip>5];chk.head(4)

#19. Loading Massive Datasets in Smaller Chunks
chunksize = 500
chunks = []
for chunk in pd.read_csv('pizza.csv', chunksize=chunksize):
    # Do stuff...
    chunks.append(chunk)

df = pd.concat(chunks, axis=0)


