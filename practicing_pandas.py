import pandas as pd


df = pd.read_csv('pokemon_data.csv')

# for i in range(4,9):
#     df[]
df['Total'] = df.iloc[:,4:9].sum(axis=1)
df['Average'] = df.iloc[:,4:9].mean(axis=1)
# df['Average'] = df.iloc[:,4:9]
df.loc[( df['Type 2'].isna()), 'Type 2'] = 'NULL'
print(df.iloc[4,3])
# print(df.iloc[4,3].dtype)
# print(df.dtypes)
print(df.head(5))