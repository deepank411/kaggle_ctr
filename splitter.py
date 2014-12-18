import csv
ifile = open('train.csv',"rb")
reader = csv.reader(ifile)
ofile1 = open('traintrain.csv', "wb")
ofile2 = open('traintest.csv', "wb")
writer1 = csv.writer(ofile1)
writer2 = csv.writer(ofile2)
count = 0
while (count<32000000):
	for row in reader:
		writer1.writerow(row)
		count += 1
else:
	for row in reader:
		writer2.writerow(row)

ifile.close()
ofile1.close()
ofile2.close()
	

