'''
Analyse the Federal Aviation Authority Dataset using Pandas
DESCRIPTION

Problem:

Analyze the Federal Aviation Authority (FAA) dataset using Pandas to do the following:

1. View
aircraft make name
state name
aircraft model name
text information
flight phase
event description type
fatal flag
2. Clean the dataset and replace the fatal flag NaN with “No”

3. Find the aircraft types and their occurrences in the dataset

4. Remove all the observations where aircraft names are not available

5. Display the observations where fatal flag is “Yes”

'''

import pandas as pn

df = pn.read_csv('C:/Users/Hima/faa_ai_prelim.csv')

# view the shape of data set
print(df.shape)

# view the first five of data set
print(df.head())

# view all columns of data set
print(df.columns)

# create data fram with only requierd columns

new_df_columns = df[['ACFT_MAKE_NAME','LOC_STATE_NAME','ACFT_MODEL_NAME','RMK_TEXT','FLT_PHASE','EVENT_TYPE_DESC','FATAL_FLAG'] ]

print(new_df_columns.head())

# Clean the dataset and replace the fatal flag NaN with “No”
new_df_columns['FATAL_FLAG'].fillna(value='No',inplace=True)
print(new_df_columns.head())

# Find the aircraft types and their occurrences in the dataset
# Remove all the observations where aircraft names are not available
final_dataset = new_df_columns.dropna(subset=['ACFT_MAKE_NAME'])
aircraft = final_dataset.groupby("ACFT_MAKE_NAME")
print(aircraft.size())

# Display the observations where fatal flag is “Yes”
fatal_flag = final_dataset.groupby("FATAL_FLAG")
print(fatal_flag.get_group('Yes'))