#Following Program is computes future data based on past anaylsis
#Example: If we store for more than 3 years traffic on a website and Now we wish to predict
#         how it wil go for next 10 months based on periodicity.
#         It is unlike other normal linear algorithms where they ignore periodicity in graphs. This one doesnt!

import numpy as np
import statsmodels.api as sm
import pandas as pd
from statsmodels.tsa.arima_process import arma_generate_sample
np.random.seed(12345)

def add_months(months, year, offset):
	for i in range(offset):
		months += 1
		if months > 12:
			months = 1
			year += 1
	return months, year							

arparams = np.array([.75, -.25])
maparams = np.array([.65, .35])

arparams = np.r_[1, -arparams]
maparam = np.r_[1, maparams]
nobs = 250
y = arma_generate_sample(arparams, maparams, nobs)

#Inputs from user
input_len = int(raw_input(""))
input_array = []
for i in range(input_len):
	input_array.append(int(raw_input("")))
#Input Ends
nobs = len(input_array)
y = input_array



dates = sm.tsa.datetools.dates_from_range('1980m1', length=nobs)
endingyear = dates[-1].year
endingmonth = dates[-1].month

#add_months(months, year, offset)
start_point = add_months(endingmonth, endingyear, 1)
end_point = add_months(endingmonth, endingyear, 31)

start_text = ''
start_text = str(start_point[1]) + 'm' + str(start_point[0])
end_text = str(end_point[1]) + 'm' + str(end_point[0])
#print "Start & End", start_text, end_text
y = pd.TimeSeries(y, index=dates)
arma_mod = sm.tsa.ARMA(y, order=(2,2))
arma_res = arma_mod.fit(trend='nc', disp=-1)


#print(arma_res.summary())

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,8))
fig = arma_res.plot_predict(start='1980m1', end=end_text, ax=ax)
legend = ax.legend(loc='upper left')
plt.show()
ans = arma_res.predict(start=start_text, end=end_text)
a = []
a = ans.values[-30:]

for i in a:
	print int(i)
