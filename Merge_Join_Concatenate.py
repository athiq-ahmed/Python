# =============================================================================
# http://pandas.pydata.org/pandas-docs/version/0.15/merging.html
# =============================================================================

# Concatenating objects
import pandas as pd
df1 = pd.DataFrame(
        {'A': ['A0','A1','A2','A3'],
         'B': ['B0','B1','B2','B3'],
         'C': ['C0','C1','C2','C3'],
         'D': ['D0','D1','D2','D3']},
         index = [1,2,3,4]
         )
df2 = pd.DataFrame(
        {'A': ['A4','A5','A6','A7'],
         'B': ['B4','B5','B6','B7'],
         'C': ['C4','C5','C6','C7'],
         'D': ['D4','D5','D6','D7']},
         index = [1,2,3,4]
         )
df3 = pd.DataFrame(
        {'A': ['A8','A9','A10','A11'],
         'B': ['B8','B9','B10','B11'],
         'C': ['C8','C9','B11','B11'],
         'E': ['D8','D9','D10','D11']},
         index = [1,2,3,4]
         )
frames = [df1,df2,df3]
result = pd.concat(frames)                                          # Combine the dataframes
result = pd.concat(frames,ignore_index=True)                        # Clear the existing index and reset it in the result by setting the ignore_index option to True
result = pd.concat(frames,ignore_index=True,verify_integrity=True)  # Prevent the result from including duplicate index values with the verify_integrity option

result = pd.concat(frames,keys=['x','y','z'])                       # Construct hierarchical index using the passed keys as the outermost level
result.loc['y']                                                     #  select out each chunk by key

df4= pd.DataFrame({'B':['B2','B3','B6','B7'],
                   'D':['D2','D3','D6','D7'],
                   'F':['F2','F3','F6','F7']
                       },
                    index = [1,2,3,4])

result = pd.concat([df1,df4])
result = pd.concat([df1,df4],axis =1)
result = pd.concat([df1,df4],axis =1,join ='inner')
result = pd.concat([df1,df4],axis =1,join_axes=[df1.index])

#Concatenating using append
df1
df2
result = df1.append(df2,ignore_index=True)
df4
result = df1.append(df4)
result = df1.append([df2,df3])
s1 = pd.Series(['X0','X1','X2','X3'],name = 'X',index=[1,2,3,4])
result = pd.concat([s1,df1],axis =1)         # Concatenating with mixed ndims

s2 =pd.Series(['_0','_1','_2','_3'],index=[1,2,3,4])
result = pd.concat([df1,s1,s2,s2],axis=1)   # If unnamed Series are passed they will be numbered consecutively.

s3 = pd.Series([0,1,2,3],name='foo')
s4 = pd.Series([0,1,2,3])
s5 = pd.Series([0,1,4,5])
pd.concat([s3,s4,s5],axis=1)
pd.concat([s3,s4,s5],axis=1,keys=['red','blue','yellow'])

result = pd.concat(frames,keys=['x','y','z'])
pieces = {'x':df1,'y':df2,'z':df3}
result = pd.concat(pieces)
result = pd.concat(pieces,keys =['z','y'])

# Appending rows to a DataFrame
s2 = pd.Series(['x1','x2','x3','x4'],index=['A','B','C','D'])
df1
result = df1.append(s2,ignore_index=True)

dict = [{'A':1,'B':2,'C':3,'D':4},
        {'A':5,'B':6,'C':7,'D':8}]
result = df1.append(dict,ignore_index=True)


# =============================================================================
# Database-style DataFrame joining/merging
# =============================================================================
import pandas as pd
left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})  # Creating a dataframe as 'left'
right = pd.DataFrame({'key':['foo','foo'],'rval':[4,5]}) # Creating a dataframe as 'right'
merge = pd.merge(left,right,on='key')                    # Merging both the datasets using the column 'key'

#Example with multiple key joins
left = pd.DataFrame({'key1':['foo','foo','bar'],              # Creating a dataframe 'left' with multiple key values
                     'key2':['one','two','one'],
                     'lval':[1,2,3]
                     })

