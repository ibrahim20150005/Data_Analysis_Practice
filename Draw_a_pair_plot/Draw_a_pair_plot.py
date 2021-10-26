'''
Draw a pair plot using seaborn library
DESCRIPTION

Problem:

Analyze the “auto mpg data” and draw a pair plot using seaborn library for mpg, weight, and origin.

Sources:

(a) Origin:  This dataset was taken from the StatLib library maintained at Carnegie Mellon University.

-Number of Instances: 398
-Number of Attributes: 9 including the class attribute
-Attribute Information:
-mpg: continuous
-cylinders: multi-valued discrete
-displacement: continuous
-horsepower: continuous
-weight: continuous
-acceleration: continuous
-model year: multi-valued discrete
-origin: multi-valued discrete
-car name: string (unique for each instance)

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_auto_dataset = pd.read_csv("C:/Users/Hima/auto_data.csv")

print(df_auto_dataset.head())

def origin(num):
    if num == 1:
        return 'USA'
    elif num == 2:
        return 'EUR'
    else:
        return 'Asia'

df_auto_dataset['origin'] = df_auto_dataset['origin'].apply(origin)

print(df_auto_dataset.head(30))

sns.pairplot(df_auto_dataset[['mpg','weight','origin']],hue='origin',height=4)
plt.show()

