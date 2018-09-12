# IPython log file
import xlrd
import pandas as pd
def co2():
    df_climate = pd.read_excel('../Code/ClimateChange.xlsx',sheetname='Data')
    df_climate = df_climate.replace('..',float(0))
    # df_climate = df_climate.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_climate[2011] = pd.to_numeric(df_climate[2011],errors='coerce')
    df_climate[2011] = df_climate[2011].fillna(0)
    df_climate['Sum emissions']=  df_climate.iloc[:,6:].apply(lambda x:x.sum() ,axis=1)
    df_country = pd.read_excel('../Code/ClimateChange.xlsx',sheetname='Country')
    df_country = df_country.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_climate_country = pd.merge(df_climate,df_country,on='Country code',how='left')
    df_climate_country_group = df_climate_country.groupby(['Income group'],as_index=False)
    Sum_emissions = df_climate_country_group['Sum emissions'].sum()
    df_climate_country_c_group = df_climate_country.groupby(['Income group','Country name_y'],as_index=False)
    Sum_emissions_country = df_climate_country_c_group['Sum emissions'].sum()
    highest_emissions = Sum_emissions_country.groupby(['Income group'],as_index = False).max()
    lowest_emissions = Sum_emissions_country.groupby(['Income group'],as_index = False).min()
    result = pd.concat([Sum_emissions,highest_emissions,lowest_emissions],axis=1)
    results = result.iloc[:,[0,1,3,4,6,7]]
    results.columns = ['Income group','Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']

    results =results.set_index('Income group')
    return results

print(co2())
