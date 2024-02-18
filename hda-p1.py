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