right = pd.DataFrame({'key1':['foo','foo','bar','bar'],    # Creating a dataframe 'left' with multiple key values
                      'key2':['one','one','one','two'],
                      'rval':[4,5,6,7]
                      })
merge = pd.merge(left,right,how='outer') # using pd.merge to outer merge two dataframes 
merge = pd.merge(left,right,how='inner') # using pd.merge to inner merge two dataframes 

# Joining on index
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8,4),columns = ['A','B','C','D']) # creating a dataframe with 8 rows and 4 columns 
df1 = df.loc[1:,['A','B']]  # Creating a new dataframe starting from 1st row and 2 columns
df2 = df.loc[:5,['C','D']]  # Creating a new dataframe ending with 5th row and 2 columns
df1.join(df2)               # Joining two dataframes with the help of 'join' function
df1.append(df2)             # checking the append function here
pd.merge(df1,df2,how='left') # checking how does the pd.merge function works without specifing the index options
df1.join(df2,how='outer')  # joining two datasets using outer join
df1.join(df2,how='inner')  # joining two datasets using inner join

# Same output can be applied using merge by adding additional parameters to use index
merge = pd.merge(df1,df2,left_index=True,right_index=True,how='outer')
merge = pd.merge(df1,df2,left_index=True,right_index=True,how='inner')

# Joining key columns on index
import pandas as pd
import numpy as np
df = df1.copy()                     # copying the df1 data to df so any changes made to df will not affect df1
dict = [{'A':0.1234,'B':-0.1234}]   # creating a dictionary
df = df.append(dict,ignore_index=True)  # Adding a row with two columns using append method
df['key']=['foo','bar']*2               # Creating a new variable and repeating the same value by 4 times    
to_join = pd.DataFrame(np.random.rand(2,2),columns=['j1','j2'],index=['bar','foo'])  # creating a dataframe with 2 rows and 2 columns and with index values
df.join(to_join,on='key')  # Joining the datasets using on method(key in this example)
merge = pd.merge(df,to_join,left_on='key',right_index=True,how='left',sort=False) # The same output can be replicated by using pd.merge with adding the parameters as shown in the code

# To join on multiple keys, the passed DataFrame must have a MultiIndex
index = pd.MultiIndex(levels =[['foo','bar','baz','qux'],
                               ['one','two','three']],
                      labels=[[0,0,0,1,1,2,2,3,3,3],
                              [0,1,2,0,1,1,2,0,1,2]],
                      names=['first','second'])             # This is the index created which levels and labels(sub levels)

to_join = pd.DataFrame(np.random.rand(10,3),columns=['j_one','j_two','j_three'],index=index) # A dataframe created

key1 = ['bar','bar','bar','foo','foo','baz','baz','qux','qux','snap'] # this is just a list
key2 = ['two','one','three','one','two','one','two','two','three','one'] # this is just a list

len(key1)
data = np.random.rand(len(key1))  # Generating the random integers based on the lenght of key1
data = pd.DataFrame({'key1':key1,
                     'key2':key2,
                     'data':data}) # A dataframe 

data # Display
to_join # Display
data.join(to_join,on=['key1','key2']) # Joining based on the multiple keys (outer join)
data.join(to_join,on=['key1','key2'],how='inner') # Joining based on the multiple keys (inner join)

# Overlapping value columns
left = pd.DataFrame({'key':['foo','foo'],'value':[1,2]})
right = pd.DataFrame({'key':['foo','foo'],'value':[4,5]})
merge = pd.merge(left,right,on='key',suffixes=('_left','_right'))

# Merging ordered data
A = pd.DataFrame({'group':['a','a','a','b','b','b'],
                  'key':['a','c','e','a','c','e'],
                  'lvalue':[1,2,3,1,2,3]
                  })
B = pd.DataFrame({'key':['b','c','d'],
                  'rvalue':[1,2,3]
                  })
merge = pd.ordered_merge(A,B,on='key',left_by = 'group',fill_method='ffill')

