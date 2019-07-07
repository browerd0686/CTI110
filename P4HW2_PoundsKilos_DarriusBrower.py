#Pounds to Kilos Table Excercise
#July 7, 2019
#CTI-110 Pounds to Kilos Table
#Darrius Brower
#
#Create table with headings Pounds, Kilograms
#Enter Pounds and convert kilos
#kg = lb/2.2046
#Calculate
#
#Print the table headings.
print('Pounds\tKilograms')
print('-------------------')

for lb in range(100, 301, 10):
    kg = (lb/2.2046)
    print(lb, '\t', format(kg, '.2f'))
