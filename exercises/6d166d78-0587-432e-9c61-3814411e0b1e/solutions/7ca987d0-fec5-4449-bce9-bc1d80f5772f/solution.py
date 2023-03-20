import pandas as pd
from datetime import datetime

date = input()

today = datetime.strptime(date, "%Y-%m-%d")

tomorrow = today + pd.Timedelta(days=1)
yesterday = today - pd.Timedelta(days=1)

print(tomorrow.date())
print(yesterday.date())

