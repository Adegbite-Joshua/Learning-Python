import pandas as pd


df = pd.read_csv('pokemon_data.csv')

# for i in range(4,9):
#     df[]
df['Total'] = df.iloc[:,4:9].sum(axis=1)
df['Average'] = df.iloc[:,4:9].mean(axis=1)
# df['Average'] = df.iloc[:,4:9]
df.loc[( df['Type 2'].isnull()), 'Type 2'] = 'NULL'
df.loc[ df['Type 1'].str.lower() == 'bug', 'Legendary'] = True
# print(df.iloc[4,3])
# print(df.iloc[4,3].dtype)
# print(df.dtypes)
# df = df.drop(columns=['#'])
print(df.head(15))
df.to_csv('practice_data.csv', index=False)