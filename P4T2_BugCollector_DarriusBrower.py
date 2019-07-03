#Bug Collector Excercise
#July 3, 2019
#CTI-110 P4T2 - Bug Collector
#Darrius Brower
#
#set total = 0
#for each of seven days
#Input bugs collected for a day
#Add bugs collected to total
#Display total
#
#Initialize the accumulator
total = 0
#Get the bugs collected for each day
for day in range(1, 8):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total = total + bugs
#Display the total bugs.
    print('You collected a total of', total, 'bugs.') 
    
