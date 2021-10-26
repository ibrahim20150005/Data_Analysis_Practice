import numpy as np

country = np.array(['Great Britain', 'China', 'Russia',
                   'United States', 'Korea', 'Japan', 'Germany'])

Country_Code = np.array(['GBR', 'CHN', 'RUS', 'US', 'KOR', 'JPN', 'GER'])

Year = np.array([2012, 2012,2012,2012,2012,2012,2012])

Medal_Tally = np.array(['Gold','Silver','Bronze'])

Medal_Tally_Gold = np.array([29,38,24,46,13,7,11])

Medal_Tally_Silver = np.array([17,28,25,28,8,14,11])

Medal_Tally_Bronze = np.array([19,22,32,29,7,17,14])

'''
Problem: 

Evaluate the dataset of the Summer Olympics, London 2012 to:
'''
#Find and print the name of the country that won maximum gold medals,
country_maximum_gold_medals = country[Medal_Tally_Gold.argmax()]
print("the name of the country that won maximum gold medals is: ",country_maximum_gold_medals)

#Find and print the countries who won more than 20 gold medals,
countries_maximum_20_gold_medals = Country_Code[Medal_Tally_Gold>20]
print("the countries who won more than 20 gold medals are: ",countries_maximum_20_gold_medals)

#Print the medal tally,
print('the medal tally of Gold: ',Medal_Tally_Gold.sum(),' ,of Silver: ',Medal_Tally_Silver.sum(),' ,of Bronze: ',Medal_Tally_Bronze.sum())

#Print each country name with the corresponding number of gold medals
for i in range(len(country)):
    print('the country of ',country[i],' is won ',Medal_Tally_Gold[i],' of gold medals')

#Print each country's name with the total number of medals won.
for i in range(len(country)):
    print('the country of ',country[i],' is won ',Medal_Tally_Gold[i]+Medal_Tally_Silver[i]+Medal_Tally_Bronze[i],' of  medals')

print(Medal_Tally_Bronze.transpose())