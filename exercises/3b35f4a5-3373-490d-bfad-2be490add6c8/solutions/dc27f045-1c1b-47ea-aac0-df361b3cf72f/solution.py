import pandas as pd

baby_names = pd.read_csv("baby_names.csv")
del baby_names['Unnamed: 0']
del baby_names['Id']
del baby_names['Year']

names = baby_names.groupby('Name').sum(numeric_only=True)
sorted_names = names.sort_values('Count', ascending=0)
print(sorted_names.head(1))
