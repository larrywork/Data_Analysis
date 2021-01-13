#importing libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
df=pd.read_csv("all_seasons.csv")

#viewing a snapshot of the dataset
df.head()

print(df.shape) #Getting the number of rows and columns of the dataframe using the "shape command"


df.info()#Getting information about null values and data types using the "info command"

plt.figure(figsize=(18,5))
plt.subplot(1,3,1)
sns.histplot(df['age'], kde = True, color ='red', bins = 30) 
plt.subplot(1,3,2)
sns.boxplot( y=df["age"] );
plt.subplot(1,3,3)
sns.violinplot( y=df["age"]);


#Getting Percentage distribution of "Players" across the dataset fot top 5 countries
df_counts= df.groupby(['country'])['player_name'].agg('count').reset_index(name="Count_of_players")
df_counts_top5= df_counts.sort_values(by=['Count_of_players'],ascending=False)
df_counts_top5= df_counts_top5.head(5)

#Calculating distribution across of players for top 5 Countries
fig1, ax1 = plt.subplots(figsize=(10,10))
ax1.pie(df_counts_top5['Count_of_players'],labels=df_counts_top5['country'],colors =["pink","orange","teal","yellow","cyan"],autopct = '%1.1f%%')
ax1.set_title('Distribution acorss of players for top 5 Countries',fontsize = 16)

#plotting scatter plot between Player Height and Player Height
sns.relplot(x=df['player_height'], y=df['player_weight'], height=4, aspect=2/1);


#Getting count of "Players" for top 10 colleges
df_counts= df.groupby(['college'])['player_name'].agg('count').reset_index(name="Count_of_players")
df_counts_top10= df_counts.sort_values(by=['Count_of_players'],ascending=False)
df_counts_top10= df_counts_top10.head(10)
sns.catplot(x='college', y='Count_of_players', data=df_counts_top10,kind='bar',palette='GnBu',height=6,aspect=2)
plt.title('Player Count across top 10 colleges')
plt.show()

#Creating Weight_Brackets and Height_Brackets Columns
bins = [20, 40, 60, 80, 100, 120, 140, 160,180]
df['Weight_Brackets']=pd.cut(df['player_weight'], bins)
bins = [160, 170, 180, 190, 200, 210, 220, 230,240]
df['Height_Brackets']=pd.cut(df['player_height'], bins)


f = plt.figure(figsize=(15,10))
ax = f.add_subplot(1,1,1)

sns.histplot(data=df, ax=ax, stat="count", multiple="stack",
             x="team_abbreviation", kde=False,
             palette="pastel", hue="Height_Brackets",
             element="bars", legend=True)

ax.set_title("Distribution of Height of players across Teams")
ax.set_xlabel("Team")
ax.set_ylabel("Player Count")

#Plotting height weight segments
df_weight_height=  df.groupby(['Height_Brackets','Weight_Brackets'],as_index=False)[('player_name')].count()
p=sns.catplot(x='Height_Brackets', y='player_name', hue='Weight_Brackets', 
            data=df_weight_height,kind='bar',palette='bright',height=4, aspect=2)
plt.ylabel('Total Players')

#Creating dataframe for time series chart
df_year_players=  df.groupby(['draft_year'])['player_name'].agg('count').reset_index(name="Count_of_players")
df_year_players= df_year_players[df_year_players['draft_year']!="Undrafted"]


#Creating time series line chart
sns.set_theme(style="whitegrid")
plt.figure(figsize=(20,7))

g=sns.lineplot(x = "draft_year", y = "Count_of_players",data=df_year_players, color='red', linewidth=1.5,marker="o")

plt.setp(g.get_xticklabels(), rotation=45)
plt.xlabel('Year', size=20)
plt.ylabel('Total Players', size=20)
plt.title("Total players  across years (1963-2019)", size = 20)
new_ticks = [i.get_text() for i in g.get_xticklabels()]

 
for i in range(len(df_year_players.draft_year)):
    plt.annotate(str(df_year_players['Count_of_players'][i]), xy=(i,df_year_players['Count_of_players'][i]+10), ha='center', va='top',size=12)
 
plt.show()