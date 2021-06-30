# pandas

import pandas as pd

df=pd.read_csv('hello.csv')
print(df)

print(df.head(1))
print(df.shape)  # row, column(행, 열)
print(df.shape[0])  # row 행개수
print(df.shape[1])  # column 열개수