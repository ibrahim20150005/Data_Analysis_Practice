'''
Analyse NewYork city fire department Dataset

DESCRIPTION

What to:

A dataset in CSV format is given for the Fire Department of New York City. Analyze the dataset to determine:

1. The total number of fire department facilities in New York city
2. The number of fire department facilities in each borough
3. The facility names in Manhattan

'''
import pandas as pn
from pandas.core.groupby.groupby import GroupBy

df = pn.read_csv('C:/Users/Hima/FDNY.csv',skiprows=1)

#1. The total number of fire department facilities in New York city
print(df.count())

#2. The number of fire department facilities in each borough
GroupBy_Borough = df.groupby("Borough")
print(GroupBy_Borough.size())

#3. The facility names in Manhattan
print(GroupBy_Borough.get_group('Manhattan'))
