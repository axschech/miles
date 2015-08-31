import json
import datetime

def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)

def write():
	f = open('config.json', 'w')
	f.seek(0)
	f.write("\n")

	print "\nSetup commencing. For numbers enter whole integers. For dates enter in the format YYYY/MM/DD \n"
	try:
		total_miles = int(raw_input('How many miles do you have total? \n'))
		input_date = str(raw_input('What date did you start your lease? \n'))
		months = int(raw_input('How many months is your lease? \n'))
		per_month = total_miles / months
		print per_month
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

	year_num = int(date.year);
	month_num = int(date.month)
	obj = {
		'total_miles': total_miles,
		'miles_map': {
			year_num: {
				month_num: per_month
			}
		}
	}
	current_miles = 0
	for x in range(0, months):

		current_miles = current_miles + per_month
		if month_num > 12:
			month_num = 1
			year_num = year_num + 1
			obj['miles_map'][year_num] = {
				month_num = current_miles
			}
		else:
			month_num = month_num + 1
		obj['miles_map'][year_num][month_num] = current_miles
	print obj

def read():
	try:
	    f = open('config.json', 'r+')
	    text = f.read()
	    return json.loads(text)
	except Exception, e:
	    write()
