# Write a program to read in a list of non-zero integers. 
# The user inputs a zero to indicate end of input. 
# The program then prints the average of all the numbers and the difference 
# between the largest number and the smallest number entered. 
# There should be no maximum number of integers in the list. Do not use built-in max, min, or average functions.

#References used:
#   - https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string | guide to replace function in python
#   - https://www.w3schools.com/python/ref_string_split.asp | guide to split function in python

user_inputs = input('please insert a list of numbers. Seperate numbers by comma. Conclude the list with 0')
#remove whitespace
user_inputs = user_inputs.replace(' ', '')
#convert string into list
input_list = user_inputs.split(',')

#variables to hold min, max, avg
min = int(input_list[0])
max = int(input_list[0])
avg = 0

for input in input_list:
    input = int(input)
    if input == 0:
        break

    avg = input + avg

    if min > input:
        min = input

    
    if max < input:
        max = input

avg = avg/(len(input_list) - 1)

print(f'avg is {avg}. Diff between max and min is {max-min}')


