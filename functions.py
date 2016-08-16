def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if day > 0 and day <=31:
			return day

months =['January','February','March']	

def valid_month(month):
	if month:
		month = month.capitalize()
		if month in months:
			return month

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year > 1900 and year <=2016:
			return year			