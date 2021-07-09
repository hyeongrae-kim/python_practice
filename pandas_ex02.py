import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20210701', periods=6)
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20210701'),
                    'C': pd.Categorical(['a', 'b', 'c', 'd'])})

print(df2.dtypes)  # df2의 각 칼럼들 데이터 형식 출력

print(df.head(2))  # 첫 2행 출력
print(df.tail(2))  # 끝 2행 출력

print(df.index)  # index(index 속성) columns(columns 속성) values(value 속성)

print(df.describe())  # df의 간단한 컬럼별 통계정보를 df 형태로 보여줌

df = df.T  # df의 행과 열을 바꿔줌

print(df)

df['A']  # 특정 칼럼 선택하는 방법
df[0:3]  # 특정 행 선택하는 방법

df.loc['20210701']  # 행 이름으로 특정 행 선택해서 가져오는 방법

df.loc[:, ['A', 'B']]  # 칼럼 a와 b에 해당되는 모든 값 가져오기

