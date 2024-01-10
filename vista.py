import pandas as pd
import numpy as np
path="datasets/"

df=pd.read_csv(path+"hechos.csv")
"""df["x"].replace("SD",np.nan,inplace=True)
df["x"]=df["x"].apply(lambda x:float(x))
df["y"].replace("SD",np.nan,inplace=True)
df["y"]=df["y"].apply(lambda x:float(x))"""

df["x"].replace("SD",np.nan,inplace=True)

mask=df["x"]=="SD"
print(df[mask][["x","y"]])