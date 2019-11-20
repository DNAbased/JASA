import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

dict = {'Level': range(1,101)}
df = pd.DataFrame(dict)

df = df.assign(XP = lambda x: np.ceil((x.Level+1)**(7/3)))

df = df.assign(HP = lambda x: np.ceil(46+x.Level*x.Level*0.5+x.Level*2+x.Level))

# exp plot
sns.set()
fig, ax = plt.subplots()
ax = sns.scatterplot(data=df, x='Level', y='XP')
ax.set(xlabel='Level', ylabel='Experience required for next level')
ax.set(xlim=(0, 100))
ax.set(ylim=(0, 5e4))
fig.savefig('info/plot_exp_per_level.png')

# hp plot
sns.set()
fig, ax = plt.subplots()
ax = sns.scatterplot(data=df, x='Level', y='HP')
ax.set(xlabel='Level', ylabel='HP at current level')
ax.set(xlim=(0, 100))
ax.set(ylim=(0, 6e3))
fig.savefig('info/plot_hp_per_level.png')
