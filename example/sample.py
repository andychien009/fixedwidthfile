from flf.fixedlengthfile import FixedLengthFile

import pandas as pd
import numpy as np

FS = "filespec.csv"
I = "sample.txt"
O = "sampleout.txt"

flf = FixedLengthFile(FS)

data = []
for l in flf.getIterator(I):
    data.append(l)
df = pd.DataFrame(data, columns=flf.getHeader())
print(f"{df.head()}")

df1 = flf.getDataFrame(I)
print(f"{df1.head()}")

df.to_csv("sample.csv", index=False)

with open(O, 'w') as ofile:
    for i, r in df.iterrows():
        ofile.write(f"{flf.getLine(r)}\n")
