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

#Status of studies in each phase
combined_studies['Start Date'] = pd.to_datetime(combined_studies['Start Date'], errors='coerce')
combined_studies['Completion Date'] = pd.to_datetime(combined_studies['Completion Date'], errors='coerce')
combined_studies['Duration'] = (combined_studies['Completion Date'] - combined_studies['Start Date']).dt.days
combined_studies = combined_studies[combined_studies['Duration'] >= 0]
order = ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]
combined_studies['Phases'] = pd.Categorical(combined_studies['Phases'], categories=order, ordered=True)
covid_studies = combined_studies[combined_studies['Study Type'] == 'COVID']
breast_cancer_studies = combined_studies[combined_studies['Study Type'] == 'Breast Cancer']
#Had to add this bc it was putting the colors in the same order but not the statuses
status_order = ['COMPLETED', 'RECRUITING', 'TERMINATED', 'ACTIVE_NOT_RECRUITING', 'UNKNOWN', 'WITHDRAWN',
                'NOT_YET_RECRUITING', 'ENROLLING_BY_INVITATION', 'SUSPENDED']
#Had to add this because it was confusing looking at different legends
status_colors = {
    'COMPLETED': 'darkblue',
    'RECRUITING': 'darkgreen',
    'TERMINATED': 'darkred',
    'ACTIVE_NOT_RECRUITING': 'darkorange',
    'UNKNOWN': 'purple',
    'WITHDRAWN': 'brown',
    'NOT_YET_RECRUITING': 'darkcyan',
    'ENROLLING_BY_INVITATION': 'darkmagenta',
    'SUSPENDED': 'black'
}
custom_palette = [sns.set_hls_values(color, l=0.5) for color in status_colors.values()]

#COVID
plt.figure(figsize=(14, 8))
sns.countplot(x='Phases', hue='Status', data=covid_studies, order=order, palette=custom_palette, hue_order=status_order)
plt.title('Status within Each Phase - COVID')
plt.xlabel('Phases')
plt.ylabel('Count')
plt.legend(title='Status', bbox_to_anchor=(0.75, 1), loc='upper left')
plt.show()

#Breast Cancer
plt.figure(figsize=(14, 8))
sns.countplot(x='Phases', hue='Status', data=breast_cancer_studies, order=order, palette=custom_palette, hue_order=status_order)
plt.title('Status within Each Phase - Breast Cancer')
plt.xlabel('Phases')
plt.ylabel('Count')
plt.legend(title='Status', bbox_to_anchor=(0.75, 1), loc='upper left')
plt.show()

"""
#Duration of each study by phase
combined_studies['Start Date'] = pd.to_datetime(combined_studies['Start Date'], errors='coerce')
combined_studies['Completion Date'] = pd.to_datetime(combined_studies['Completion Date'], errors='coerce')
combined_studies['Duration'] = (combined_studies['Completion Date'] - combined_studies['Start Date']).dt.days
combined_studies = combined_studies[combined_studies['Duration'] >= 0]
order = ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]
combined_studies['Phases'] = pd.Categorical(combined_studies['Phases'], categories=order, ordered=True)
covid_studies = combined_studies[combined_studies['Study Type'] == 'COVID']
breast_cancer_studies = combined_studies[combined_studies['Study Type'] == 'Breast Cancer']

#COVID
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Phases', y='Duration', data=covid_studies, hue='Study Type')
plt.title('Duration vs. Phase of COVID Studies')
plt.xlabel('Phase of Study')
plt.ylabel('Duration (Days)')
plt.legend(title='Study Type')
plt.show()

#Breast Cancer
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Phases', y='Duration', data=breast_cancer_studies, hue='Study Type')
plt.title('Duration vs. Phase of Breast Cancer Studies')
plt.xlabel('Phase of Study')
plt.ylabel('Duration (Days)')
plt.legend(title='Study Type')
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
combined_studies['Start Date'] = pd.to_datetime(combined_studies['Start Date'], errors='coerce')combined_studies['Period'] = combined_studies['Start Date'].dt.to_period('M').dt.to_timestamp() + pd.offsets.MonthBegin(1)
combined_studies['Period'] = (combined_studies['Period'].dt.year.astype(str) + '-' +
                              ((combined_studies['Period'].dt.month - 1) // 3 + 1).astype(str))
covid_data = combined_studies[combined_studies['Study Type'] == 'COVID']
breast_cancer_data = combined_studies[combined_studies['Study Type'] == 'Breast Cancer']
covid_counts = covid_data.groupby('Period').size().reset_index(name='Count')
breast_cancer_counts = breast_cancer_data.groupby('Period').size().reset_index(name='Count')
covid_counts['Count'] = covid_counts['Count'].astype(int)
breast_cancer_counts['Count'] = breast_cancer_counts['Count'].astype(int)
covid_counts = covid_counts[covid_counts['Period'] != 'nan-nan']
breast_cancer_counts = breast_cancer_counts[breast_cancer_counts['Period'] != 'nan-nan']
plt.figure(figsize=(12, 8))
sns.lineplot(x=covid_counts['Period'], y=covid_counts['Count'], label='COVID')
sns.lineplot(x=breast_cancer_counts['Period'], y=breast_cancer_counts['Count'], label='Breast Cancer')
plt.title('Number of Trials for COVID and Breast Cancer, Trimonthly')
plt.xlabel('Period')
plt.ylabel('Number of Trials')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.show()
"""
