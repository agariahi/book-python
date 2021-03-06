import pandas as pd
import numpy as np

NUMBER = 100

s = pd.Series(
    data=np.random.randn(NUMBER),
    index=pd.date_range('1970-01-01', freq='D', periods=NUMBER))

s['1970-02-14':'1970-02']
# 1970-02-14   -0.189844
# 1970-02-15    0.354809
# 1970-02-16   -2.024668
# 1970-02-17   -1.282907
# 1970-02-18   -0.884613
# 1970-02-19    0.405803
# 1970-02-20    0.586722
# 1970-02-21    2.493938
# 1970-02-22    0.234319
# 1970-02-23   -0.017180
# 1970-02-24    0.116735
# 1970-02-25    1.845281
# 1970-02-26    0.478368
# 1970-02-27   -0.367546
# 1970-02-28   -0.744079
# Freq: D, dtype: float64
