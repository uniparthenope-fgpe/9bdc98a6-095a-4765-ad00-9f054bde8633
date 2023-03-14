import pandas as pd
import ast

dictionary = ast.literal_eval(input())
dataframe = pd.DataFrame(dictionary)
print(dataframe)
