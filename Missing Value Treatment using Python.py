#importing libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.impute import KNNImputer

#loading the dataset
df=pd.read_csv("recipeData.csv", sep=',', engine='python')

#Printing the dataset
df.head()

#Printing shape of the dataset
df.shape

#Printing basic info about the dataset
df.info()

#Printing Column names that contain Null Values
df.columns[df.isna().any()].tolist()


#Printing Null Values in Columns
df_nulls=df.isnull().sum().to_frame()
df_nulls.columns= ['Null_Values']
df_nulls[df_nulls['Null_Values']!=0]

#Printing Percentage distribuition of Null Values
df_nulls['Percentage_distribuition'] = (df_nulls['Null_Values']/df.shape[0])*100
df_nulls[df_nulls['Null_Values']!=0]

#Deleting rows that contain Null Values
print("Shape before row cleaning: " + str(df.shape))
df_rows_cleaned= df.dropna(axis=0, subset=['Name','Style','BoilGravity' ])
print("Shape after row cleaning: " + str(df_rows_cleaned.shape))


#Deleting Columns that contain Null Values
print("Shape before column cleaning: " + str(df_rows_cleaned.shape))
df_row_col_cleaned = df_rows_cleaned.drop(['PrimingMethod','PrimingAmount', 'UserId'], axis = 1) 
print("Shape after column cleaning: " + str(df_row_col_cleaned.shape))

#Imputing Null values in the MashThickness column using Mean
print("Null Values in MashThickness before imputation :" + str(df_row_col_cleaned[['MashThickness']].isnull().sum()[0]))
df_row_col_cleaned['MashThickness'].fillna(df_row_col_cleaned['MashThickness'].mean(), inplace = True)
print("Null Values in MashThickness before imputation :" + str(df_row_col_cleaned[['MashThickness']].isnull().sum()[0]))

#Imputing Null values in the PitchRate column using mode
print("Null Values in PitchRate before imputation :" + str(df_row_col_cleaned[['PitchRate']].isnull().sum()[0]))
df_row_col_cleaned['PitchRate'].fillna(df_row_col_cleaned['PitchRate'].mode, inplace = True)
print("Null Values in PitchRate before imputation :" + str(df_row_col_cleaned[['PitchRate']].isnull().sum()[0]))


#Imputing Null values in the PrimaryTemp column using KNN Imputer
print("Null Values in PrimaryTemp before imputation :" + str(df_row_col_cleaned[['PrimaryTemp']].isnull().sum()[0]))

#Selecting only numerical columns so that the KNNImputer function works
df_numeric= df_row_col_cleaned[['BeerID','StyleID', 'Size(L)','OG','FG','ABV','IBU','Color','BoilSize','BoilTime', 'BoilGravity','Efficiency','MashThickness','PrimaryTemp']]
imputer = KNNImputer(n_neighbors=3)
imputed = imputer.fit_transform(df_numeric)
df_imputed = pd.DataFrame(imputed, columns=df_numeric.columns)

print("Null Values in PrimaryTemp after imputation :" + str(df_imputed[['PrimaryTemp']].isnull().sum()[0]))


