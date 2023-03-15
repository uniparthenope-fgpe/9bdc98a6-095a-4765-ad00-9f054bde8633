import pandas as pd
import numpy as np

df = pd.read_excel('coalpublic2013.xlsx')
df.insert(1, "column", np.nan)
print(df[:10])
