import os
import csv
totMonths=0
totRevenue=0
gIncMo=""
gIncRev=0
gDecMo=""
gDecRev=0
csvpath1 = os.path.join("raw_data", "budget_data_1.csv")
csvpath2 = os.path.join("raw_data", "budget_data_2.csv")

with open(csvpath1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    firstline=True
    for row in csvreader:
        if firstline:
            firstline = False
            continue
        if(int(row[1])>int(gIncRev)):
            gIncMo=row[0]
            gIncRev=row[1]
        if(int(row[1])<int(gDecRev)):
            gDecMo=row[0]
            gDecRev=row[1]
        totRevenue = totRevenue + int(row[1])
        totMonths=totMonths+1

with open(csvpath2, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    firstline=True
    for row in csvreader:
        if firstline:
            firstline = False
            continue
        if(int(row[1])>int(gIncRev)):
            gIncMo=row[0]
            gIncRev=row[1]
        if(int(row[1])<int(gDecRev)):
            gDecMo=row[0]
            gDecRev=row[1]
        totRevenue = totRevenue + int(row[1])
        totMonths=totMonths+1

avgRevChange=round(totRevenue/totMonths,2)
print("\nFinancial Analysis")
print("-----------------------")
print("Total Months: "+str(totMonths))
print("Total Revenue: $"+str(totRevenue))
print("Average Revenue Change: $"+str(avgRevChange))
print("Greatest Increase in Revenue: "+str(gIncMo)+" ("+str(gIncRev)+")")
print("Greatest Decrease in Revenue: "+str(gDecMo)+" ("+str(gDecRev)+")")