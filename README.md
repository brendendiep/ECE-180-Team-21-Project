# ECE-180-Team-21-Project
                                            Price Analysis and Prediction of Cryptocurrency 
                              Team members: Huan Hu, David Paz, Brenden Diep, Yuwei Li, Jaihee Kim, Chen Du
                                                    Email: huh015@eng.ucsd.edu

**Purpose**  
	In 2017, the cryptocurrency Bitcoin went from $830 to a record of $19,300. As cryptocurrency gains acceptance by its increasing use by a number of companies and organizations, more and more people are trading cryptocurrency while the profits lie on the prediction of its price. Unlike conventional stocks, the cryptocurrency price had big swings in short time. Our team is trying to predict the price of cryptocurrency includes Bitcoin, Ethereum, Ripple and so on with different mathematical models and optimize the trading strategy of cryptocurrency trading.

**Data Acquisition and Analysis**  
	Cryptocurrency price is free of access and we are going to scratch the financial data (prices of stocks, ETFs etc.) from Quandl with Pandas [1]. Numpy modules will be used for data formatting and preparation prior to prediction. We are planning to implement three different algorithms for price prediction: auto-regression (AR) model [2], Kalman filter [3], and machine learning [4]. We’ll analyze the cryptocurrency price of the last 3 years and 80% of the data collected will be used for training and 20% of data will be used to validate our model. Relations between different cryptocurrencies will also be discussed [5]. Matplotlib, Plotly will be used for visualization of results. 

**Schedules**  
02/08~02/15	Data scratch, cleaning and formatting		(Yuwei Li, Jaihee Kim)				

02/15~03/01	Python implementation of AR and Kalman filter model		(David Paz, Brenden Diep)
		Machine learning algorithms (Huan Hu, Chen Du)

03/01~03/08	Prediction and validation of three different algorithms		(Brenden Diep, Jaihee Kim, Yuwei Li)

03/08~03/15	Conclusion and report	(Chen Du, Huan Hu, David Paz)
		

**Reference**
[1] http://pandas-datareader.readthedocs.io/en/latest/remote_data.html#quandl

[2] https://en.wikipedia.org/wiki/Autoregressive_model

[3] Haykin, S. S. (2008). Adaptive filter theory. Pearson Education India.

[4] Christopher, M. B. (2016). PATTERN RECOGNITION AND MACHINE LEARNING. Springer-Verlag New York.
     
