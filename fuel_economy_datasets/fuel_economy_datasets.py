'''
Assessing Data
The files all_alpha_08.csv and all_alpha_18.csv discussed in the previous pages have been provided in the workspace for you here to access. Use pandas to explore these datasets in the Jupyter Notebook below to answer the quiz questions below the notebook about these characteristics of the data:

number of samples in each dataset
number of columns in each dataset
duplicate rows in each dataset
datatypes of columns
features with missing values
number of non-null unique values for features in each dataset
what those unique values are and counts for each
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df_all_alpha_08 = pd.read_csv("C:/Users/Hima/fuel_economy_datasets/all_alpha_08.csv")


df_all_alpha_18 = pd.read_csv("C:/Users/Hima/fuel_economy_datasets/all_alpha_18.csv")

#number of samples in each dataset in 2008
df_all_alpha_08.index.size

#number of samples in each dataset in 2018
df_all_alpha_18.index.size

#number of columns in each dataset in 2008
df_all_alpha_08.columns.size

#number of columns in each dataset in 2018
df_all_alpha_18.columns.size

#duplicate rows in each dataset in 2008
df_all_alpha_08.duplicated().sum()


#duplicate rows in each dataset in 2018
df_all_alpha_18.duplicated().sum()

#datatypes of columns for dataset in 2008
df_all_alpha_08.info()

#datatypes of columns for dataset in 2018
df_all_alpha_18.info()

#features with missing values for dataset in 2008
df_all_alpha_08.isna().sum()

#features with missing values for dataset in 2018
df_all_alpha_18.isna().sum()

#Type of Object
type(df_all_alpha_08['Cyl'][0])

#number of non-null unique values for features in each dataset
df_all_alpha_08.info()
df_all_alpha_18.info()

#what those unique values are and counts for each
df_all_alpha_08.nunique()
df_all_alpha_18.nunique()


#to check that the type of fuel is found
df_all_alpha_18[df_all_alpha_18['Fuel']=='Electricity']
df_all_alpha_18[df_all_alpha_18['Fuel']=='Electricity']

## Cleaning Column Labels ##
"""
1. Drop extraneous columns
Drop features that aren't consistent (not present in both datasets) or aren't
relevant to our questions. Use Pandas' drop function.
(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.
html)
Columns to Drop:
From 2008 dataset: 'Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'
From 2018 dataset: 'Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'
2. Rename Columns
Change the "Sales Area" column label in the 2008 dataset to "Cert Region" for
consistency.
Rename all column labels to replace spaces with underscores and convert
everything to lowercase. (Underscores can be much easier work with in Python
than spaces. For example, having spaces wouldn't allow you to use df.column_name
instead of df['column_name'] to select columns or use query(). Being consistent
with lowercase and underscores also helps make column names easy to remember.)
"""

# Drop Extraneous Columns
# drop columns from 2008 dataset
df_all_alpha_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1,
inplace=True)

# confirm changes
df_all_alpha_08.head(1)

# drop columns from 2018 dataset
df_all_alpha_18.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'], axis=1,
inplace=True)

# confirm changes
df_all_alpha_18.head(1)

# Rename Columns
# rename Sales Area to Cert Region
df_all_alpha_08.rename(columns={'Sales Area':'Cert Region'}, inplace=True)
# confirm changes
df_all_alpha_08.head(1)

# replace spaces with underscores and lowercase labels for 2008 dataset
df_all_alpha_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
# confirm changes
df_all_alpha_08.head(1)
# replace spaces with underscores and lowercase labels for 2018 dataset
df_all_alpha_18.rename(columns=lambda x: x.strip().lower().replace(" ","_"), inplace=True)
# confirm changes
df_all_alpha_18.head(1)

# confirm column labels for 2008 and 2018 datasets are identical
df_all_alpha_08.columns == df_all_alpha_18.columns
# make sure they're all identical like this
(df_all_alpha_08.columns == df_all_alpha_18.columns).all()

'''
Filter, Drop Nulls, Dedupe
1. Filter
For consistency, only compare cars certified by California standards. Filter both datasets using query to select only rows where cert_region is CA. Then, drop the cert_region columns, since it will no longer provide any useful information (we'll know every value is 'CA').

2. Drop Nulls
Drop any rows in both datasets that contain missing values.

3. Dedupe
Drop any duplicate rows in both datasets.
'''

#  Filter both datasets using query to select only rows where cert_region is CA
df_all_alpha_08 = df_all_alpha_08[df_all_alpha_08['cert_region']=='CA']
df_all_alpha_18 = df_all_alpha_18[df_all_alpha_18['cert_region']=='CA']

# drop the cert_region columns

df_all_alpha_08.drop(['cert_region'],axis=1,inplace=True)
df_all_alpha_18.drop(['cert_region'],axis=1,inplace=True)

# Drop Nulls

df_all_alpha_08.dropna(inplace=True)
df_all_alpha_18.dropna(inplace=True)


# Drop any duplicate rows in both datasets

df_all_alpha_08.drop_duplicates(inplace=True)
df_all_alpha_18.drop_duplicates(inplace=True)

'''
Fixing Data Types
In the next three sections, you'll make the following changes to make the datatypes consistent and practical to work with.
'''

'''
Fix cyl datatype
2008: extract int from string.
2018: convert float to int.
'''
df_all_alpha_08['cyl'] = df_all_alpha_08['cyl'].str.extract('(\d+)').astype(int)


df_all_alpha_18['cyl'] = df_all_alpha_18['cyl'].astype(int)



'''
Fix air_pollution_score datatype
2008: convert string to float.
2018: convert int to float.
'''
df_all_alpha_08['air_pollution_score'] = df_all_alpha_08['air_pollution_score'].str.extract('(\d+)').astype(float)
df_all_alpha_18['air_pollution_score'] = df_all_alpha_18['air_pollution_score'].astype(float)


'''
Fix city_mpg, hwy_mpg, cmb_mpg datatypes
2008 and 2018: convert string to float.
'''
df_all_alpha_08['city_mpg'] = df_all_alpha_08['city_mpg'].str.extract('(\d+)').astype(float)
df_all_alpha_08['hwy_mpg'] = df_all_alpha_08['hwy_mpg'].str.extract('(\d+)').astype(float)
df_all_alpha_08['cmb_mpg'] = df_all_alpha_08['cmb_mpg'].str.extract('(\d+)').astype(float)


df_all_alpha_18['city_mpg'] = df_all_alpha_18['city_mpg'].str.extract('(\d+)').astype(float)
df_all_alpha_18['hwy_mpg'] = df_all_alpha_18['hwy_mpg'].str.extract('(\d+)').astype(float)
df_all_alpha_18['cmb_mpg'] = df_all_alpha_18['cmb_mpg'].str.extract('(\d+)').astype(float)

'''
Fix greenhouse_gas_score datatype
2008: convert from float to int.
'''
df_all_alpha_08['greenhouse_gas_score'] = df_all_alpha_08['greenhouse_gas_score'].str.extract('(\d+)').astype(int)


'''
Exploring with Visuals
Use histograms and scatterplots to explore 
Then, answer the quiz questions below the notebook.
'''
'''
#Compare the distributions of greenhouse gas score in 2008 and 2018.
df_all_alpha_08['greenhouse_gas_score'].hist()
df_all_alpha_18['greenhouse_gas_score'].hist()

plt.xlabel("the distributions of greenhouse gas score in 2008 and 2018", fontsize=16)  
#create legend
labels= ["greenhouse gas score in 2008","greenhouse gas score in 2018"]
plt.legend(labels)


#How has the distribution of combined mpg changed from 2008 to 2018?
df_all_alpha_08['cmb_mpg'].hist()
df_all_alpha_18['cmb_mpg'].hist()

plt.xlabel("the distribution of combined mpg changed from 2008 to 2018", fontsize=16)  
#create legend
labels= ["combined mpg score in 2008","combined mpg gas score in 2018"]
plt.legend(labels)


#Describe the correlation between displacement and combined mpg.

plt.scatter(df_all_alpha_08['displ'], df_all_alpha_08['cmb_mpg'])
plt.scatter(df_all_alpha_18['displ'], df_all_alpha_18['cmb_mpg'])


plt.xlabel(" displacement in 2008 and 2018", fontsize=10)  
plt.ylabel(" combined mpg in 2008 and 2018")
#create legend
labels= ["displacement and combined mpg in 2008","displacement and combined mpg in 2018"]
plt.legend(labels)

#Describe the correlation between greenhouse gas score and combined mpg.

plt.scatter(df_all_alpha_08['greenhouse_gas_score'], df_all_alpha_08['cmb_mpg'])
plt.scatter(df_all_alpha_18['greenhouse_gas_score'], df_all_alpha_18['cmb_mpg'])


plt.xlabel(" greenhouse gas score in 2008 and 2018", fontsize=10)  
plt.ylabel(" combined mpg in 2008 and 2018")
#create legend
labels= ["greenhouse gas score and combined mpg in 2008","greenhouse gas score and combined mpg in 2018"]
plt.legend(labels)
'''
'''
Conclusions & Visuals
Draw conclusions and create visuals to communicate results in the Jupyter notebook below! Make sure to address the following questions.
'''
#Q1: Are more unique models using alternative fuels in 2018 compared to 2008? By how much?

# set labeles
x_08 = df_all_alpha_08['fuel'].unique()
x_18 = df_all_alpha_18['fuel'].unique()

#set y_axis
y_08 = df_all_alpha_08['fuel'].value_counts().values
y_18 = df_all_alpha_18['fuel'].value_counts().values




fig, ax = plt.subplots()
rects1 = ax.bar(x_08, y_08, 0.35, label='2008')
rects2 = ax.bar(x_18 , y_18, 0.35, label='2018')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Count')
ax.set_title('types of Fuel')
ax.legend()

#Q2: How much have vehicle classes improved in fuel economy (increased in mpg)?

veh_08 = df_all_alpha_08.groupby(['veh_class']).cmb_mpg.mean()
veh_18 = df_all_alpha_18.groupby('veh_class').cmb_mpg.mean()
print(veh_08)
print(veh_18)
inc = veh_18 - veh_08
print(inc)
inc.dropna(inplace=True)
print(inc)
plt.subplots(figsize=(8, 5))
plt.bar(inc.index, inc)
plt.title('Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Increase in Average Combined MPG');

#Q3: What are the characteristics of SmartWay vehicles? Have they changed over time? (mpg, greenhouse gas)
print(df_all_alpha_08.head())
print(df_all_alpha_08.smartway.value_counts())
print(df_all_alpha_18.smartway.value_counts())
print(df_all_alpha_18.smartway.unique())
smart_08 = df_all_alpha_08.query('smartway == "no"')
print(smart_08.describe())
smart_18 = df_all_alpha_18.query('smartway == "Elite"')
print(smart_18.describe())

# Q4: What features are associated with better fuel economy?
print(df_all_alpha_08.describe())
print(df_all_alpha_18.describe())


for name in df_all_alpha_08.columns:
    print(name[0:10]+'_2008')


df_all_alpha_08.rename(columns=lambda x: x[:10]+'_2008', inplace=True)

print(df_all_alpha_08.columns)

df_combined = pd.concat([df_all_alpha_08,df_all_alpha_18])
print(df_combined)
print(df_combined.columns.size)
'''
Results with Merged Dataset
Use the notebook below to answer the final question with the merged dataset.

Q5: For all of the models that were produced in 2008 that are still being produced now, how much has the mpg improved and which vehicle improved the most?

Here are the steps for answering this question.

'''

'''
1. Create a new dataframe, model_mpg, that contain the mean combined mpg values in 2008 and 2018 for each unique model
To do this, group by model and find the mean cmb_mpg_2008 and mean cmb_mpg for each.
'''
model_mpg = df_combined.groupby('model').mean()[['cmb_mpg_2008', 'cmb_mpg']]
print(model_mpg)

'''
2. Create a new column, mpg_change, with the change in mpg
Subtract the mean mpg in 2008 from that in 2018 to get the change in mpg
'''
model_mpg['mpg_change'] = model_mpg['cmb_mpg']-model_mpg['cmb_mpg_2008']
print(model_mpg.head())

'''
3. Find the vehicle that improved the most
Find the max mpg change, and then use query or indexing to see what model it is!
'''

max_mpg_change = model_mpg['mpg_change'].max()
print(max_mpg_change)

idx = model_mpg.mpg_change.idxmax()
print(idx)
