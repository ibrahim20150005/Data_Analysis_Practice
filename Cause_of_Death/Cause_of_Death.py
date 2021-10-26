'''
Analysing Cause of Death
DESCRIPTION

What to:

You have been provided with a dataset that lists Ohio State’s leading causes of death from the year 2012.

Using the two data points:

-Cause of deaths and
-Percentile
-Draw a pie chart to visualize the dataset

'''

import matplotlib.pyplot as plt

Cause_of_deaths = ['Chronic Disease', 'Unintetional Injuries', 'Alzheimers', 'Infuenza and Pneumonia', 'Sepsis','Others']
Percentile = [62, 5, 4, 2, 1 , 26]

#set figure size
plt.figure(figsize=(10,7))
explode = (0.03,0.03,0.03,0.03,0.03,0.03)
plt.pie(Percentile,labels=Cause_of_deaths,explode=explode,autopct='%1.1f%%',startangle=90)
plt.title('Ohio State’s leading causes of death from the year 2012')
plt.show()
