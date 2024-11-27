import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = df["weight"]/(df["height"]/100)**2
df['overweight'] = (df['overweight'] > 25).astype(int)
# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, 
                 id_vars=['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cardio'],
                 value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active'],
                 var_name='Indicator', 
                 value_name='Health Status')


    # 6
    df_cat_grouped = df_cat.groupby(['cardio', 'Indicator', 'Health Status']).size().reset_index(name='count')


    # 7
    fig = sns.catplot(x="Indicator", hue="Health Status", kind="count", col="cardio", data=df_cat)
    plt.show()


    # 8
    fig = fig.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    plt.show()

    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]


    # 12
    corr = df_heat.select_dtypes(include=['float64', 'int64']).corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, cmap='coolwarm', square=True)

    # 16
    fig.savefig('heatmap.png')
    plt.show()
    return fig
