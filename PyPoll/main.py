import os
import csv

csvpath = os.path.join('.','election_data.csv')
outputpath = os.path.join('.','result.txt')
open(outputpath,'w')

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    namelist = []
    name = []
    count = []
    winner = ''
    tmp = 0
    for line in csvreader:
        namelist.append(line[2])
    votes = (csvreader.line_num)-1
    for i in range(len(namelist)):
        if name.count(namelist[i]) == 0:
            name.append(namelist[i])
    output = open(outputpath,'w+')
    print("Election Results")
    print >> output, "Election Results"
    print("-----------------------------")
    print >> output, "-----------------------------"
    print("Total Votes: %d" %votes)
    print >> output, "Total Votes: %d" %votes
    print("-----------------------------")
    print >> output, "-----------------------------"
    for voteename in name:
        print("%s: %.2f%% (%d)" %(voteename, namelist.count(voteename)*100/votes,namelist.count(voteename)))
        print >> output, "%s: %.2f%% (%d)" %(voteename, namelist.count(voteename)*100/votes,namelist.count(voteename))
        count.append(namelist.count(voteename))
    print("-----------------------------")
    print >> output, "-----------------------------"
    for i in range(len(count)):
        if tmp < count[i]:
            winner = name[i]
            tmp = count[i]
    print("Winner: %s" %winner)
    print >> output, "Winner: %s" %winner
    print("-----------------------------")
    print >> output, "-----------------------------"
    output.close()
