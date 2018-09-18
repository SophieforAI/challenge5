import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def climate_plot():
    df_climate = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    Series_code = ['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE','EN.ATM.NOXE.KT.CE','EN.ATM.GHGO.KT.CE','EN.CLC.GHGR.MT.CE']
    df_gas = df_climate[df_climate['Series code'].isin(Series_code)]
## deal with the lack data
#replace the number
    df_gas = df_gas.replace('..',pd.np.NaN)
#fill the NaN
    df_gas_fillna = df_gas.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_gas_fillna.dropna(how='all',inplace = True)
#add all gas number
    df_gas_sum = df_gas_fillna.sum(axis=0)
    gas_sum = pd.Series(df_gas_sum).iloc[6:]
    df_temperature = pd.read_excel('GlobalTemperature.xlsx')
    df_temperature = df_temperature.set_index(['Date'])
    df_temperature.dropna(how='all',inplace=True)
    df_temperature = df_temperature.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1) 
    df_temperature.index = pd.to_datetime(list(df_temperature.index))
    DEC_sum = df_temperature.resample('A-DEC').sum()
    DEC_sum_selected = DEC_sum[pd.datetime(1990,1,1):]
    DEC_sum_selected.index = pd.to_datetime(list(DEC_sum_selected.index)).year
    DEC_sum_selected.index = DEC_sum_selected.index.astype('object')
    pic_data1_2 = pd.concat([DEC_sum_selected,gas_sum],axis=1)
    pic_data1_2 = pic_data1_2.loc['1990':'2010']
    pic_data1_2.rename(columns={0:'Total GHG'},inplace = True)
    df_max_min = (pic_data1_2-pic_data1_2.min())/(pic_data1_2.max()-pic_data1_2.min())

    df_mm = df_max_min[['Land Average Temperature','Land And Ocean Average Temperature','Total GHG']]
    df_tem = df_temperature.resample('Q').mean()
    df_tem_p = df_tem[['Land Average Temperature','Land And Ocean Average Temperature']]
    #picture 1
    #picture 2
    #picture 3
    #picture 4
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Values')
    df_mm.plot(kind='line',ax=ax1)
    ax2 = fig.add_subplot(2,2,2)
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Values')
    df_mm.plot(kind='bar',ax=ax2)
    ax3 = fig.add_subplot(2,2,3)
    ax3.set_xlabel('Quarters')
    ax3.set_ylabel('Temperature')
    df_tem_p.plot(kind='area',ax=ax3)
    ax4 = fig.add_subplot(2,2,4)
    ax4.set_xlabel('Values')
    ax4.set_ylabel('Values')
    df_tem_p.plot(kind='kde',ax=ax4)
    fig.show()
    return fig


print(climate_plot())
    


