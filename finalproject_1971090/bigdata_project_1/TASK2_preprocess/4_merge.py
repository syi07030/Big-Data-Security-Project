import os, glob
import pandas as pd

path = "/*data file dir*/"

all_files = glob.glob(os.path.join(path, "*.csv"))

all_csv = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(all_csv, ignore_index=True, sort=True)

df_merged.to_csv( "/*fileOut path*/")