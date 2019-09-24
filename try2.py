import csv


exampleFile = open('5rows.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
	print(row)