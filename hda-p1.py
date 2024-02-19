import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

covid_studies = pd.read_csv("C:\\Users\\terra\\OneDrive\\Desktop\\hda-p1\\covid.csv")
breast_cancer_studies = pd.read_csv("C:\\Users\\terra\\OneDrive\\Desktop\\hda-p1\\breast.csv")

covid_studies['Study Type'] = 'COVID'
breast_cancer_studies['Study Type'] = 'Breast Cancer'

combined_studies = pd.concat([covid_studies, breast_cancer_studies], ignore_index=True)

plt.figure(figsize=(10, 6))
order = ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]
sns.countplot(x='Phases', hue='Study Type', data=combined_studies, order=order)
plt.title('Comparison of Study Phases between COVID and Breast Cancer Studies')
plt.xlabel('Phase of Study')
plt.ylabel('Count')
plt.show()

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
