import pandas as pd
import re

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
# print(df)

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4: -2]]

# print(df.head(5))
# df.to_csv('modified.csv', index=False)
# df.to_excel('modified.xlsx', index=False)
# df.to_csv('modified.txt', index=False, sep='\t')



# Filtering data

# new_df = df.loc[(df['Type 1'] == 'Grass') &  (df['Type 2'] ==  'Poison') & (df['HP'] > 70)]
# new_df = new_df.reset_index(drop=True)
# new_df.reset_index(drop=True, inplace=True)
# print(new_df)
# new_df.to_csv('filtered.csv', index=False)
# print(df.loc[df['Type 1'].str.contains('Fire|Grass', flags=re.I,regex=True)])
# print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I,regex=True)])




# Conditional Changes
# df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Value 1', 'Value 2']
# print(df)



# Aggregate Statistics (groupby)
# df['Defense'] = pd.to_numeric(df['Defense'], errors='coerce')
# print(df.groupby(['Type 1']).sum().sort_values('Defense', ascending=False))
# print(type(df['Defense']))

# df['count'] = 1
# print(df.groupby(['Type 1', 'Type 2']).count()['count'])




# Working with large data
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize=5):
    # print('CHUNK DF')
    # print(df)
    results = df.groupby(['Type 1']).count()
    # print(results)
    new_df = pd.concat([new_df, results])
    
print(new_df.head(10))

import os
print("cpu", os.cpu_count())