# Write a program that finds the number of days between two dates in the same year. 
# The user inputs one date, presses the return key, then enters another date. 
# The input is of the form "Month day", for example, Jul 4 or Oct 31.
# Do not use built-in date parsing functions. Write the algorithm yourself.

days_in_year = 365
days_in_each_month = [31,28,31,30,31,30,31,31,30,31,30,31]
month_to_num = {
    'Jan': 0,
    'Feb': 1,
    'Mar': 2,
    'Apr': 3,
    'May': 4,
    'Jun': 5,
    'Jul': 6,
    'Aug': 7,
    'Sep': 8,
    'Oct': 9,
    'Nov': 10,
    'Dec': 11
}

first_date = input('please insert a date in the following format: Month day, e.g. Dec 12')
second_date = input('please insert a date in the following format: Month day, e.g. Jul 12')

first_month, first_day = first_date.split(' ')
second_month, second_day = second_date.split(' ')

try:
    first_month = month_to_num[first_month]
    first_day = int(first_day)

    second_month = month_to_num[second_month]
    second_day = int(second_day)
except:
    print('the values you inserted were not properly formatted')

#convert dates into numbers between 1 and 365
first_val = 0
second_val = 0
for i in days_in_each_month[:first_month]:
    first_val += i
first_val += first_day
for i in days_in_each_month[:second_month]:
    second_val += i
second_val += second_day

print(f'days between {first_val} {second_val}: {second_val - first_val if first_val < second_val else 365 - (first_val - second_val)}')
