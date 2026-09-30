import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import  seaborn as sns
import warnings            
warnings.filterwarnings('ignore')

df = pd.read_csv('heart.csv')

'''
df_encode = pd.get_dummies(df,drop_first=True)
df_encode = df_encode.astype(int)
from sklearn.preprocessing import StandardScaler
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
scaler = StandardScaler()
df_encode[numerical_cols] = scaler.fit_transform(df_encode[numerical_cols])
df_encode.head()'''