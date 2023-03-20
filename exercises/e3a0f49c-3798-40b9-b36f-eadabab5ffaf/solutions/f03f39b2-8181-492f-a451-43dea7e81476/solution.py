import pandas as pd

diamonds = pd.read_csv('diamonds.csv')
print(diamonds.cut.value_counts(normalize=True))
