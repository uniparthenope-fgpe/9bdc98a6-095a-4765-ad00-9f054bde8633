import pandas as pd

dataframe = pd.read_csv('data.csv', header=0)
dataframe_sorted = dataframe.sort_values(by=["name"])
print(dataframe_sorted)
