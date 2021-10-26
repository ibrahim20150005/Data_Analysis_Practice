"""
Analyse GDP of Countries
DESCRIPTION

Problem Statement: Evaluate the dataset containing the GDPs of different countries to:

Find and print the name of the country with the highest GDP
Find and print the name of the country with the lowest GDP
Print out text and input values iteratively
Print out the entire list of the countries with their GDPs
Print the highest GDP value, lowest GDP value, mean GDP value, standardized GDP value, and the sum of all the GDPs
"""
from datetime import date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


countries=np.array(['Algeria','Angola','Argentina','Australia','Austria','Bahamas','Bangladesh','Belarus','Belgium','Bhutan','Brazil','Bulgaria','Cambodia','Cameroon','Chile','China','Colombia','Cyprus','Denmark','El Salvador','Estonia','Ethiopia','Fiji','Finland','France','Georgia','Ghana','Grenada','Guinea','Haiti','Honduras','Hungary','India','Indonesia','Ireland','Italy','Japan','Kenya', 'South Korea','Liberia','Malaysia','Mexico', 'Morocco','Nepal','New Zealand','Norway','Pakistan', 'Peru','Qatar','Russia','Singapore','South Africa','Spain','Sweden','Switzerland','Thailand', 'United Arab Emirates','United Kingdom','United States','Uruguay','Venezuela','Vietnam','Zimbabwe'])
GDP_values_for_each_country = np.array([2255.225482,629.9553062,11601.63022,25306.82494,27266.40335,19466.99052,588.3691778,2890.345675,24733.62696,1445.760002,4803.398244,2618.876037,590.4521124,665.7982328,7122.938458,2639.54156,3362.4656,15378.16704,30860.12808,2579.115607,6525.541272,229.6769525,2242.689259,27570.4852,23016.84778,1334.646773,402.6953275,6047.200797,394.1156638,385.5793827,1414.072488,5745.981529,837.7464011,1206.991065,27715.52837,18937.24998,39578.07441,478.2194906,16684.21278,279.2204061,5345.213415,6288.25324,1908.304416,274.8728621,14646.42094,40034.85063,672.1547506,3359.517402,36152.66676,3054.727742,33529.83052,3825.093781,15428.32098,33630.24604,39170.41371,2699.123242,21058.43643,28272.40661,37691.02733,9581.05659,5671.912202,757.4009286,347.7456605])

#Find and print the name of the country with the highest GDP
Highest_GDP = countries[GDP_values_for_each_country.argmax()] 
print("the highest GDP is ",GDP_values_for_each_country.max(),"with country is ",Highest_GDP)

#Find and print the name of the country with the lowest GDP
Lowest_GDP = countries[GDP_values_for_each_country.argmin()] 
print("the lowest GDP is ",GDP_values_for_each_country.min(),"with country is ",Lowest_GDP)

#Print out text and input values iteratively
for country in countries:
    print(format(country))

#Print out the entire list of the countries with their GDPs
for i in range(len(countries)):
    country = countries[i]
    country_GDP = GDP_values_for_each_country[i]
    print("the country is: ",country,"and the GDP is:",country_GDP)

#Print the highest GDP value, lowest GDP value, mean GDP value, standardized GDP value, and the sum of all the GDPs
print("the highest GDP value",GDP_values_for_each_country.max())
print("the lowest GDP value",GDP_values_for_each_country.min())
print("the mean GDP value",GDP_values_for_each_country.mean())
print("standardized GDP value",GDP_values_for_each_country.std())
print("the sum of all the GDPs",GDP_values_for_each_country.sum())
