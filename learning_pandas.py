import pandas as pd

# Loading data

df = pd.read_csv('pokemon_data.csv')
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# df_txt = pd.read_csv('pokemon_data.csv', delimiter='\t')

# df
# df_txt
# df_xlsx


# Reading data from the dataframe

# print(df.head(5))
# print(df.columns)
# print(df[['Name', 'Type 1', 'HP']][-10:])
# print(df.iloc[0:10][['Name', 'HP']])
# print(df.iloc[[2, 1], [5, 4]])
# for index, row in df.iterrows():
#  if index <= 10:
#    print(index, row[['Name', 'HP']])
# print(df.loc[df['Type 1'] == 'Grass' ][0:10])



# Sorting and describing data

# print(df.describe())
# print(df.sort_values(['Name', 'Type 1'], ascending=[1,0]))



# Making changes to the data

# print(df.head(5))
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df.head(5))
# df = df.drop(columns=['Total'])
df['Total'] = df.iloc[:,4:10].sum(axis=1)

print(df)
  
