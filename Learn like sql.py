import pandas as pd
data2 = pd.read_csv(r'C:/Users/athiq.ahmed/Desktop/RB - Chatbot/Reports/Total data_v3_Test.csv')
data2.shape
data = data2.dropna(axis='columns',how='all')
data.shape
#data.head(5)
data.iloc[0:5,0:5]
data.columns
data.dtypes
#data.groupby('year').sum()

#select sum(mo) from <table> where year = 2018 and brand = 'Dettol'
round(sum(data[(data['year']==2018) & (data['brand']=='Dettol')].mo),2)

# getting values where year = 2018 and brand = dettol
data1 = data[(data['year']==2018) & (data['brand']=='Dettol')] 
data1.head(4)
total = sum(data1.mo)

data.iloc[0:5,0:]
data.date.unique()
import numpy as np
#data['date'] = data['date'].replace(np.nan,0)
data['date'] = data['date'].fillna(0).astype(int)
data.date.unique()

data[['year','month','month1','date']].dtypes
data[['year','month','date']].head(5)

data['date'] = data['date'].astype(str)
data['month'] = data['month'].astype(str)
data['year'] = data['year'].astype(str)
data['test'] = data[['year','month1','date']].apply(lambda x: '-'.join(x),axis=1)
data.iloc[0:5,0:]
chk = data[data['date'] != '0']
chk.head(5)
chk.iloc[0:5,11:]
data.dtypes[['year','month','date','test']]

data.year.unique()
data.month1.unique()
data.date.unique()

def converton(month,month_n):
    data[month_n] = np.where((data[month] == 'Jan'),1,0)
    return data

data11 = converton('month','month_n')
data.head(5)
data.dtypes

data['test2']=pd.to_datetime(data['test'],format = '%y-%m-%d',errors ='coerce')

data[['month']].dtypes
import datetime
data['month_number'] = datetime.datetime.strptime(data['month'], '%b').month
datetime.datetime.strftime(data['month'], '%b')


import numpy as np
data['date'] = data['date'].dropna().apply(np.int64)
data.iloc[0:5,0:]
data.dtypes
data['date'] = int(data['date'])
data['date'] = data['date'].fillna(0).astype(int)

data['new_date'] = str_join([date,month,year],axis = 1)
data_sample = data[data['date'].notnull()]
data_sample.head()
data_sample.dtypes
data_sample['test'] = data_sample['date'] + data_sample['year']
data[data['test'].isnull()].sum()
data.isnull().sum()
data[data.date == None]
data.dtypes
data.head(5)



from datetime import date


def int2date(argdate: int):
    year = int(argdate / 10000)
    month = int((argdate % 10000) / 100)
    day = int(argdate % 100)

    return date(year, month, day)


print(int2date(20160618))

data.head(5)


def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.str.strip()[:3]
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

print(month_string_to_number('october'))

data['month'] = data[month_string_to_number(data['month'])]

import calendar
month_number = list(calendar.month_abbr).index
data['month'] = data[month_number(data['month'])]
data['month'] = data['month'].apply(lambda x: calendar.month_abbr[x])
data['new'] = data['month'].apply(lambda x :list(calendar.month_abbr[x]).index(month_abbr[x]))
list(calendar.month_abbr).index(month_abbr)
data = data2.dropna(axis='columns',how='all')
data.month = pd.to_numeric(data.month, errors='ignore')
data.month = pd.to_numeric(data.month, errors='coerce').fillna(0).astype(np.int64)
data['month'] = np.where(data['month'] == 'Mar', 3, 0)

def change_month(month):
    if month == 'Jan' : return '1'
    elif month == 'Feb' : return '2'
    elif month == 'Mar' : return '3'
    elif month == 'Apr' : return '4'
    elif month == 'May' : return '5'
    elif month == 'Jun' : return '6'
    elif month == 'Jul' : return '7'
    elif month == 'Aug' : return '8'
    elif month == 'Sep' : return '9'
    elif month == 'Oct' : return '10'
    elif month == 'Nov' : return '11'
    elif month == 'Dec' : return '12'
    else: return '100'
        
