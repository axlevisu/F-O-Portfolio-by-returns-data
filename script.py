import urllib2
import time
from bs4 import BeautifulSoup
from datetime import date
from dateutil.relativedelta import relativedelta
import csv
import sys
#Gets data from yahoos-finance
#for time being let consider trading on July 1
def get_args(a):
	return map(int,a.split('/'))

TD = "07/01/2014"# "Jul 01 2015" #Trading date
a=get_args(TD)
# .strftime("%m/%d/%y")
td = date(a[2],a[0],a[1])
data_class ="yfnc_tabledata1"
base_url = "http://finance.yahoo.com/q/hp?s="
# fo_list = open(sys.argv[1],'r').read().splitlines()
fo_list = open('2014.csv','r').read().splitlines()
del fo_list[0]
Js =range(1,5)
Ks =range(1,5)
portfolio ={}
curr_price =[]
for company in fo_list:
	url = base_url+company+".NS&a="+str(a[0]-1)+"&b="+str(a[1])+"&c="+str(a[2])+"&d="+str(a[0]-1)+"&e="+str(a[1])+"&f="+str(a[2])
	page=urllib2.urlopen(url).read()
	soup = BeautifulSoup(page,'html.parser')
	try:
		print company,float(soup.findAll('td',{'class':'yfnc_tabledata1','align':'right'})[-1].string)
	except:
		pass
	# curr_price.append(float(soup.findAll('td',{'class':'yfnc_tabledata1','align':'right'})[-1].string))
print curr_price
# for j in Js:
	# p_date = get_args((td +relativedelta(months=-3*j)).strftime("%m/%d/%y"))
	# portfolio[j]=[]
	# for company in fo_list:

		# portfolio[j].append()
	# for k in Ks:
		# r_date = td + relativedelta(months = +3*k)  
		# for company in fo_list:

