import os
import glob
import numpy as np
import pandas as pd
from numpy import genfromtxt

cwd = os.getcwd()

count = 0
data = []
df = pd.DataFrame()

# files = glob.glob(cwd + '/*.csv')

for subdir, dirs, files in os.walk(cwd):
	for file in files:
		if file.endswith(".csv"):
			data = genfromtxt(file, delimiter = ",")
			df[count] = data
			count = count + 1

df.to_csv('df_trace.csv')