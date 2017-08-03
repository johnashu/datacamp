
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = 'all_medalists.csv'
medals = pd.read_csv(filename)

USA_edition_grouped = medals.loc[medals.NOC == 'USA'].groupby('Edition')

print(USA_edition_grouped['Medal'].count())

country_names = medals['NOC']
medal_counts = country_names.value_counts()
print(medal_counts.head(15))


counted = medals.pivot_table(aggfunc='count', index='NOC', values='Athlete', columns='Medal')
counted['totals'] = counted.sum(axis='columns')
counted = counted.sort_values('totals', ascending=False)

print(counted.head(15))

ev_gen = medals[['Event_gender', 'Gender']]
ev_gen_uniques = ev_gen.drop_duplicates()
print(ev_gen_uniques)

medals_by_gender = medals.groupby(['Event_gender', 'Gender'])
medal_count_by_gender = medals_by_gender.count()
print(medal_count_by_gender)

sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')
suspect = medals[sus]
print(suspect)

country_grouped = medals.groupby('NOC')
Nsports = country_grouped['Sport'].nunique()
Nsports = Nsports.sort_values(ascending=False)
print(Nsports.head(15))


during_cold_war = (medals['Edition'] >= 1952) & (medals['Edition'] <= 1988)
is_usa_urs = medals.NOC.isin(['USA', 'URS'])
cold_war_medals = medals.loc[during_cold_war & is_usa_urs]
country_grouped = cold_war_medals.groupby('NOC')
Nsports = country_grouped['Sport'].nunique()
print(Nsports)

medals_won_by_country = medals.pivot_table(index='Edition', columns='NOC', values='Athlete', aggfunc='count')
cold_war_usa_usr_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]
most_medals = cold_war_usa_usr_medals.idxmax(axis='columns')
print(most_medals.value_counts())


usa = medals.NOC == 'USA'
usa_medals_by_year = medals.groupby(['Edition', 'Medal'])
usa_medals_by_year.plot()
plt.show()