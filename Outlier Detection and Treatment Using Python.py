#importing libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#loading the dataset
df=pd.read_csv("all_seasons.csv")

#viewing a snapshot of the dataset
df.head()

print(df.shape) #Getting the number of rows and columns of the dataframe using the "shape command"

df.info()#Getting information about null values and data types using the "info command"

#Creating Box-plots for numeric columns to visually identify outliers
plt.figure(figsize=(18,5))
plt.subplot(1,3,1)
sns.boxplot( y=df["age"] );
plt.subplot(1,3,2)
sns.boxplot( y=df["player_height"] );
plt.subplot(1,3,3)
sns.boxplot( y=df["player_weight"] );

#Creating distribution-plots to bettwr understand the spread of the numeric columns
fig, ax =plt.subplots(1,3, figsize=(18, 7))
sns.histplot(df['age'], kde = True, color ='red', bins = 50, ax=ax[0]) 
sns.histplot(df['player_height'], kde = True, color ='red', bins = 50, ax=ax[1]) 
sns.histplot(df['player_weight'], kde = True, color ='red', bins = 50, ax=ax[2]) 
fig.show()

#Identifying the upper limit for age using IQR  
IQR = df.age.quantile(0.75) - df.age.quantile(0.25)
upper_limit = df.age.quantile(0.75) + (IQR * 1.5)
upper_limit

#Printing total number of outliers for the age feature 
total = np.float(df.shape[0])
print('Total Players: {}'.format(df.age.shape[0]))
print('Players aged more than 39 years: {}'.format(df[df.age>39].shape[0]))
print('Percentage of players aged more than 39 years: {}'.format(df[df.age>39].shape[0]*100/total))

#Deleting the players that are aged more than the upper limit
df_ageremoved= df[df['age']<39]
df_ageremoved
sns.boxplot( y=df_ageremoved["age"] );


#Identifying upper and lower limit for height
IQR = df.player_height.quantile(0.75) - df.player_height.quantile(0.25)
upper_limit = df.player_height.quantile(0.75) + (IQR * 1.5)
lower_limit = df.player_height.quantile(0.25) - (IQR * 1.5)

print("Upper height limit:"+ str(upper_limit ))
print("Lower height limit:"+ str(lower_limit ))


#Let us cap these outliers at the upper and lower limits and print the box-plot after outlier treatment
df['Height_treated'] = np.where(df['player_height']> 217.28 , 217.28 , df['player_height'])
df['Height_treated'] = np.where(df['Height_treated']< 186.58 , 186.58, df['Height_treated'])
sns.boxplot( y=df["Height_treated"] );


#Identifying upper and lower limit for weight
IQR = df.player_weight.quantile(0.75) - df.player_weight.quantile(0.25)
upper_limit = df.player_weight.quantile(0.75) + (IQR * 1.5)
lower_limit = df.player_weight.quantile(0.25) - (IQR * 1.5)

print("Upper weight limit:"+ str(upper_limit ))
print("Lower weight limit:"+ str(lower_limit ))


#Let us impute these outliers using the mean and print the box-plot after outlier treatment
df['Weight_treated'] = np.where(df['player_weight']> 137.21 ,  df['player_weight'].mean(), df['player_weight'])
df['Weight_treated'] = np.where(df['Weight_treated']< 62.82 ,  df['player_weight'].mean(), df['Weight_treated'])
sns.boxplot( y=df["Weight_treated"] );