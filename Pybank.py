# import csv and os
import os
import csv

# set paths
Budget = os.path.join('','budget_data_2.csv')

with open('budget_data_2.csv', newline='') as csvfile1:

    reader = csv.reader(csvfile1, delimiter= ",")
    next(reader,None)
    months = []
    revenue = [] 
    change = []
   
    for row in reader:        
        revenue.append(float(row[1]))
        months.append(row[0])


for i in range(1,len(revenue)):
    change.append(revenue[i] - revenue[i-1])

avgchange = sum(change) / len(change)
maxchange = max(change)
minchange = min(change)
maxchangemonth = str(months[change.index(max(change))])
minchangemonth = str(months[change.index(min(change))])


txtfile = open("Pybank.txt","w")

txtfile.writelines("Financial Analysis")
txtfile.writelines("\n"+"------------------------")
txtfile.writelines("\n"+"Total Months"+ str(len(months)))
txtfile.writelines("\n"+"Total Revenue $"+ str(sum(revenue)))
txtfile.writelines("\n"+"------------------------")    
txtfile.writelines("\n"+"Average Change $"+ str(avgchange))
txtfile.writelines("\n"+"Greatest Increase $" + maxchangemonth + str(maxchange))
txtfile.writelines("\n"+"Greatest Decrease $" + minchangemonth + str(minchange))
txtfile.writelines("\n"+"------------------------")
