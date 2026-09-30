import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('heart.csv')

'''------------EDA------------------'''
#print(df.describe())
#print(df.info())
#print(df.columns)
#print(df.duplicated().sum())
df['HeartDisease'].value_counts().plot(kind = "bar")
'''plt.title("Heart Disease Distribution")
plt.xlabel("Heart Disease")
plt.ylabel("Count")'''
'''def plotting(var,num):
    plt.subplot(2,2,num)
    sns.histplot(df[var],kde = True)

plotting('Age',1)
plotting('RestingBP',2)
plotting('Cholesterol',3)
plotting('MaxHR',4)


plt.tight_layout()
'''
#plt.show()
'''ch_mean = df.loc[df['Cholesterol'] != 0,'Cholesterol'].mean()
df['Cholesterol'] = df['Cholesterol'].replace(0,ch_mean)
df['Cholesterol'] = df['Cholesterol'].round(2)
resting_bp_mean = df.loc[df['RestingBP'] != 0, 'RestingBP'].mean()

df['RestingBP'] = df['RestingBP'].replace(0, resting_bp_mean)

df['RestingBP'] = df['RestingBP'].round(2)
def plotting(var,num):
    plt.subplot(2,2,num)
    sns.histplot(df[var],kde = True)

plotting('Age',1)
plotting('RestingBP',2)
plotting('Cholesterol',3)
plotting('MaxHR',4)


plt.tight_layout()
pip install sheryanalysis==0.1.0   to do in terminal t o sheriyans that  makes anayalse work easier
import sheryanalysis as sh  
sh.analyze(df)
sns.countplot(x = df['Sex'],hue = df['HeartDisease'])
sns.countplot(x = df['ChestPainType'],hue = df['HeartDisease'])
sns.countplot(x = df['FastingBS'],hue = df['HeartDisease'])
sns.boxplot(x = 'HeartDisease', y = 'Cholesterol',data = df)
sns.violinplot(x='HeartDisease', y='Age', data=df)
sns.heatmap(df.corr(numeric_only=True), annot=True)
'''
