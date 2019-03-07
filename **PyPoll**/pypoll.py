import os
import csv

# Path to collect data 
data = os.path.join('.', 'election_data.csv')

# Read in the CSV file
with open(data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    
#   create variables
    totalvotes = 0
    Khan = 0
    Correy = 0
    Li = 0
    Tooley = 0 
    
#   read each row of data
#  calculate total votes & total vote percent
    for row in csvreader:
        totalvotes += 1
        if row[2] == "Khan":
            Khan += 1
            khanpercent = (Khan/totalvotes)
        if row[2] == "Correy":
            Correy += 1 
            Correypercent = (Correy/totalvotes)
        if row[2] == "Li":
            Li += 1
            Lipercent = (Li/totalvotes)
        if row[2] == "O'Tooley":
            Tooley += 1
            Tooleypercent = (Tooley/totalvotes)
combination = [Khan, Correy, Li, Tooley]   
maximum = max(combination)

#determine winner
if maximum == Khan:
    winner = "Khan"
if maximum == Correy:
    winner = "Correy"
if maximum == Li:
    winner = "Li"
if maximum == Tooley:
    winner = "O'Tooley"
    
#chance format to percent
kpercent = "{:.3%}".format(khanpercent)
cpercent = "{:.3%}".format(Correypercent)
lpercent = "{:.3%}".format(Lipercent)
opercent = "{:.3%}".format(Tooleypercent)

# print ("Election Results")
# print ("Total Votes: ", totalvotes)
# print("Khan:","{:.3%}".format(khanpercent),"(",Khan,")")
# print ("Correy:","{:.3%}".format(Correypercent), "(" ,Correy, ")")
# print ("Li:","{:.3%}".format(Lipercent), "(" ,Li, ")")
# print ("O'Tooley:","{:.3%}".format(Tooleypercent), "(" ,Tooley, ")")
# print ("Winner:",winner)


# combine all data
data = ("Election Results \n"+ "------------------------ \n"+ 
        f"Total Votes: {totalvotes}\n"+ "------------------------ \n"+ 
        f"Khan: {kpercent} ({Khan})\n"+ f"Correy: {cpercent} ({Correy})\n" + 
        f"Li: {lpercent} ({Li})\n" + f"O Tooley: {opercent} ({Tooley})\n" + 
        "------------------------ \n"+ f"Winner: {winner}\n" + 
        "------------------------ \n")
    
print (data)

# export to text file
output_file_path = os.path.join('.', 'result2.txt')
with open(output_file_path, 'w') as resultfile:
        resultfile.write(data)