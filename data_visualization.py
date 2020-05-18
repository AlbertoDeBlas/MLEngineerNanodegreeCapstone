from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




def correlationMap(d):

    # Compute the correlation matrix
    corr = d.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    
def display_component(v, features_list, component_num, n_components, n_weights=10):
    
    # get index of component (last row - component_num)
    row_idx = n_components-component_num

    # get the list of weights from a row in v, dataframe
    v_1_row = v.iloc[:, row_idx]
    v_1 = np.squeeze(v_1_row.values)

    # match weights to features in counties_scaled dataframe, using list comporehension
    comps = pd.DataFrame(list(zip(v_1, features_list)), 
                         columns=['weights', 'features'])
    
    # we'll want to sort by the largest n_weights
    # weights can be neg/pos and we'll sort by magnitude
    comps['abs_weights']=comps['weights'].apply(lambda x: np.abs(x))
    sorted_weight_data = comps.sort_values('abs_weights', ascending=False).head(n_weights)

    # display using seaborn
    ax=plt.subplots(figsize=(10,6))
    ax=sns.barplot(data=sorted_weight_data, 
                   x="weights", 
                   y="features", 
                   palette="rocket")
    ax.set_title("PCA Component Makeup, Component #" + str(component_num))
    plt.show()
    
def display_null_distribution(df):
    f, (ax1) = plt.subplots(1, 1, figsize=(20, 7), sharex=True)

    x = df.index
    y1 = df.values
    sns.barplot(x=x, y=y1, palette="rocket", ax=ax1)
    ax1.axhline(0, color="k", clip_on=False)
    ax1.set_ylabel("Nulls")
    ax1.set_xlabel("Features")
    ax1.set_xticks([])

    
def display_variance_distribution(df):
    f, (ax1) = plt.subplots(1, 1, figsize=(20, 7), sharex=True)

    x = list(df)
    y1 = df.values
    sns.barplot(x=x, y=y1, palette="rocket", ax=ax1)
    ax1.axhline(0, color="k", clip_on=False)
    ax1.set_ylabel("Nulls")
    ax1.set_xlabel("Features")
    ax1.set_xticks([])