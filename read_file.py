import csv
reader = csv.reader(open("NelisaSalesHistory.csv","rbU"), delimiter=";")   
for row in reader:    
	print row[2], row[3]
