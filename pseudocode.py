# machine learning module TensorFlow only work in Python 3, so let's use Python 3 for the whole project.

import header  # include every module we need (Numpy, pandas, keras,...)


define currencyName = ['Bitcoin','Ether','Ripple']  # list of strings
define priceStartDate = ['2018-01-01'] # list of string with 1 item, that's the date we will start analyzing
define getPriceStartDate = ['2016-10-01'] # list of string with 1 item, that's the date we will start scratching
define priceAcutal = [] # pandas dataframe, actual price
'''
eg.
        Date	    Price
1762	2013-04-28	134.21
1761	2013-04-29	144.54
'''
define priceAll = [] # pandas dataframe
'''
           Date     Price  Price_AR  Price_Kalman  Price_LSTM  Price_ML
1762 2013-04-28    134.21    134.21        134.21      134.21    134.21
1761 2013-04-29    144.54    144.54        144.54      144.54    144.54
1760 2013-04-30    139.00    139.00        139.00      139.00    139.00 
'''



def predictionPriceAnalysis(priceAll){
    ''' 
    # this function analyze the performance of price prediction and plot
    # we should discuss what kind of properties we need to analyze, 
    for example,  root mean square error, are these method correlated?, what factors that suggest a good prediction(oil price, stock price,...)
    '''

}


priceActual = getPriceData(currencyName,getPriceStartDate)
def getPriceData(currencyName,getPriceStartDate){
    '''
    # data acquisition, get the price of currencyName from priceStartDate to today
    '''
}

priceAll = predictPriceData(priceActual)
def predictPriceData(priceActual){
    '''
    predict the price, return a dataframe with 'Date','Price','Method'
    '''
    price0 = predictPriceData_AR(priceActual)
    price1 = predictPriceData_Kalman(priceActual)
    price2 = predictPriceData_LSTM(priceActual)
    price3 = predictPriceData_ML(priceActual)

    md = priceActual
    md['Price_AR'] = pd.Series(price0,index=md.index)
    md['Price_Kalman'] = pd.Series(price1,index=md.index)
    md['Price_LSTM'] = pd.Series(price2,index=md.index)
    md['Price_ML'] = pd.Series(price3,index=md.index)

    return md
}

