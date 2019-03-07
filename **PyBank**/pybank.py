import os
import csv

# Path to collect data 
data = os.path.join('.', 'budget_data.csv')

# Read in the CSV file
with open(data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    
#   create variables
    total_months = 0
    total = 0
    previousProfitValue = 0
    maxProfitIncrease = 0
    profitChange = 0
    minProfitDecrease = 0
    nettotal = 0
    totalmonths = 0
    highest = 0
    lowest = 0
    previousvalue = 0
    profitchange = 0
    avevalue = 0
    average = []
    
#   read each row of data
    for row in csvreader:
        date = str(row[0])
        value = int(row[1])
        
#       calculate total months,net total, and average change
#       calculate gretest decrease and greatest increase
        nettotal += value
        totalmonths += 1
        profitincrease = value-previousvalue
        profitdecrease = int(previousvalue)-int(value)
        averageindi = (value - avevalue)
        average.append(averageindi)
        avevalue = int(row[1])
        totalave = (((sum(average)-(867884))/85))
        if highest < profitincrease:
            highest = profitincrease
            namehighest = date
        if lowest < int(profitdecrease):
            lowest = int(profitdecrease)
            namelowest = date
        previousvalue = value
        
#       change format to currency
        highestdata = "${:.0f}".format(int(highest))
        lowestdata = "$-{:.0f}".format(int(lowest))
        totalnet = "${:.0f}".format(nettotal)
        averagetotal = "${:.2f}".format(totalave)

        
# print ("Financial Analysis")
# print ("Total Months:",totalmonths)
# print ("Total:",totalnet)
# print ("Average Change:", averagetotal)
# print ("Greatest Increase in Profits:",namehighest,highestdata)
# print ("Greatest Decrease in Profits:",namelowest,lowestdata)

# combine all data
data = ("Financial Analysis \n"+ "------------------------ \n"+ 
        f"Total Months: {totalmonths}\n"+ f"Total: {totalnet}\n"+ 
        f"Average Change: {averagetotal}\n" + f"Greatest Increase in Profits: {namehighest} {highestdata}\n" + 
        f"Greatest Increase in Profits: {namelowest} {lowestdata}\n")
print (data)

# export to text file
output_file_path = os.path.join('.', 'result.txt1')
with open(output_file_path, 'w') as resultfile:
        resultfile.write(data)