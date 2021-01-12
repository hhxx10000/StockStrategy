import pandas as pd

df = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150], columns=['A'])
df.sort_index(inplace=True)
print(df.to_string())