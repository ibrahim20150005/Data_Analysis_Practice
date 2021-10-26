'''
IBM HR Analytics Employee Attrition Modeling .
DESCRIPTION

IBM is an American MNC operating in around 170 countries with major business vertical as computing, software, and hardware.
Attrition is a major risk to service-providing organizations where trained and experienced people are the assets of the company. The organization would like to identify the factors which influence the attrition of employees.

Data Dictionary

Age: Age of employee
Attrition: Employee attrition status
Department: Department of work
DistanceFromHome
Education: 1-Below College; 2- College; 3-Bachelor; 4-Master; 5-Doctor;
EducationField
EnvironmentSatisfaction: 1-Low; 2-Medium; 3-High; 4-Very High;
JobSatisfaction: 1-Low; 2-Medium; 3-High; 4-Very High;
MaritalStatus
MonthlyIncome
NumCompaniesWorked: Number of companies worked prior to IBM
WorkLifeBalance: 1-Bad; 2-Good; 3-Better; 4-Best;
YearsAtCompany: Current years of service in IBM
Analysis Task:
- Import attrition dataset and import libraries such as pandas, matplotlib.pyplot, numpy, and seaborn.
- Exploratory data analysis

Find the age distribution of employees in IBM
Explore attrition by age
Explore data for Left employees
Find out the distribution of employees by the education field
Give a bar chart for the number of married and unmarried employees
- Build up a logistic regression model to predict which employees are likely to attrite.

'''
import matplotlib
from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.indexes.base import Index

dataframe = pd.read_csv('H:/Data Science/Datasets/IBM Attrition Data.csv')
dataframe.head()
name = dataframe.columns.values

def Education(num):
    if num == 1:
        return 'Below College'
    elif num == 2:
        return 'College'    
    elif num == 3:
        return 'Bachelor'        
    elif num == 4:
        return 'Master'
    else:
        return 'Doctor'

dataframe['Education'] = dataframe['Education'].apply(Education)


def EnvironmentSatisfaction(num):
    if num == 1:
        return 'Low'
    elif num == 2:
        return 'Medium'    
    elif num == 3:
        return 'High'    
    else:
        return 'Very High'

dataframe['EnvironmentSatisfaction'] = dataframe['EnvironmentSatisfaction'].apply(EnvironmentSatisfaction)

def JobSatisfaction(num):
    if num == 1:
        return 'Low'
    elif num == 2:
        return 'Medium'    
    elif num == 3:
        return 'High'    
    else:
        return 'Very High'

dataframe['JobSatisfaction'] = dataframe['JobSatisfaction'].apply(JobSatisfaction)

def WorkLifeBalance(num):
    if num == 1:
        return 'Bad'
    elif num == 2:
        return 'Good'    
    elif num == 3:
        return 'Better'    
    else:
        return 'Best'

dataframe['WorkLifeBalance'] = dataframe['WorkLifeBalance'].apply(WorkLifeBalance)



#Find the age distribution of employees in IBM
dataframe['Age'].hist(bins=60,figsize=[10,10])
plt.title("Age distribution of Employees")
plt.xlabel("Age")
plt.ylabel(" Count of Employees")
plt.show()


#Explore attrition by age
plt.figure(figsize=(10,10))
plt.scatter(dataframe.Attrition,dataframe.Age,alpha=.50)
plt.title("attrition by age")
plt.xlabel("attrition")
plt.ylabel("Age")
plt.grid(b=True, which='major',axis='y')
plt.show()


# explore data for Left employees breakdown\n
plt.figure(figsize=(8,6))
dataframe.Attrition.value_counts().plot(kind='barh',color='blue',alpha=.65)
plt.title("Attrition breakdown")
plt.show()

#Find out the distribution of employees by the education field
myexplode = [0.05, 0, 0, 0, 0]
mylabels = dataframe.groupby('Education').size().index
sizes =  dataframe.groupby('Education').size().values
plt.figure(figsize=(8,6))
plt.pie(sizes,labels=mylabels,explode=myexplode, autopct='%1.1f%%',shadow=True,startangle=90)
plt.title("the distribution of employees by the education field")
plt.show() 



#Give a bar chart for the number of married and unmarried employees
xaxis= dataframe.groupby('MaritalStatus').size().index
yaxis=dataframe.groupby('MaritalStatus').size().values
plt.bar(xaxis,yaxis,width=0.3,color="#4CAF50",alpha=.9)
plt.show()