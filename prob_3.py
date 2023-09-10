# Write a prgram that prints out a diamond shape made of alternating #'s and _'s that looks like:
#                        #
#                       #_#
#                      #_#_#
#                       #_#
#                        #
	
# Your program should accept a positive integer as input and print a checkerboard diamond with that many rows.
# In the example shown, the number of rows is five. Your program should work for even and odd numbers.

user_input = 0
while True:
    user_input = input('insert positive integer')
    user_input = int(user_input)
    if user_input > 0:
        break
    
is_even = not(user_input % 2)
spaces = 0
for i in range(1, user_input + 1):
    spaces = abs(user_input // 2 - i + 1)
    if i <= (user_input // 2):
        pattern = '#' + ('_#' * (i - 1))
    else:
        pattern = '#' + ('_#' * (user_input - i))
        if(is_even):
            spaces = abs(user_input // 2 - i)

    print(' ' * spaces + pattern)

        
    
