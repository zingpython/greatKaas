import datetime
import imp
def benchmark(function, repit):

	timeStart.datetime.now();
	for i in range(0, repit, 1):
		function()

	timeEnd.datetime.now();
	return (timeEnd-timeStart);

fib = imp.load_source("fibonacci","C:\Users\Matthew\Documents\Python\Python 11.py");