

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





dataset=pd.read_csv("C:/Users/computer/Desktop/WorldCupMatches.csv")





dataset.head()





dataset.head(20)





dataset.tail(8)





dataset.shape



dataset.describe()




dataset.info()





dataset.columns





dataset.dtypes





#slice the result for first 5 rows
print (dataset[0:5]['City'])





#reading specific columns
print (dataset.loc[:,['Stadium','City']])





dataset.loc[0:5,['Stadium','City']]





#reading specific columns and rows
print (dataset.loc[[1,2,7],['Stadium','City']])




#showing all null values
dataset.isnull()




dataset.isnull().values.any()



dataset.isnull().sum()




print(dataset['Attendance'].isnull())





#filling missing value using fillna()
dataset.fillna(99,inplace=True)
print(dataset)





dataset.isnull().sum()





dataset.isnull().values.any()



#select rows in dataset where the column attendance is null
df_null = dataset.loc[dataset['Attendance'].isnull()]
print (df_null)





#drop rows with missing values
dataset.dropna(inplace=True)
dataset.shape







