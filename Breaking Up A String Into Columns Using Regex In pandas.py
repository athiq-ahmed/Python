# =============================================================================
# https://chrisalbon.com/python/data_wrangling/pandas_regex_to_create_columns/
# =============================================================================
import re
import pandas as pd

# Create a dataframe with a single column of strings
data = {'raw': ['Arizona 1 2014-12-23       3242.0',
                'Iowa 1 2010-02-23       3453.7',
                'Oregon 0 2014-06-20       2123.0',
                'Maryland 0 2014-03-14       1123.6',
                'Florida 1 2013-01-15       2134.0',
                'Georgia 0 2012-07-14       2345.6']}
data
df = pd.DataFrame(data, columns = ['raw']);df

#Search a column of strings for a pattern
df['raw'].str.contains('....-..-..',regex=True);df

#Extract the column of single digit
df['Gender'] = df['raw'].str.extract('(\d)',expand=True);df

#Extract the column of dates
df['date'] = df['raw'].str.extract('(....-..-..)',expand=True);df

#Extract the column of thousands
df['amount'] = df['raw'].str.extract('(\d\d\d\d\.\d)',expand=True);df

#Extract the column of words
df['state'] = df['raw'].str.extract('([A-Z]\w{0,})',expand=True);df

#view the final dataframw
df

