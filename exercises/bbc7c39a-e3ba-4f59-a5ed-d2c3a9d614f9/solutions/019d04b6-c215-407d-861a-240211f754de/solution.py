import pandas as pd

baby_names = pd.read_csv("baby_names.csv")

ratio = baby_names.Gender.value_counts()

if ratio['M'] > ratio['F']:
    print("Male -", ratio['M'])
else:
    print("Female -", ratio['F'])
