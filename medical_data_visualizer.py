import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")


# 2
#f['bmi'] = df['weight'] / np.square(df['height']/100)
#df = df.drop(columns=['bmi'])
df['overweight'] = np.where(df['weight'] / np.square(df['height']/100) > 25, 1, 0)

# 3
#df['cholesterol'].value_counts()
#df['gluc'].value_counts()
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['id'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat = df_cat.rename(columns={'size': 'total'})
    

    # 7
    fig_test = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    # 8
    fig = fig_test


    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))].copy()
    
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,  dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12,10))

    # 15
    sns.heatmap(corr, mask=mask, cbar=True, ax=ax, square=True, cmap='coolwarm', annot=True, fmt='.1f')

    # 16
    fig.savefig('heatmap.png')
    return fig
