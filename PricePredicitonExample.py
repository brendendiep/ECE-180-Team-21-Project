import pandas as pd
import time
import matplotlib.pyplot as plt
import datetime
import numpy as np

# get market info for bitcoin from the start of 2016 to the current day
bitcoin_market_info = pd.read_html(
    "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=" + time.strftime("%Y%m%d"))[0]
# convert the date string to the correct date format
bitcoin_market_info = bitcoin_market_info.assign(Date=pd.to_datetime(bitcoin_market_info['Date']))
# when Volume is equal to '-' convert it to 0
bitcoin_market_info.loc[bitcoin_market_info['Volume'] == "-", 'Volume'] = 0
# convert to int
bitcoin_market_info['Volume'] = bitcoin_market_info['Volume'].astype('int64')

market_info = bitcoin_market_info

model_data = market_info[['Date'] + ['Close']]
# need to reverse the data frame so that subsequent rows represent later timepoints
model_data = model_data.sort_values(by='Date')
split_date = '2017-06-01'

training_set, test_set = model_data[model_data['Date'] < split_date], model_data[model_data['Date'] >= split_date]
training_set = training_set.drop('Date', 1)
test_set = test_set.drop('Date', 1)
window_len = 10
col = 'Close'

# format the training data and test data
LSTM_training_inputs = []
for i in range(len(training_set) - window_len):
    temp_set = training_set[i:(i + window_len)].copy()
    temp_set.loc[:, col] = temp_set[col] / temp_set[col].iloc[0] - 1
    LSTM_training_inputs.append(temp_set)

LSTM_training_outputs = (training_set['Close'][window_len:].values / training_set['Close'][:-window_len].values) - 1

LSTM_test_inputs = []
for i in range(len(test_set) - window_len):
    temp_set = test_set[i:(i + window_len)].copy()
    temp_set.loc[:, col] = temp_set[col] / temp_set[col].iloc[0] - 1
    LSTM_test_inputs.append(temp_set)
LSTM_test_outputs = (test_set['Close'][window_len:].values / test_set['Close'][:-window_len].values) - 1

# I find it easier to work with numpy arrays rather than pandas dataframes
# especially as we now only have numerical data
LSTM_training_inputs = [np.array(LSTM_training_input) for LSTM_training_input in LSTM_training_inputs]
LSTM_training_inputs = np.array(LSTM_training_inputs)

LSTM_test_inputs = [np.array(LSTM_test_inputs) for LSTM_test_inputs in LSTM_test_inputs]
LSTM_test_inputs = np.array(LSTM_test_inputs)

# import the relevant Keras modules
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.layers import LSTM
from keras.layers import Dropout


def build_model(inputs, output_size, neurons, activ_func="linear",
                dropout=0.25, loss="mae", optimizer="adam"):
    model = Sequential()

    model.add(LSTM(neurons, input_shape=(inputs.shape[1], inputs.shape[2])))
    model.add(Dropout(dropout))
    model.add(Dense(units=output_size))
    model.add(Activation(activ_func))

    model.compile(loss=loss, optimizer=optimizer)
    return model


# random seed for reproducibility
np.random.seed(202)
# initialise model architecture
bitc_model = build_model(LSTM_training_inputs, output_size=1, neurons=6)
# model output is next price normalised to 10th previous closing price
# train model on data
# note: eth_history contains information on the training error per epoch
bitc_history = bitc_model.fit(LSTM_training_inputs, LSTM_training_outputs,
                              epochs=2, batch_size=1, verbose=2, shuffle=True)



fig, ax1 = plt.subplots(1,1)
ax1.plot(model_data['Date'][window_len:].astype(datetime.datetime),
         model_data['Close'][window_len:], label='Actual')
ax1.plot(model_data[model_data['Date']< split_date]['Date'][window_len:].astype(datetime.datetime),
         ((np.transpose(bitc_model.predict(LSTM_training_inputs))+1) * training_set['Close'].values[0:-window_len])[0],
         label='Predicted')
ax1.plot(model_data[model_data['Date']>= split_date]['Date'][window_len:].astype(datetime.datetime),
         ((np.transpose(bitc_model.predict(LSTM_test_inputs))+1) * test_set['Close'].values[0:-window_len])[0],
         label='Predicted')