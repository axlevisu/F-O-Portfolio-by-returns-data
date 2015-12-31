import csv
import sys
import math

portfolio={}
def transpose(alist):
	return map(list, zip(*alist))

# Read and store in 2D Array
datafile = open(sys.argv[1],'r')
# datafile = open("2006d.csv",'r') for example
datareader = csv.reader(datafile, delimiter =",")
data=list(datareader)
del data[0:5]

for i in xrange(0,len(data)):
	for j in xrange(1,len(data[i])):
		try:
			data[i][j] = float(data[i][j])
		except:
			data[i][j] = 0.0

for j in xrange(1,5):
	ret=[]
	companies_for_removal=[]
	data1=data
	for company in data1:
		try:
			var=1/company[5]
			ret.append((company[5]-company[5-j])/company[5-j])
		except:
			companies_for_removal.append(company)
	for company in companies_for_removal:
		data1.remove(company)
	data1=transpose(data1)
	data1.append(ret)
	data1=transpose(data1)
	data1 = sorted(data1, key = lambda x: x[-1])
	bottom_decile =[i for j,i in enumerate(data1) if j in range(0,int(math.floor(len(data1)/10)))]
	top_decile =[i for j,i in enumerate(data1) if j not in range(0,int(math.ceil(9*len(data1)/10)))]
	portfolio[j]=[top_decile,bottom_decile]
	ret1=[]
	for k in xrange(1,5):
		tret,bret=0,0
		for company in portfolio[j][0]:
			tret+=(company[5+k]-company[5])/company[5]
		tret=tret/len(portfolio[j][0])

		for company in portfolio[j][1]:
			bret+=(company[5+k]-company[5])/company[5]
		bret=bret/len(portfolio[j][1])
		ret1.append(100*(tret-bret))
	portfolio[j].append(ret1)
	print portfolio[j][2]

