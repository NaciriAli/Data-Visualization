import seaborn as sns 
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic=sns.load_dataset('titanic')
# print(titanic.head(5))
# sns.jointplot(x='fare',y='age',data=titanic)
# sns.distplot(titanic['fare'],kde=False,color='pink')
# sns.boxplot(x='class',y='age',data=titanic)
# sns.swarmplot(x='class',y='age',data=titanic)
# sns.countplot(x="sex",data=titanic)
# sns.heatmap(titanic.corr(),cmap='coolwarm')
# g=sns.FacetGrid(titanic,col='sex')
# g.map(plt.hist,'age')
plt.show()