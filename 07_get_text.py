# script for High-Performance Computing Center

import pandas as pd
from Uniscraper import uniscraper
import csv
from ast import literal_eval
import sys
import numpy as np

ID = int(sys.argv[1])
N_jobs = int(sys.argv[2])
print(ID,N_jobs)

df = pd.read_csv("for_hpcc.csv", converters={"link": literal_eval})
N_rows = len(df)
rows_per_job = np.floor(N_rows/(N_jobs-1))

x = ID*rows_per_job
y = (ID+1)*rows_per_job

if ID == N_jobs - 1:
    y = N_rows - (rows_per_job * N_jobs - 1)

for i in range(int(x),int(y)):
    print(i)
    urls = df.link.iloc[i]
    gisjoin = df.GISJOIN.iloc[i]
    for j in range(len(urls)):
        url = urls[j]
        webpage = uniscraper(url)
        smart_text = webpage.text
        csv.writer(open(f"text_{ID}.csv", "a")).writerow([gisjoin, smart_text])
