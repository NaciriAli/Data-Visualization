import pandas as pd
import matplotlib.pyplot as plt
df3=pd.read_csv("D:/Autormt°/Courses/Data Visualization/[DesireCourse.Net] Udemy - Python for Data Science and Machine Learning Bootcamp/1. Course Introduction/Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df3")
# df3.info()
# print(df3.head())
# df3.plot.scatter(x='a',y='b',figsize=(10,3),c="red")
# df3['a'].hist(bins=30)
# df3[['a','b']].plot.box()
# df3['d'].plot.kde()
# df3['d'].plot.kde(lw=3,ls='--',c='orange')
df3.loc[:30,].plot.area(alpha=0.5)
plt.legend(loc='upper right',bbox_to_anchor=(1.13, 0.7))
plt.show()