# Sum of Numbers Excercise
# July 8, 2019
# CTI-110 P4HW3 - Sum Of Numbers
# Darrius Brower
#
# Write program with a loop that asks for user to enter a series of positive numbers.
# The program should enter a negative number to end the program.
# Program should display the sum of positive numbers that you entered.
#
total = 0
userNumber = float( input('Please enter the first number or a negative ' + \
                          'number to quit: '))
while userNumber > -1:
     total = total + userNumber
     userNumber = float( input('Please enter the next number or a ' + \
                               'negative number to quit: ') )
print('The sum of all the numbers you entered is',total )
