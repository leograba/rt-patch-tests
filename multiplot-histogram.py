# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_histogram(data1, data2, data3):
        #print data
	plt.figure(1)
	if sys.argv[4] == 'auto':
		plt.subplot(311)
        	plt.hist(data1)

		plt.subplot(312)
                plt.hist(data2)

		plt.subplot(313)
                plt.hist(data3)
		print 'Bins automatically configured'
	else:
		ax1 = plt.subplot(311)
		plt.hist(data1, bins=int(sys.argv[4]), range=(0.35, 0.45))
		plt.title(u'Simple (approach 1)')
		plt.ylabel(u'Occurrences')
		ax1.set_xlim([0.35, 0.45])		
		ax1.set_ylim([0, 50])

		ax2 = plt.subplot(312)
                plt.hist(data2, bins=int(sys.argv[4]), range=(0.35,0.45))
		plt.title(u'Enhanced (approach 2)')
		plt.ylabel(u'Occurrences')
		ax2.set_xlim([0.35, 0.45])
		ax2.set_ylim([0, 50])

		ax3 = plt.subplot(313)
                plt.hist(data3, bins=int(sys.argv[4]), range=(0.35,0.45))
		plt.title(u'Nanosleep (approach 3)')
		plt.ylabel(u'Occurrences')
		ax3.set_xlim([0.35, 0.45])
		ax3.set_ylim([0, 50])

		print 'Plotting with fixed number of bins and axis limits manually configured'
        plt.xlabel(u'Period (ms)')
	axes = plt.gca()
        fig = plt.gcf()

        plt.show()

def stats_data(data):
	samples_100 = len(data)
	samples_01 = int(samples_100*0.01)
	samples_99 = int(samples_100*0.99)
	data.sort()
	print 'Number of samples: %s' % samples_100
	print 'Fastest period scenario: %.3f' % data[0]
	print '01%% period scenario: %.3f' % data[samples_01]
        print '99%% period scenario: %.3f' % data[samples_99]
	print 'Worst period scenario: %.3f' % data[samples_100-1]
	print 'Median: %.3f' % np.median(data)
	print 'Average: %.3f' % np.mean(data)
	

# Execute the script
full_data1 = []
full_data2 = []
full_data3 = []
with open (sys.argv[1], 'r') as data_input:
       for line in data_input:
               full_data1.append(line)
with open (sys.argv[2], 'r') as data_input:
       for line in data_input:
               full_data2.append(line)
with open (sys.argv[3], 'r') as data_input:
       for line in data_input:
               full_data3.append(line)
#stats_data(np.array(full_data).astype(np.float))
plot_histogram(np.array(full_data1).astype(np.float), np.array(full_data2).astype(np.float), np.array(full_data3).astype(np.float))
