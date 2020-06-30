# =============================================================================
# https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html
# =============================================================================

import pandas as pd
import numpy as np

url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv'
tips = pd.read_csv(url)
tips.head()

#Select statement
#select total_bill, tip, sex from tips limit 5
tips[['total_bill','tip','sex']].head()

#Where condition
#select * from tips where time= 'dinner'
tips[tips['time'] =='Dinner'].head()

#select count(*) from tips where time ='Dinner'
a = tips['time']=='Dinner'
a.value_counts()

#select * from tips where time = 'Dinner' and tip > 5;
a = tips[(tips['time'] =='Dinner') & (tips['tip'] > 5)]
a.head()

#select sum(tip) from tips where time ='Dinner' and tip > 5
sum(tips[(tips['time'] =='Dinner') & (tips['tip'] > 5)].tip)

#select * from tips where size >= 5 or total_bill > 45
a = tips[(tips['size'] >=5) | (tips['total_bill'] > 45)]

#select sum(tips) from tips where size >=5 or total_bill > 45
sum(tips[(tips['size'] >= 5) | (tips['total_bill'] > 45)].tip)
sum(a['tip'])


#Null checking is done using notna and isna method
frame = pd.DataFrame({'col1': ['A','B',np.nan,'C','D'],
                      'col2':['F',np.nan,'G','H','I']
                      })
frame

#select * from frame where col2 is null
frame[frame['col2'].isna()]

#select * from frame where col2 is not null
frame[frame['col2'].notna()]

#Group by
#select sex, count(*) from tips group by sex;
tips.groupby('sex').size()

#Notice that in the pandas code we used size() and not count(). This is because count()
#applies the function to each column, returning the number of not null records within each.
tips.groupby('sex').count()

#Alternatively, we could have applied the count() method to an individual column
tips.groupby('sex')['total_bill'].count()

#select day, avg(tip),count(*) from tips group by day
tips.groupby('day').agg({'tip':np.mean,'day':np.size})

#select smoker,day,count(*),avg(tip) from tips group by smoker,day
tips.groupby(['smoker','day']).agg({'smoker':np.size,'tip':np.mean})
tips.groupby(['smoker','day']).agg({'tip':[np.size,np.mean]})

#Join
df1 = pd.DataFrame({'key':['A','B','C','D'],
                    'value':np.random.randn(4)})
df1

df2 = pd.DataFrame({'key':['B','D','D','E'],
                    'value':np.random.randn(4)})
df2

#Inner join
#select * from df1 inner join df2 on df1.key = df2.key;
pd.merge(df1,df2,on='key')

#merge() also offers parameters for cases when you’d like to join one DataFrame’s column with 
#another DataFrame’s index
pd.merge(df1,df2,on ='key',right_index=True)
pd.merge(df1,df2,on ='key',left_index=True)

#Left outer join
pd.merge(df1,df2,on='key',how='left')

#Right join
pd.merge(df1,df2,on='key',how='right')

#Full join
pd.merge(df1,df2,on='key',how='outer')

#union
df1 = pd.DataFrame({'city':['chicago','san fransico','new york city'],
                    'rank': range(1,4)})
df1
df2 = pd.DataFrame({'city':['chicago','boston','los angeles'],
                    'rank':[1,4,5]})
df2

#select city,rank from df1 
#union all 
#select city,rank from df2
pd.concat([df1,df2])

#select city,rank from df1 
#union 
#select city,rank from df2
pd.concat([df1,df2]).drop_duplicates()

#Pandas equivalents for some SQL analytic and aggregate functions

#top n rows with offset
#select top 5 * from tips;
#select * from tips order by tips offset 5;
tips.nlargest(6,columns = 'tip')

#update
    #update tips
    #set tip = tip* 2
    #where tip < 2;
tips['tip2'] = np.where(tips['tip'] < 2,
                tips['tip'] * 2, 
                tips['tip'])
tips.head(5)

#tips.loc[tips['tip'] < 2, 'tip'] *= 2

#Delete
#delete from tips where tip >9 ;
tips = tips.loc[tips['tip'] <= 9]



