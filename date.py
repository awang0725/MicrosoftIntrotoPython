from datetime import datetime,timedelta
# this error message is coming from pylint is not supporting python 3.6
# if you run it under python 3.5 then it is fine.
# this information is from stackOverflow

current_time = datetime.now()

print('Current time is:' + str(current_time))

one_day = timedelta(days=1)
today = current_time
yesterday = current_time - one_day

print(f'Today is ', today ,'\nYesterday is ',yesterday)

print('This is year: ' + str(current_time.year))
print('Month: ' + str(current_time.month))
print('Date: ' + str(current_time.day))

birthday = input('Input your birthday (dd/mm/yyyy) : ')
birthday_date = datetime.strptime(birthday,'%d/%m/%Y')

print('Your birthday is : ',str(birthday_date))