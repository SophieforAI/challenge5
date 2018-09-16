import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
def co2_gdp_plot():
    df_data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    df_data = df_data.replace({'..':pd.np.NaN})
    df_co2 = df_data[df_data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    df_gdp = df_data[df_data['Series code']=='NY.GDP.MKTP.CD'].set_index('Country code')
    df_co2 = df_co2.iloc[:,5:].fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_gdp = df_gdp.iloc[:,5:].fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_co2['co2_sum']=df_co2.sum(axis=1)
    df_gdp['gdp_sum']=df_gdp.sum(axis=1)
    df_merge = pd.concat([df_co2['co2_sum'],df_gdp['gdp_sum']],axis=1)
    df_merge_fill = df_merge.fillna(value=0)
    df_max_min = (df_merge_fill-df_merge_fill.min())/(df_merge_fill.max()-df_merge_fill.min())
    china = np.array(np.round(df_max_min.loc[df_max_min.index=='CHN'],3)).tolist()[0]
    countries_labels = ['USA', 'CHN', 'FRA', 'RUS', 'GBR']
    sticks_labels = []
    labels_position = []
    for i in range(len(df_max_min)):
        if df_max_min.index[i] in countries_labels:
            sticks_labels.append(df_max_min.index[i])
            labels_position.append(i)

    fig = plt.subplot()
    df_max_min.plot(kind= 'line',title='GDP-CO2',ax=fig)
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(labels_position,sticks_labels,rotation='vertical')
    plt.show()
    return fig,china
