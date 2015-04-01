#!/usr/bin/python
# -*- coding: utf-8 -*-,  

# 1 Open Terminal:
# 2 run the command
# python 'filename'.py 'filename2.csv'
# It will output the txt files in the folder named after your .csv filename in the directory where the .csv file is present
# You can also use to output column Just uncomment the 2nd code blocks and comment the first one and follow the same steps.

__author__="noones"


#--------------------------------------------------------------------------
# USe for Row Extraction
#--------------------------------------------------------------------------

import sys, string, os
import ntpath
from itertools import izip
import csv

#path = os.path.dirname(os.path.abspath(sys.argv[1]))+"/"+sys.argv[1]
path = sys.argv[1]
filename = ntpath.basename(path)

location = sys.argv[2]

if not os.path.exists(location+filename):
 	os.makedirs(location+filename)

datafile = open(sys.argv[1], 'rU')
datareader = csv.reader(datafile)
count=0
for index, row in enumerate(datareader):
    output_file = open(os.path.join(location+filename, str(index)+'.txt'),'wb')
    output_csv = csv.writer(output_file)
    output_csv.writerow(row)
    count=count+1
datafile.close()

print "\n-------------------------------------------------------------------------"
print ("total {} .txt files written to ".format(count)+location+filename,count)
print "-------------------------------------------------------------------------\n"
#--------------------------------------------------------------------------
# Uncomment to use for Column Extraction
#--------------------------------------------------------------------------

#import sys, string, os
#import ntpath
#from itertools import izip
#import csv

#path = os.path.dirname(os.path.abspath(sys.argv[1]))+"/"+sys.argv[1]
# path = sys.argv[1]
# filename = ntpath.basename(path)

# location = sys.argv[2]

# if not os.path.exists(location+filename):
#  	os.makedirs(location+filename)

# a = izip(*csv.reader(open(sys.argv[1], "rbU")))
# csv.writer(open("output.csv", "wb")).writerows(a)
# datafile = open('output.csv', 'rU')

# datareader = csv.reader(datafile)
# data = []
# for index, row in enumerate(datareader):
#     output_file = open(os.path.join(location+filename, str(index)+'.txt'),'wb')
#     output_csv = csv.writer(output_file)
#     output_csv.writerow(row)


# datafile.close()
