import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20210701', periods=6)
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20210701'),
                    'C': pd.Categorical(['a', 'b', 'c', 'd'])})

print(df2.dtypes)  # df2의 각 칼럼들 데이터 형식 출력

