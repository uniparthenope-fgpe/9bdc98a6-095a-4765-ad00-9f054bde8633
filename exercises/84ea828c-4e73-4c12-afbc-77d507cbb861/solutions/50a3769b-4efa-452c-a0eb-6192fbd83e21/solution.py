import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')
final = df[df["Mine_Name"].map(lambda x: x.startswith('P'))].head()
print(final)
