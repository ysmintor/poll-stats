import pandas as pd
import os
import seaborn as sns
sns.set_theme(style="ticks")
sns.set(rc={'figure.figsize':(19,8.27)})
# 处理中文显示
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['SimHei', 'MicroSoft YaHei']

path = '~/Downloads'
filename = 'res.xlsx'
poll_col = 2 #投票列

df = pd.read_excel(os.path.join(path, filename), usecols=[poll_col])

df.columns = ['poll']
df = df['poll']

df = df.str.split(pat=',\s')
df = df.explode()

stats = df.value_counts(sort=True, ascending=False)

ax = sns.barplot(x=stats.index, y=stats.values)
ticks = ax.get_xticklabels()
ticks = ax.set_xticklabels(ticks, 
                          rotation=60, 
                          horizontalalignment='right')
print('前10信息如下')
stats.head(10)