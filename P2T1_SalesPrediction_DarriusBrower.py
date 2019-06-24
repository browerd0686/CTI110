first_name = 'Darrius'
last_name = 'Brower'
brief_description = 'Sales Prediction Project'
date = 'June 17, 2019'
course = 'CTI-110 P2T1 - Sales Prediction'
print(brief_description)
print(date)
print(course)
print(first_name, last_name)

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
