import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
def Temperature():
    GST = pd.read_csv('GlobalSurfaceTemperature.csv')
    GST = GST.set_index(['Year'])
    GG = pd.read_csv('GreenhouseGas.csv')
    GG = GG.set_index(['Year'])
    CO2 = pd.read_csv('CO2ppm.csv')
    CO2 = CO2.set_index(['Year'])
    GTGGCO = pd.concat([GST,GG,CO2],axis = 1)
    GTGGCO_data = GTGGCO
    rng = pd.period_range('1850','2017',freq='A-DEC')
    GTGGCO_data = GTGGCO_data.reset_index()
    GTGGCO_data.index = rng
    GTGGCO_data = GTGGCO_data.drop(['Year'],axis =1)
    figure = GTGGCO_data.iloc[:,3:]
    figure_fill = figure.fillna(method='ffill').fillna(method='bfill')
    figure_train = figure_fill.loc['1850':'2010',:]
    figure_test = figure_fill.loc['2011':,:]

# median
    median_target = GTGGCO_data.loc['1850':'2010','Median']
    upper_target = GTGGCO_data.loc['1850':'2010','Upper']
    lower_target = GTGGCO_data.loc['1850':'2010','Lower']

    model_median  = LinearRegression()
    model_median.fit(figure_train, median_target)
    model_upper  = LinearRegression()
    model_upper.fit(figure_train,upper_target)
    model_lower  = LinearRegression()
    model_lower.fit(figure_train,lower_target)

    m_pre = model_median.predict(figure_test)
    u_pre = model_upper.predict(figure_test)
    l_pre = model_lower.predict(figure_test)

    return list(m_pre),list(u_pre),list(l_pre)



print(Temperature())



