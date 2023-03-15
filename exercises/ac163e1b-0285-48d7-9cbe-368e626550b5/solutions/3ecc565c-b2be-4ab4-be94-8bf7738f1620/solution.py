import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')
final = df[df["Labor_Hours"] > 20000].head()
print(final)
