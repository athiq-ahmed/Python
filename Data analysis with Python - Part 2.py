# =============================================================================
# https://www.dataquest.io/blog/pandas-tutorial-python-2/
# =============================================================================
import pandas as pd
data = pd.read_csv(r'C:\Users\athiq.ahmed\Desktop\Other\Python code\Datasets\thanksgiving-2015-poll-data.csv',encoding ='Latin-1')
data.head(4)
data.columns[:5]

data['Do you celebrate Thanksgiving?'].unique()
data["What is your gender?"].unique()
data["What is your gender?"].value_counts(dropna=False)


#Applying functions to Series in pandas

#3 ways to create a new column if nan values are present
#1. SUB WHERE condition's
import numpy as np
data['gender1'] = np.where(data["What is your gender?"]=='Male',1,data["What is your gender?"])
data['gender1'] = np.where(data["gender1"]=='Female',0,data["gender1"])

data["gender1"].unique()
data["gender1"].value_counts(dropna=False)

#2. WHERE condition
data['gender2'] = np.where(data["What is your gender?"].isnull(), data["What is your gender?"], 
                    np.where(data["What is your gender?"]=="Male", 0, 1))
data["gender2"].unique()
data["gender2"].value_counts(dropna=False)

#3. IF condition
def gender_code(x):
    if (pd.isnull(x)):
        return x
    elif (x=="Male"):
        return 1
    else:
        return 0

data['gender3'] = data["What is your gender?"].apply(gender_code)
data.gender3.unique()
data.gender3.value_counts(dropna = False)

data.dtypes

data = data.drop(['gender1','gender2'],axis=1)
data = data.rename(columns={'gender3':'gender'})
data.head()


#Applying functions to DataFrames in pandas
data.dtypes.head()
data.apply(lambda x :x.dtype).head()
data['RespondentID'].dtypes

#Using the apply method to clean up income
data["How much total combined money did all members of your HOUSEHOLD earn last year?"].dtypes
data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts(dropna = False)
data["How much total combined money did all members of your HOUSEHOLD earn last year?"].head()

import math
def clean_income(x):
    if x =='$200,000 and up':
        return 200000
    elif x =="Prefer not to answer":
        return np.nan
    elif isinstance(x,float) and math.isnan(x):
#    elif isinstance(x,float):
        return np.nan
    x = x.replace(",","").replace("$","")
    income_low,income_high = x.split(" to ")
    return(int(income_low)+int(income_high))/2

data['Income'] = data['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(clean_income)    
data['Income'].head()


#Grouping data with pandas
data["What type of cranberry saucedo you typically have?"].value_counts()

homemade = data[data["What type of cranberry saucedo you typically have?"]=='Homemade'];homemade.head()
canned = data[data["What type of cranberry saucedo you typically have?"]=='Canned'];canned.head()

homemade['Income'].mean()
canned['Income'].mean()

grouped = data.groupby("What type of cranberry saucedo you typically have?");grouped
grouped.groups
grouped.size()

for name,group in grouped:
    print(name)
    print(group.shape)

grouped['Income'].size()


#Aggregating values in groups
grouped['Income'].agg(np.mean)
grouped.agg(np.mean)

#Plotting the results of aggregation
#%matplotlib inline
sauce = grouped.agg(np.mean);sauce
sauce['Income'].plot(kind='bar')

#Aggregating multiple columns
grouped = data.groupby(["What type of cranberry saucedo you typically have?", "What is typically the main dish at your Thanksgiving dinner?"],sort=True)
grouped.agg(np.mean)

#Aggregating with multiple functions
grouped['Income'].agg([np.mean,np.sum,np.std]).head(10)

#Using apply on groups
grouped = data.groupby("How would you describe where you live?")["What is typically the main dish at your Thanksgiving dinner?"]
grouped.apply(lambda x:x.value_counts())



