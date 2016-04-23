# -*- coding: utf-8 -*-

#Used for converting the cvs to an array.
# #this was a greate idea
#Author: Benjamin R. Nold

import csv

electrodes = "electrodes_name = ["
scripts = "scripts_name = ["

with open('backside.csv', 'rb') as csvfile:
	fieldnames = ['electrode', 'response']
	theReader = csv.DictReader(csvfile, fieldnames = fieldnames, delimiter=',')
	for row in theReader:
		electrodes = electrodes + "0x" +row['electrode'] + ", "
		scripts = scripts + "\"" + row['response'] + "\", "
	#now finish the strings
	l = len(electrodes)
	electrodes = electrodes[:(l-2)]
	electrodes = electrodes + "]"

	l = len(scripts)
	scripts = scripts[:(l-2)]
	scripts = scripts + "]"

	print electrodes
	print scripts