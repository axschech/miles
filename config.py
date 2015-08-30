import json
try:
	from dateutil.relativedelta import relativedelta
except Exception, e:
	print "Please install python-dateutil"

import datetime

def write():
	f = open('config.json', 'w')
	f.seek(0)
	f.write("\n")

	print "\nSetup commencing. For numbers enter whole integers. For dates enter in the format YYYY/MM/DD \n"
	try:
		total_miles = int(raw_input('How many miles do you have total? \n'))
		per_month = int(raw_input('How many miles do you have per month? \n'))
		input_date = str(raw_input('What date did you start your lease? \n'))
		months = int(raw_input('How many months is your lease? \n'))
	except Exception, e:
		print "Something was entered incorrectly... terminating...\n"

	print "\n Calculating mileage per month... please wait... \n"
	try:
		dates = input_date.split('/')
		print dates
		date = datetime.date(int(dates[0]),int(dates[1]),int(dates[2]))
		print date
	except Exception, e:
		print e
		print "Incorrect date, terminating...\n"

	# for x in range(0, months):


def read():
	try:
	    f = open('config.json', 'r+')
	    text = f.read()
	    return json.loads(text)
	except Exception, e:
	    write()