change_month('Ma')
data['month1'] = data['month'].apply(lambda x: change_month('month'))

data.loc[data['month'].str.contains("Jan"),'month1'] = '01'
data.loc[data['month'].str.contains("Feb"),'month1'] = '02'
data.loc[data['month'].str.contains("Mar"),'month1'] = '03'
data.loc[data['month'].str.contains("Apr"),'month1'] = '04'
data.loc[data['month'].str.contains("May"),'month1'] = '05'
data.loc[data['month'].str.contains("Jun"),'month1'] = '06'
data.loc[data['month'].str.contains("Jul"),'month1'] = '07'
data.loc[data['month'].str.contains("Aug"),'month1'] = '08'
data.loc[data['month'].str.contains("Sep"),'month1'] = '09'
data.loc[data['month'].str.contains("Oct"),'month1'] = '10'
data.loc[data['month'].str.contains("Nov"),'month1'] = '11'
data.loc[data['month'].str.contains("Dec"),'month1'] = '12'

data['month1'] = data['month1'].astype(str)


data.head(5)
data.month.unique()
data.month1.unique()
data.dtypes



def month_converter(month):
#    month = month.strip()[:3].title()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1

month_converter('jan')
month_converter(data['month'])
data['month2'] = data[month_converter(data['month'])]


##############################################################################################################################
##############################################################################################################################
    #Get the date value saved in the column new_date2 which is the concatenation of year,month and date
    #and if date is null the new_date2 should have the last day of the month and this variable should be in 
    #date format

import pandas as pd
import numpy as np
data2 = pd.read_csv(r'C:/Users/athiq.ahmed/Desktop/RB - Chatbot/Reports/Total data_v3_Test.csv')
data = data2.dropna(axis='columns',how='all')
data.head(5)
data.dtypes

data.date.unique()
data['date'] = data['date'].fillna(99).astype(int)
data['date'] = data.date.map("{:02}".format)
data.date.unique()

data.loc[data['month'].str.contains("Jan"),'month1'] = '01'
data.loc[data['month'].str.contains("Feb"),'month1'] = '02'
data.loc[data['month'].str.contains("Mar"),'month1'] = '03'
data.loc[data['month'].str.contains("Apr"),'month1'] = '04'
data.loc[data['month'].str.contains("May"),'month1'] = '05'
data.loc[data['month'].str.contains("Jun"),'month1'] = '06'
data.loc[data['month'].str.contains("Jul"),'month1'] = '07'
data.loc[data['month'].str.contains("Aug"),'month1'] = '08'
data.loc[data['month'].str.contains("Sep"),'month1'] = '09'
data.loc[data['month'].str.contains("Oct"),'month1'] = '10'
data.loc[data['month'].str.contains("Nov"),'month1'] = '11'
data.loc[data['month'].str.contains("Dec"),'month1'] = '12'

data.dtypes
data.month.unique()
data.month1.unique()

data['year'] = data['year'].astype(str)

data.date.unique()
data['new_date1'] = np.where(data['date']=='99',
    data['year']+'-'+data['month1']+'-'+'01',
    data['year']+'-'+data['month1']+'-'+data['date'])
data.head(5)
chk = data[data['date'] != '99']
chk.head(5)
data.dtypes

from pandas.tseries.offsets import MonthEnd
data['new_date2'] = np.where(data['date']=='99',
                    pd.to_datetime(data['new_date1'], format="%Y-%m-%d") + MonthEnd(1),
                    pd.to_datetime(data['new_date1'],format = '%Y-%m-%d'))
data.head(5)
data.dtypes
chk = data[data['date'] !='99']
chk.head(5)

data = data.drop(['new_date1'],axis =1)
data.head(5)

data = data.rename(columns={'new_date2':'New_date'})
data.tail(5)

#select sum(ytd) from <dataset> where country = 'India' and brand = 'Dettol'
round(sum(data[(data['country']=='India') & (data['brand']=='Dettol')].ytd),2)
round(sum(data[(data['brand']=='Dettol')].ytd),2)

