import pandas as pd

drinks = pd.read_csv("drinks.csv")
print(drinks.groupby(by='continent').beer_servings.mean())
