import pandas as pd

df = pd.read_csv('out.csv',encoding='latin1',delimiter=';',header=None)
df.to_csv('executive.csv',index=False)