#select sum(ytd) from dataset where country ='' and brand ='' and fpi ='' and month ='' and year =''
filtered_data = data[
                  (data['country'] =='India') 
                & (data['brand'] =='Dettol') 
                & (data['fpi'] =='Gross Sales 3rd Party') 
                & (data['month'] =='Mar') 
                & (data['year'] =='2018')
                ]
filtered_data.head(10)
sum(filtered_data.ytd)
sum(filtered_data.mo)

filtered_data['ytd'].sum()
filtered_data['mo'].sum()

#filtered_data.dtypes

#select sum(ytd) from <dataset> group by fpi
data.groupby(['fpi'])['ytd'].sum()

#select sum(ytd) from dataset group by year and rephrase the exponential number to normal number
round(data.groupby(['year'])['ytd'].sum(),2).map("{:01}".format)

#take the recent 3 months for each year
data.groupby('year')['month'].unique()

chk = data.groupby(['year','month1'],sort = True).sum().sort_index(ascending = False)
chk.head(6)

data.dtypes
data.year.unique()
#Define a function with a year filter and respective mo/ytd column
#select sum(ytd) from dataset where year ='2018'
#data[data['year']=='2018']['ytd'].sum()
def year_only(a,b):
    chk= data[data['year'] == a][b].sum()
    return chk
year_only('2017','ytd')
year_only('2017','mo')

#Define a function with fpi & year filter and respective mo/ytd column
#data.groupby(['fpi'])['ytd'].sum()
def groupby_ex1(a,b):
#    chk = data.groupby([a])['ytd'].sum()
    chk = data.groupby([a])[b].sum()
    return chk
groupby_ex1('fpi','mo')


#Define a function with year & month1 filter and respective mo/ytd column and get only the respective rows
#data.groupby(['year','month1'])['ytd'].sum().head(3)
def groupby_ex2(a,b,c,d,e):
    chk = e.groupby([a,b])[c].sum().head(d)
    return chk
groupby_ex2('year','month1','ytd',4,data)


#Define a function to sum the values based on mo/ytd column
#Get the sum(mo/ytd) based on the new_Date filter 
#data.groupby(['fpi'])['ytd'].sum()
def groupby_ex3(a,b):
    chk = data.groupby([a])[b].sum()
    return chk
groupby_ex3('fpi','ytd')


#Get one query for all the filters such as
#select sum(ytd) from dataset where brand ='' and country ='' and fpi = '' and scenario_code='' 
#and month='' and year=''

# IF all the fields are given
def filter_data_1(a,b,c,d,e,f):
    filtered_data = data[
                  (data['country'] ==a) 
                & (data['brand'] ==b) 
                & (data['fpi'] ==c) 
                & (data['month'] ==d) 
                & (data['year'] ==e)
                ]
#    chk = sum(filtered_data.ytd)
    chk = filtered_data[f].sum()
    return chk
    
filter_data_1('India','Dettol','Gross Sales 3rd Party','Mar','2018','ytd')
filter_data_1('India','Dettol','Gross Sales 3rd Party','Mar','2018')

# IF some of the fields are given
def filter_data_2(a,b,c,d,e,f):
    filtered_data = data[
                  (data['country'] ==a) 
                & (data['brand'] ==b) 
                & (data['fpi'] ==c) 
                & (data['month'] ==d) 
                & (data['year'] ==e)
                ]
#    chk = sum(filtered_data.ytd)
    chk = filtered_data[f].sum()
    return chk


chk = data[data['country']=='India']



# change the fpi into short names
data[:2]
data.fpi.unique()

def fpi_short(fpi):
    if fpi =='COP':
        return 'COP'
    elif fpi == 'Gross Margin 3rd Party':
        return 'Margin'
    elif fpi == 'Total Marketing Spend':
        return 'Marketing'
    elif fpi =='Net Revenue Third Party':
        return 'Revenue'
    elif fpi =='Gross Sales 3rd Party':
        return 'Sales'
    else:
        return 'Not known'

fpi_short('Athiq')

data['fpi_1']=data['fpi'].apply(fpi_short)
#data =data.drop('fpi1',axis=1)
data.head(5)



#Add a new column called quarter and calculate the sum(mo/ytd) based on the conditions




#Get the top/bottom performing brands 


