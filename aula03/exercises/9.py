#função que define um no bissexto
def isLeapYear(year):
	if (year % 4 == 0 and ((year % 100 == 0 and year % 400 == 0) or (year % 100 != 0))):
		return True
	else:
		return False 

# A table with the days in each month.
# For example: MONTHDAYS[3] is the number of days in March.
MONTHDAYS__COMMON = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MONTHDAYS__LEAP = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

#função que define os dias dos meses de um ano, caso ele seja bissexto ou não
def monthDays(year, month):
	if (isLeapYear(year) == True):
		days = MONTHDAYS__LEAP[month]
	else:
		days = MONTHDAYS__COMMON[month]
		
	return days
    
#função que define que, se o dia do mês for igual ao ultimo dia daquele mês, salta para um mês seguinte
def nextDay(year, month, day):
	num_days = monthDays(year, month)
	if (day == num_days):
		day = 1
		if (month == 12):
			month = 1
			year = year + 1
		else:
			month += 1
	else: 
		day += 1

	return year, month, day


# This is the main function
def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?

# call the main function
main()
# This function checks if year is a leap year.
def isLeapYear(year):
	if (year % 4 == 0 and ((year % 100 == 0 and year % 400 == 0) or (year % 100 != 0))):
		return True
	else:
		return False
		
		
# For example: MONTHDAYS[3] is the number of days in March.
MONTHDAYS_COMMON = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MONTHDAYS_LEAP = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def monthDays(year, month):
	if (isLeapYear(year) == True):
		days = MONTHDAYS_LEAP[month]
	else:
		days = MONTHDAYS_COMMON[month]
		
	return days
	

def nextDay(year, month, day):
	num_days = monthDays(year, month)
	
	if (day == num_days):
		day = 1
		if (month == 12):
			month = 1
			year = year + 1
		else:
			month += 1
	else:
		day += 1
    
	return year, month, day


def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?

# call the main function
main()