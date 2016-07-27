# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_histogram(data):
        #print data
	if sys.argv[3] == 'auto':
        	plt.hist(data)
		print 'Bins automatically configured'
	else:
		plt.hist(data, bins=int(sys.argv[3]), range=(0.0,1.0))
		print 'Plotting with fixed number of bins'
        plt.title(u'Histogram of the square wave period - ' + sys.argv[2])
        plt.xlabel(u'Period (ms)')
        plt.ylabel(u'Occurrences')
	axes = plt.gca()
	#axes.set_xlim([0.0,1.0])

	#plt.xaxis([0.0, 7.0])

        fig = plt.gcf()

        plt.show()

def stats_data(data):
	samples_100 = len(data)
	samples_01 = int(samples_100*0.01)
        #samples_02 = int(samples_100*0.02)
        #samples_03 = int(samples_100*0.03)
        #samples_04 = int(samples_100*0.04)
        #samples_05 = int(samples_100*0.05)
	#samples_95 = int(samples_100*0.95)
	#samples_96 = int(samples_100*0.96)
	#samples_97 = int(samples_100*0.97)
	#samples_98 = int(samples_100*0.98)
	samples_99 = int(samples_100*0.99)
	data.sort()
	print 'Number of samples: %s' % samples_100
	print 'Fastest period scenario: %.3f' % data[0]
	print '01%% period scenario: %.3f' % data[samples_01]
        #print '02%% period scenario: %.3f' % data[samples_02]
        #print '03%% period scenario: %.3f' % data[samples_03]
        #print '04%% period scenario: %.3f' % data[samples_04]
        #print '05%% period scenario: %.3f' % data[samples_05]

	#print '95%% period scenario: %.3f' % data[samples_95]
        #print '96%% period scenario: %.3f' % data[samples_96]
        #print '97%% period scenario: %.3f' % data[samples_97]
        #print '98%% period scenario: %.3f' % data[samples_98]
        print '99%% period scenario: %.3f' % data[samples_99]
	print 'Worst period scenario: %.3f' % data[samples_100-1]
	print 'Median: %.3f' % np.median(data)
	print 'Average: %.3f' % np.mean(data)
	

# Execute the script
full_data = []
with open (sys.argv[1], 'r') as data_input:
       for line in data_input:
               full_data.append(line)
stats_data(np.array(full_data).astype(np.float))
plot_histogram(np.array(full_data).astype(np.float))
