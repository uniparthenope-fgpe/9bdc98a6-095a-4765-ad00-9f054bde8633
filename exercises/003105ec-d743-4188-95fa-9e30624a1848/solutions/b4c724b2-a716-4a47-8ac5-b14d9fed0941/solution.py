import pandas as pd

N = input().strip()

df = pd.read_excel('employee.xlsx')
df2 = df.set_index(['hire_date'])
result = df2.loc[N]
print(result)
