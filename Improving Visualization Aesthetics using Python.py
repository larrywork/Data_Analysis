#STEP 1
#importing libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
import matplotlib.ticker as ticker

#loading the dataset
df=pd.read_csv("Sales Data.csv")

#viewing a snapshot of the dataset
df.head()


#Step 2
#Data wrangling to create the dataset for the graph
df_orders_date= df.groupby('Order Date',as_index=False).agg({'Order ID': ['nunique']})
df_orders_date.columns= ['Order_Date','Total_Orders']
df_orders_date['Order_Date_f']=  pd.to_datetime(df_orders_date['Order_Date'], format='%d/%m/%Y')
df_orders_date['Year'] = pd.DatetimeIndex(df_orders_date['Order_Date_f']).year
df_orders_date['Month']= pd.DatetimeIndex(df_orders_date['Order_Date_f']).month
df_orders_date['Year_month'] = df_orders_date['Order_Date_f'].apply(lambda x: x.strftime('%Y-%b')) 


df_final_ts= df_orders_date.groupby(['Year','Month','Year_month'],as_index=False).agg({'Total_Orders': ['sum']})

df_final_ts.columns= ['Year','Month','Year_month','Total_Orders']
df_final_ts.head()

#Step 3
#Creating Base Plot
sns.lineplot(x = "Year_month", y = "Total_Orders",data=df_final_ts)


#Step 4
#Increasing chart siez, improving x-axis ticks alignment
plt.figure(figsize=(20,7))
g=sns.lineplot(x = "Year_month", y = "Total_Orders",data=df_final_ts)
plt.setp(g.get_xticklabels(), rotation=45)
new_ticks = [i.get_text() for i in g.get_xticklabels()]
plt.xticks(range(0, len(df_final_ts['Year_month']), 5), df_final_ts['Year_month'][::5])
plt.show()


#Step 5
#Adding axis-titles, graph title, increasing font size, reducing x-axis tick frequency
plt.figure(figsize=(20,7))
g=sns.lineplot(x = "Year_month", y = "Total_Orders",data=df_final_ts)
plt.setp(g.get_xticklabels(), rotation=45)
plt.xlabel('Year Month', size=20)
plt.ylabel('Total Orders', size=20)
plt.title("Total orders placed across years (2015-2018)", size = 20)
new_ticks = [i.get_text() for i in g.get_xticklabels()]
plt.xticks(range(0, len(df_final_ts['Year_month']), 5), df_final_ts['Year_month'][::5])
plt.show()


#Step 6
#Changing line colour, increasing line width, adding line marker
plt.figure(figsize=(20,7))
g=sns.lineplot(x = "Year_month", y = "Total_Orders",data=df_final_ts, color='red', linewidth=1.5,marker="o")
#p=sns.pointplot(x = "Year_month", y = "Total_Orders", data = df_final_ts, ) 
plt.setp(g.get_xticklabels(), rotation=45)
plt.xlabel('Year Month', size=20)
plt.ylabel('Total Orders', size=20)
plt.title("Total orders placed across years (2015-2018)", size = 20)
new_ticks = [i.get_text() for i in g.get_xticklabels()]
plt.xticks(range(0, len(df_final_ts['Year_month']), 5), df_final_ts['Year_month'][::5])
plt.show()


#Step 7 
#Adding data labels
plt.figure(figsize=(20,7))
g=sns.lineplot(x = "Year_month", y = "Total_Orders",data=df_final_ts, color='red', linewidth=1.5,marker="o")
#p=sns.pointplot(x = "Year_month", y = "Total_Orders", data = df_final_ts, ) 
plt.setp(g.get_xticklabels(), rotation=45)
plt.xlabel('Year Month', size=20)
plt.ylabel('Total Orders', size=20)
plt.title("Total orders placed across years (2015-2018)", size = 20)
new_ticks = [i.get_text() for i in g.get_xticklabels()]
plt.xticks(range(0, len(df_final_ts['Year_month']), 5), df_final_ts['Year_month'][::5])

for i in range(len(df_final_ts.Year_month)):
    plt.annotate(str(df_final_ts['Total_Orders'][i]), xy=(i,df_final_ts['Total_Orders'][i]+10), ha='center', va='top',size=12)

plt.show()


#Step 8
#Adding theme to Graph
sns.set_theme(style="whitegrid")
plt.figure(figsize=(20,7))
g=sns.lineplot(x = "Year_month", y = "Total_Orders",data=df_final_ts, color='red', linewidth=1.5,marker="o")
#p=sns.pointplot(x = "Year_month", y = "Total_Orders", data = df_final_ts, ) 
plt.setp(g.get_xticklabels(), rotation=45)
plt.xlabel('Year Month', size=20)
plt.ylabel('Total Orders', size=20)
plt.title("Total orders placed across years (2015-2018)", size = 20)
new_ticks = [i.get_text() for i in g.get_xticklabels()]
plt.xticks(range(0, len(df_final_ts['Year_month']), 5), df_final_ts['Year_month'][::5])

for i in range(len(df_final_ts.Year_month)):
    plt.annotate(str(df_final_ts['Total_Orders'][i]), xy=(i,df_final_ts['Total_Orders'][i]+10), ha='center', va='top',size=12)

plt.show()



