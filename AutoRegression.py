
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
def autoregress(inputFile, trainPercent):
	'''
		argument1: inputFile
		type: str
		argument2: Percent of training data (i.e: 80% = .8)
		type: double
	'''
	series = Series.from_csv(inputFile, header=0)
	# split dataset
	X = series.values
	trainLimit = int(len(X)*trainPercent)
	train, test = X[1:trainLimit], X[trainLimit-7:]
	# train autoregression
	model = AR(train)
	model_fit = model.fit()
	print('Lag: %s' % model_fit.k_ar)
	print('Coefficients: %s' % model_fit.params)
	# make predictions
	predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
	for i in range(len(predictions)):
		print('predicted=%f, expected=%f' % (predictions[i], test[i]))
	error = mean_squared_error(test, predictions)
	print('Test MSE: %.3f' % error)
	# plot results
	pyplot.plot(test)
	pyplot.plot(predictions, color='red')
	pyplot.show()
