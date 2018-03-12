import os
import csv

totVotes=0
candidates=[]
votes=[]
winner=""
curVotes=0

csvpath1 = os.path.join("raw_data", "election_data_1.csv")
csvpath2 = os.path.join("raw_data", "election_data_2.csv")

with open(csvpath1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    firstline=True
    for row in csvreader:
        if firstline:
            firstline = False
            continue
        if(str(row[2]) in candidates):
            x=candidates.index(str(row[2]))
            votes[x]=votes[x]+1
        else:
            candidates.append(str(row[2]))
            votes.append(1)
        totVotes = totVotes+1
with open(csvpath2, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    firstline=True
    for row in csvreader:
        if firstline:
            firstline = False
            continue
        if(str(row[2]) in candidates):
            x=candidates.index(str(row[2]))
            votes[x]=votes[x]+1
        else:
            candidates.append(str(row[2]))
            votes.append(1)
        totVotes = totVotes+1
      
print("\nElection Results")
print("-----------------------------")
print("Total Votes: "+str(totVotes))
print("-----------------------------")
i=0
while i < len(candidates):
    votePerc=round((votes[i]/totVotes)*100,1)
    print(str(candidates[i])+": "+str(votePerc)+"% ("+str(votes[i])+")")
    if(votes[i]>curVotes):
        curVotes=votes[i]
        winner=candidates[i]
    i+=1

print("-----------------------------")
print("Winner: "+str(winner))
print("-----------------------------")