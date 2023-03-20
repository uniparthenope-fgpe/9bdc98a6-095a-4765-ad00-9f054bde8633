import pandas as pd

diamonds = pd.read_csv('diamonds.csv')
print(diamonds.groupby('cut').price.mean())
