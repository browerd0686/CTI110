#A brief description
#Date
#CTI-110 P2HW2 - Meal Tip Calculator
#Your Name
#
print('Meal Tip Calculator Project')
print('June 21, 2019')
print('CTI - 110 P2HW2 - Meal Tip Calculator')
print('Darrius Brower')
#
#Input the original price for the food
#Calculate total original price by 15%
#Calculate total original price by 18%
#Calculate total original price by 20%
#Display the total tip price of 15%
#Display the total tip price of 18%
#Display the total tip price of 20%
      
#Get the charge for the food.
original_price = float(input("Enter the charge for the food: "))

#Get the amount of tip for 15%
tip_1 = original_price * .15

#Get the amount of tip for 18%
tip_2 = original_price * .18

#Get the amount of tip for 20%
tip_3 = original_price * .20

print('The amount of the 15% tip is: ', format(tip_1, '.2f'))
print('The amount of the 18% tip is: ', format(tip_2, '.2f'))
print('The amount of the 20% tip is: ', format(tip_3, '.2f'))
