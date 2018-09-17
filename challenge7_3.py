import pandas as pd
import matplotlib import pyplot plt

def climate_plot():
    df_climate = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    Series_code = ['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE','EN.ATM.NOXE.KT.CE','EN.ATM.GHG
O.KT.CE','EN.CLC.GHGR.MT.CE']
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
    DEC_sum = df_temperature.resample('A-DEC',how='sum')
    #picture 1
    #picture 2
    #picture 3
    #picture 4
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)


    


