import os
import csv

csvpath = os.path.join('.','budget_data.csv')
outputpath = os.path.join('.','result.txt')
open(outputpath,'w')

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    total = 0
    date1 = ''
    date2 = ''
    max = 0
    maxdiff = 0
    min = 0
    mindiff = 0
    tmp = 0
    totaldiff = 0
    diff = 0
    for line in csvreader:
        total += int(line[1])
        if tmp !=0:
            diff = int(line[1])-tmp
        totaldiff +=diff
        if(int(line[1])>max):
            max = int(line[1])
            maxdiff = diff
            date1 = line[0]
        if (int(line[1]) < min):
            min = int(line[1])
            mindiff = diff
            date2 = line[0]
        tmp = int(line[1])
    months = (csvreader.line_num)-1
    average = totaldiff/(months-1)
    output = open(outputpath, 'w+')
    print("Financial Analysis")
    print >> output,"Financial Analysis"
    print("-----------------------------")
    print >> output, "-----------------------------"
    print("Total Months: %d" %months)
    print >> output, "Total Months: %d" %months
    print("Total: $%d" %total)
    print >> output, "Total: $%d" %total
    print("Average Change: $%.2f" %average)
    print >> output, "Average Change: $%.2f" %average
    print("Greatest Increase in Profits: %s (%d)" %(date1,maxdiff))
    print >> output, "Greatest Increase in Profits: %s (%d)" %(date1,maxdiff)
    print("Greatest Increase in Profits: %s (%d)" % (date2, mindiff))
    print >> output, "Greatest Increase in Profits: %s (%d)" % (date2, mindiff)
    output.close()


