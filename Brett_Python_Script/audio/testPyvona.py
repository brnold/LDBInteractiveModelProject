# -*- coding: utf-8 -*-
import pyvona
import  csv
import os


#create the voice
v = pyvona.create_voice('GDNAJGKAD65YFOAQDQUA','yEI2lUqBdbBfTrgujIcIoLzJrIgZv824UpGRv0Xs')
v.voice_name = "Salli"
v.codec = "mp3"

#Use the following line to submit a simple text to Ivona and get a MP3 file. 
#v.fetch_voice('Text you want to make to MP3', 'Name_of_file')

#Line 18-23 is used to open the CSV file and turn the whole list of text to mp3 files
# Open and parse the CSV of the data

with open('backSide_from_Bip.csv', 'rb') as csvfile:
	fieldnames = ['soundNumber', 'response']
	theReader = csv.DictReader(csvfile, fieldnames = fieldnames, delimiter=',')
	for row in theReader:
		print row['soundNumber'], row['response']
		v.fetch_voice(row['response'], row['soundNumber'])
