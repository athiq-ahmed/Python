# Importing the libraray
import pandas as pd

# How to see more than five columns of a data frame output in PyCharm run window
pd.set_option('display.width', 320)
pd.set_option("display.max_columns", 12)

# To get rid of scientific notation
pd.options.display.float_format = '{:.2f}'.format

# read the dataset
data = pd.read_csv(r'C:\Users\athiq.ahmed\Desktop\RB - Chatbot\Reports\MVP2\mvp2_data.csv')

import datetime as dt
data['date'] = pd.to_datetime(data['calendar_day'])
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day'] = data['date'].dt.day

# print the data in a tabular form
import tabulate as tb
print(tb.tabulate(data.head(), headers='keys', tablefmt='psql') )

# List of the columns
data.columns

# list of categorical and numerical columns
data.dtypes
categorical = data.dtypes[data.dtypes=='object'].index ; categorical
numerical = data.dtypes[data.dtypes!='object'].index ; numerical

data[categorical].describe()

# information about the number of observations/columns/categorical variables/numerical variables
print("The total number of observations :", data.shape[0])
print("The total number of columns :", data.shape[1])
print("The total number of categorical columns :", len(categorical))
print("The total number of numerical columns :", len(numerical))


data.groupby(['scenario_code','year'])['mo'].sum()
data.groupby('fpi')[['mo','mo_lc']].sum()
len(data.countryname.unique())  # 160
len(data.brand_name.unique())   # 265
len(data.loc_curr.unique())     # 49
min(data.calendar_day)          # 1/1/2017
max(data.calendar_day)          # 9/9/2018
data['calendar_day'][data.scenario_code=='ACT'].min()
data['calendar_day'][data.scenario_code=='ACT'].max()

data.groupby(['scenario_code','year', 'month'])['mo'].sum()>0
data.groupby(['scenario_code','year', 'month'])['mo'].nlargest(3)
data.groupby(['scenario_code','year', 'month']).filter(lambda x: x['mo'].sum()>0)
['mo'].sum()

data['kpi'][(data.brand=='ABC') & data.country.isnull()].sum()


# define a function to show the unique values of a column
def unique_value(column_name):
    return data.column_name.unique()

data.year.unique()

unique_value(year)


# select top 5 * from data
data.head(5)
print(tb.tabulate(data.head(5), headers='keys', tablefmt='psql'))


# select sum(mo), sum(mo_lc) from data
data[['mo', 'mo_lc']].sum()

# select countryname, count(countryname) as count from data group by countryname
data.groupby('countryname')['countryname'].count()

# select scenario_code, sum(mo) from table_name group by scenario_code
data.groupby('scenario_code')['mo'].sum()

# select sum(mo) from table_name where brand_name ='Dettol'
data['mo'][data['brand_name']=='Dettol'].sum()

# select sum(mo), sum(mo_lc) from table_name where brand_name ='Dettol' and countryname = 'UNITED STATES'
data[['mo','mo_lc']][(data['brand_name']=='Dettol') & (data['countryname']=='United States')].sum()

# select sum(mo), sum(mo_lc) from table_name where brand_name ='Dettol' and countryname = 'UNITED STATES' and scenario_code = 'ACT'
data[['mo','mo_lc']][(data['brand_name']=='Dettol') & (data['countryname']=='United States') & (data['scenario_code']=='ACT')].sum()



data.groupby('year')['year'].count()
data.groupby('scenario_code')[['mo','mo_lc']].sum()
data.groupby(['year','scenario_code'])['mo','mo_lc'].sum()

data['mo'][data.brand_name=='Dettol'].sum()


def fin_query_1p(brand_name_parameter):
    return data['mo'][data.brand_name==brand_name_parameter].sum()

fin_query_1p('Disprin')
fin_query_1p('Dettol')
data.brand_name.unique()[:15,]


def fin_query_2p(brand_name_p, countryname_p):
    return data[['mo','mo_lc']][(data.brand_name==brand_name_p) & (data.countryname==countryname_p)].sum()

fin_query_2p('Dettol', 'UNITED STATES')
fin_query_2p('Dettol', None)
data.countryname.unique()[:10,]

def currency_conv(number):
    number = int(number)
    count = len(str(abs(number)))
    if len(str(abs(number))) > 9:
        print (str(round(number/1000000000,2)) + ' bn')
    elif (len(str(abs(number))) > 6) & (len(str(abs(number))) <= 9):
        print(str(round(number / 1000000, 2)) + ' mn')
    elif (len(str(abs(number))) > 3) & (len(str(abs(number))) <= 6):
        print(str(round(number / 1000, 2)) + ' k')
    else:
        print(number)

currency_conv(1107200000.00)
currency_conv(11072000)
currency_conv(110720)
currency_conv(110)

def fin_query_morep_nn(brand_name_p,countryname_p,loc_curr_p,scenario_code_p='ACT'):
    return data['mo'][(data.brand_name==brand_name_p) & (data.countryname==countryname_p) & (data.loc_curr==loc_curr_p)
               & (data.scenario_code==scenario_code_p)].sum()

fin_query_morep_nn('Dettol','UNITED STATES', 'USD')


def fin_query_morep(brand_name_p,countryname_p,loc_curr_p,scenario_code_p='ACT'):
    return data['mo'][(data.brand_name is None or data.brand_name==brand_name_p) & (data.countryname==countryname_p) & (data.loc_curr==loc_curr_p)
               & (data.scenario_code==scenario_code_p)].sum()

fin_query_morep('Dettol','UNITED STATES', 'USD')


data['mo'][(data.brand_name=='Dettol') & (data.scenario_code == 'ACT')].sum()
data['mo'][(data.brand_name=='Dettol')].sum()

data['mo'][(data.brand_name=='Dettol') & data.countryname.isnull()].sum()
data['mo'][(data.brand_name=='Dettol')].sum()
data['mo'][(data.countryname.isnull())].sum()


data['kpi'][(data.brand=='ABC') & data.country.isnull()].sum()


def coalesce(*args):
    return next(arg for arg in args if arg is not None)

coalesce(None, 'dd')


print(tb.tabulate(data.head(), headers='keys', tablefmt='psql'))


