import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

covid_studies = pd.read_csv("covid.csv")
breast_cancer_studies = pd.read_csv("breast.csv")

covid_studies['Study Type'] = 'COVID'
breast_cancer_studies['Study Type'] = 'Breast Cancer'

combined_studies = pd.concat([covid_studies, breast_cancer_studies], ignore_index=True)

"""
plt.figure(figsize=(10, 6))
order = ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]
sns.countplot(x='Phases', hue='Study Type', data=combined_studies, order=order)
plt.title('Comparison of Study Phases between COVID and Breast Cancer Studies')
plt.xlabel('Phase of Study')
plt.ylabel('Count')
plt.show()
"""

'''
Trevor:
I have this commented out in case you dont want it to mess with your stuff. Just a few countplots to help visualize the data and then,
I added some pie charts that we could change to fit any categorical variable as long as you print out the "gbA" for any given attribute and change the agbl acordingly,
Finaly, on my own csv file i created a grouping mechanism for the enrollment becaue there are so many differnt values. thats what the "EG" is.
Idk how to get my coppies of the csv to yall but if we meet up sometime I can show it. Its not alot but I don't think we need much for the first email doc anyway.
'''

'''
sns.countplot(x = 'Age', hue = 'Study Type', data=combined_studies)
plt.show()

sns.countplot(x = 'Funder Type', hue = 'Study Type', data=combined_studies)
plt.show()

sns.countplot(x = 'EG', hue = 'Study Type', data=combined_studies)
plt.show()

sns.countplot(x = 'Status', hue = 'Study Type', data=combined_studies)
plt.show()
'''
'''
gbA = combined_studies.groupby('Age').apply(len)
agbl = ['Adult', 'Adult and Older-Adult', 'Child', 'Child and Adult', 'All', 'Older-Adult']
plt.pie(gbA , labels = agbl, autopct='%1.1f%%', shadow=False, startangle=140)
plt.show()

gbA2 = covid_studies.groupby('Age').apply(len)
agbl = ['Adult', 'Adult and Older-Adult', 'Child', 'Child and Adult', 'All', 'Older-Adult']
plt.pie(gbA2 , labels = agbl, autopct='%1.1f%%', shadow=False, startangle=140)
plt.show()

gbA3 = breast_cancer_studies.groupby('Age').apply(len)
agbl = ['Adult', 'Adult and Older-Adult', 'Child and Adult', 'All', 'Older-Adult']
plt.pie(gbA3 , labels = agbl, autopct='%1.1f%%', shadow=False, startangle=140)
plt.show()
'''
'''
This monstrosity is a roundabout way to get the top 10 most frequent drugs from the dataset. 
All of the frequencies are stored in the drugFrequencies dictionary and I pulled out the top 10 in top10.
'''
'''
covid_copy = covid_studies.copy(deep = True)

intTotal = []
for index, row in covid_copy.loc[:, ['Interventions']].iterrows():
    x = covid_copy['Interventions'].loc[index].split('|')
    intTotal = intTotal + x

keyword = ['DRUG:']
drugList=[]
for i in keyword:
    for j in intTotal:
        if(j.find(i)!=-1):
            drugList.append(j)

from itertools import groupby

drugFrequencies = {value: len(list(freq)) for value, freq in groupby(sorted(drugList))}

from collections import Counter

n = 10
counter = Counter(drugFrequencies)
top10 = dict(counter.most_common(n))
print(top10)
'''

#Enrollment by funder type
"""
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Funder Type', y='Enrollment', hue='Study Type', data=combined_studies)
plt.title('Enrollment by Funder Type')
plt.xlabel('Funder Type')
plt.ylabel('Enrollment')
plt.legend(title='Study Type')
plt.show()
"""

"""
#Enrollment of studies at each phase
order = ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]
combined_studies_sorted = combined_studies.sort_values(by='Phases', key=lambda x: x.map({phase: i for i, phase in enumerate(order)}))
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Phases', y='Enrollment', hue='Study Type', data=combined_studies_sorted)
plt.title('Enrollment by Study Phase')
plt.xlabel('Study Phase')
plt.ylabel('Enrollment')
plt.legend(title='Study Type')
plt.show()
"""

"""
#Graph of status by current phase
combined_studies['Start Date'] = pd.to_datetime(combined_studies['Start Date'], errors='coerce')
combined_studies['Completion Date'] = pd.to_datetime(combined_studies['Completion Date'], errors='coerce')
combined_studies['Duration'] = (combined_studies['Completion Date'] - combined_studies['Start Date']).dt.days
plt.figure(figsize=(14, 8))
sns.countplot(x='Phases', hue='Status', data=combined_studies, order=["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"])
plt.title('Distribution of Status within Each Phase')
plt.xlabel('Phases')
plt.ylabel('Count')
plt.legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
"""

#Status by duration - currently broken
"""
combined_studies = combined_studies.dropna(subset=['Start Date', 'Completion Date'])
print("Unique values in 'Start Date':", combined_studies['Start Date'].unique())
print("Unique values in 'Completion Date':", combined_studies['Completion Date'].unique())
# Calculate the duration in days
combined_studies['Duration'] = (combined_studies['Completion Date'] - combined_studies['Start Date']).dt.days

# Create a boxplot to show the distribution of duration for each status
plt.figure(figsize=(12, 8))
sns.boxplot(x='Status', y='Duration', data=combined_studies)
plt.title('Distribution of Duration for Each Status')
plt.xlabel('Status')
plt.ylabel('Duration (days)')
plt.show()
"""




"""
#Ranking of diseases - managed to combine all breast cancer variants into one, no luck
#with COVID. (Part C/2)
combined_studies['Study Type'] = combined_studies['Study Type'].replace({'COVID-19': 'COVID', 'Covid19': 'COVID'})
combined_studies.loc[combined_studies['Conditions'].str.contains('Breast Cancer', case=False, na=False), 'Conditions'] = 'Breast Cancer'
combined_studies['Conditions_List'] = combined_studies['Conditions'].str.split('|')
exploded_studies = combined_studies.explode('Conditions_List')
condition_counts = exploded_studies['Conditions_List'].value_counts()
top_conditions = condition_counts.head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x=top_conditions.values, y=top_conditions.index, palette='viridis')
plt.title('Top 10 Most Common Conditions in Clinical Trials')
plt.xlabel('Number of Trials')
plt.ylabel('Condition')
plt.show()
"""
"""
#Number of trials by 2 month period (Part C/3)
#Not exactly sure why the x-axis is labeled like so
combined_studies['Start Date'] = pd.to_datetime(combined_studies['Start Date'], errors='coerce')
combined_studies['Period'] = combined_studies['Start Date'].dt.to_period('2M')
covid_data = combined_studies[combined_studies['Study Type'] == 'COVID']
breast_cancer_data = combined_studies[combined_studies['Study Type'] == 'Breast Cancer']
covid_counts = covid_data['Period'].value_counts().sort_index()
breast_cancer_counts = breast_cancer_data['Period'].value_counts().sort_index()
plt.figure(figsize=(12, 8))
sns.lineplot(x=covid_counts.index.astype(str), y=covid_counts.values, label='COVID')
sns.lineplot(x=breast_cancer_counts.index.astype(str), y=breast_cancer_counts.values, label='Breast Cancer')
plt.title('Number of Trials for COVID and Breast Cancer, Bimonthly')
plt.xlabel('Period')
plt.ylabel('Number of Trials')
plt.xticks(rotation=90, ha='right')
plt.legend()
plt.show()
"""
