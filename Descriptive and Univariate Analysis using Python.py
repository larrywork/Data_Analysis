#importing libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
df=pd.read_csv("bestsellers with categories.csv")

#viewing a snapshot of the dataset
df.head()

print(df.shape) #Getting the number of rows and columns of the dataframe using the "shape command"

df.info()#Getting information about null values and data types using the "info command"

#Getting basic statstics such as mean, quantiles,min, max etc. about numeric columns and data types using the "describe" command
df.describe()

#Another way to calculate the mean and median of the numeric columns is the following
print("User Rating Mean: " + str(df["User Rating"].mean()))
print("User Rating Median: " +  str( df["User Rating"].median()))
print("Reviews Mean: " +str(df["Reviews"].mean()))
print("Reviews Median: " + str(df["Reviews"].median()))
print("Price Mean: " +str(df["Price"].mean()))
print("Price Median: " +str(df["Price"].median()))

df["Genre"].mode()

#Getting Percentage distribuition of "Genre" across the dataset
df_counts= df.groupby(['Genre'])['Name'].agg('count').reset_index(name="Count_of_books")
fig1, ax1 = plt.subplots()
ax1.pie(df_counts['Count_of_books'],labels=df_counts['Genre'],colors =["pink","blue"], explode= (0,0.05),autopct = '%1.1f%%')
ax1.set_title('Percentage of books across Genre',fontsize = 12)


#Getting Percentage distribuition of Books across years
df_counts_year= df.groupby(['Year'])['Name'].agg('count').reset_index(name="Count_of_books")
fig1, ax1 = plt.subplots()
ax1.pie(df_counts_year['Count_of_books'],labels=df_counts_year['Year'],autopct = '%1.1f%%')
ax1.set_title('Percentage of books across Years',fontsize = 12)

fig, ax =plt.subplots(1,3, figsize=(18, 7))
sns.histplot(df['User Rating'], kde = True, color ='red', bins = 30, ax=ax[0]) 
sns.histplot(df['Reviews'], kde = True, color ='red', bins = 30, ax=ax[1]) 
sns.histplot(df['Price'], kde = True, color ='red', bins = 30, ax=ax[2]) 
fig.show()



#Creating Box-plots for numeric columns
plt.figure(figsize=(18,5))
plt.subplot(1,3,1)
sns.boxplot( y=df["User Rating"] );
plt.subplot(1,3,2)
sns.boxplot( y=df["Reviews"] );
plt.subplot(1,3,3)
sns.boxplot( y=df["Price"] );


#Creating violin-plots for numeric columns
plt.figure(figsize=(18,5))
plt.subplot(1,3,1)
sns.violinplot( y=df["User Rating"] );
plt.subplot(1,3,2)
sns.violinplot( y=df["Reviews"] );
plt.subplot(1,3,3)
sns.violinplot( y=df["Price"] );



