#CTI-110
#P3HW2-MealTipTax
#Darrius Brower
#June 30, 2019
#
#Ask the user to enter the charge for the meal.
#Ask user to enter the tip percentage they would like to consider - 15%, 18%, 20%.
#Calcualte the tip and 7% sales tax.
#Display tip, tax, and total.
#
#
#Enter charge of meal.
meal = float(input('How much did your meal cost: '))
salesTax = .07 * meal
tip_1 = .15 * meal
tip_2 = .18 * meal
tip_3 = .20 * meal
Total_Cost_1 = meal + salesTax + tip_1
Total_Cost_2 = meal + salesTax + tip_2
Total_Cost_3 = meal + salesTax + tip_3
print('meal: $' + format( meal, '.2f'), 'tip_1: $' + format( tip_1, '.2f'), 'salesTax: $' + format( salesTax, ',.2f'), 'Total_Cost_1: $' + format( Total_Cost_1, ',.2f'))
print('meal: $' + format( meal, '.2f'), 'tip_2: $' + format( tip_2, '.2f'), 'salesTax: $' + format( salesTax, ',.2f'), 'Total_Cost_2: $' + format( Total_Cost_2, ',.2f'))     
print('meal: $' + format( meal, '.2f'), 'tip_3: $' + format( tip_3, '.2f'), 'salesTax: $' + format( salesTax, ',.2f'), 'Total_Cost_3: $' + format( Total_Cost_3, ',.2f'))
