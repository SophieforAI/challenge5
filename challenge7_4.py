import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
GST = pd.read_csv('GlobalSurfaceTemperature.csv')
GST = GST.set_index(['Year'])
GG = pd.read_csv('GreenhouseGas.csv')
GG = GG.set_index(['Year'])
CO2 = pd.read_csv('CO2ppm.csv')
CO2 = CO2.set_index(['Year'])
GTGGCO = pd.concat([GST,GG,CO2],axis = 1)
GTGGCO_data = GTGGCO.loc[:,['Median','Upper','Lower','CO2','CO2 concentrations (NOAA (2017)) (parts per million)']]
rng = pd.period_range('1850','2017',freq='A-DEC')
GTGGCO_data = GTGGCO_data.reset_index()
GTGGCO_data.index = rng
GTGGCO_data = GTGGCO_data.drop(['Year'],axis =1)
GTGGCO_train = GTGGCO_data.loc[1850:2010]
GTGGCO_test = GTGGCO_data.loc[2011:]
GST_median = GTGGCO_data.loc[:,['Median']]
rolmean = pd.rolling_mean(GST_median,window = 15)
rolmean.plot()
plt.show()

