#import dependencies
import os
import csv

#Declare CSV Path
#csvpath = os.path.join('/Users','alamar','Desktop','GitHub', 'Python Challenge', 'PyBank','Resources','budget_data.csv')
csvpath = os.path.join(os.getcwd(),'PyBank','Resources','budget_data.csv')
printpath = os.path.join(os.getcwd(),'PyBank','Analysis','BankAnalysis.text')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    Months, Total = [], []
    for row in csvreader:

        #Total = Total + int(row[1])

        if row[0] not in Months:
            Months.append(row[0])
        if row[1] not in Total:
            Total.append(int(row[1]))

change = []
end = (len(Total)-1)
for i in range(end):
    change.append(Total[i+1]-Total[i])

changedict = {}
for i in range(end):
    changedict[Months[i+1]] = change[i]

TotalMonths = str(len(Months))
TotalSum = str(sum(Total))
AvgChng = (Total[len(Total)-1]-Total[0])/(len(Total)-1)
AvgChngRnd = str(round(AvgChng,2))

#find greatest increase/decrease
changedictmax = max(changedict.items(), key=lambda x : x[1])
changedictmin = min(changedict.items(), key=lambda x : x[1])

#Assign month to Greates Increase/decrease.
maxwithmonth = changedictmax[0] + ' ($' + str(changedictmax[1]) + ')'
minwithmonth = changedictmin[0] + ' ($' + str(changedictmin[1]) + ')'

#print to terminal
print(f'Financial Analysis \n---------------------------- \nTotal Months: {TotalMonths} \nTotal: ${TotalSum} \nAverage Change: ${AvgChngRnd} \nGreatest Increase in Profits: {maxwithmonth} \nGreatest Decrease in Profits: {minwithmonth}')

#print to .text file
f = open(printpath,"w")
f.write('Financial Analysis' + '\n' + '----------------------------' + '\nTotal Months: ' + TotalMonths + '\nTotal: $' + TotalSum + '\nAverage  Change: $' + AvgChngRnd + '\nGreatest Increase in Profits: ' + maxwithmonth + '\nGreatest Decrease in Profits: ' + minwithmonth)
