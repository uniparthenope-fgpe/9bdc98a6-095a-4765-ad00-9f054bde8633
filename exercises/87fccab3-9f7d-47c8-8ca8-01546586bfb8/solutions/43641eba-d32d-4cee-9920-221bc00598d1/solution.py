import pandas as pd

a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
b = [int(arr_temp) for arr_temp in input().strip().split(' ')]

ds1 = pd.Series(a)
ds2 = pd.Series(b)
ds = ds1 + ds2

print(ds)
