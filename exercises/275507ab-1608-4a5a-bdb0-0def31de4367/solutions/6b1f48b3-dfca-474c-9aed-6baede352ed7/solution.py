import pandas as pd

baby_names = pd.read_csv("baby_names.csv")

names = len(pd.unique(baby_names.Name))
print(names)
