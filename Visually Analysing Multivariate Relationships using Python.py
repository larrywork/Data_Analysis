#importing libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
#loading the dataset
df=pd.read_csv("Churn_Modelling.csv")

#viewing a snapshot of the dataset
df.head()

print(df.shape) #Getting the number of rows and columns of the dataframe using the "shape command"

#plotting scatter plot between age and salary
sns.relplot(x=df['Age'], y=df['EstimatedSalary'], height=6, aspect=2/1, hue=df["Age"]);


#Creating age brackets
bins = [20, 30, 40, 50, 60, 70, 80, 90,100]
df['Age_Brackets']=pd.cut(df['Age'], bins)
df_age_salary = df.groupby('Age_Brackets',as_index=False)[('EstimatedSalary')].mean()

#Plotting Mean Salary across age
sns.catplot(x='Age_Brackets', y='EstimatedSalary', data=df_age_salary,kind='bar',palette='GnBu',height=4,aspect=2)
plt.title('Mean Salary across Age Brackets')
plt.show()

df_bal_gender_geo=  df.groupby(['Gender','Geography'],as_index=False)[('Balance')].mean()
p=sns.catplot(x='Geography', y='Balance', hue='Gender', 
            data=df_bal_gender_geo,kind='bar',palette='bright',height=4, aspect=1.5)


#Plotting stacked baar chart to represent the distribution of males and females across gender
f = plt.figure(figsize=(8,5))
ax = f.add_subplot(1,1,1)

sns.histplot(data=df, ax=ax, stat="count", multiple="stack",
             x="Tenure", kde=False,
             palette="pastel", hue="Gender",
             element="bars", legend=True)
ax.set(ylim=(0, 1400))
ax.set_title("Distribution of males and females across Tenure")
ax.set_xlabel("Tenure")
ax.set_ylabel("Count")


#Plotting line chart to visualize the distribution of people across age and country
df_geo_age = df.groupby(['Age','Geography'],as_index=False).count()

plt.figure(figsize=(10,7))
plt.ylabel('Count')
sns.lineplot(x = "Age", y = "RowNumber",hue="Geography",data=df_geo_age)


# Let us now checkout the number of people across Age, Geography, Gender that have a Credit Card
df_geo_credit_gender = df.groupby(['Geography','HasCrCard','Gender'],as_index=False).count()

grid_plot_credit=sns.catplot(x='Geography', y='RowNumber', hue='Gender',col='HasCrCard', 
               data=df_geo_credit_gender,kind='bar',palette='bright',height=6, aspect=0.7)
plt.legend(loc='upper right')
plt.ylabel('Count')

#Creating dataframe to plot the combo chart
df_tenure_people_count =  df.groupby(['Tenure'],as_index=False).count()
df_tenure_people_count= df_tenure_people_count[['Tenure','RowNumber']]
df_tenure_people_count.columns = ['Tenure','Counts']
df_tenure_salary_mean = df.groupby(['Tenure'],as_index=False)[('EstimatedSalary')].mean()
df_tenure_salary_mean.columns = ['Tenure','Mean_Salary']
merged_table = pd.merge(df_tenure_people_count,df_tenure_salary_mean,on='Tenure')


#Create combo chart
fig, ax1 = plt.subplots(figsize=(10,6))
color = 'tab:green'
#bar plot creation
ax1.set_title('People count and estimated salary across Tenure', fontsize=16)
ax1.set_ylabel('People Counts', fontsize=16)
ax1 = sns.barplot(x='Tenure', y='Counts', data = merged_table, palette='summer')
ax1.tick_params(axis='y')
#specify we want to share the same x-axis
ax2 = ax1.twinx()
color = 'tab:red'
#line plot creation
ax2.set_ylabel('Mean Estimated Salary', fontsize=16)
ax2 = sns.lineplot(x='Tenure', y='Mean_Salary', data = merged_table, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
#show plot
ax1.legend(["People Counts"], loc="upper left")
ax2.legend(["Estimated Salary"])
ax1.set(ylim=(0, 1500))
ax2.set(ylim=(90000, 120000))
plt.show()
