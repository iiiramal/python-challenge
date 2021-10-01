
#
import os
import csv

#Declare CVS Path
csvpath = os.path.join(os.getcwd(),'Python Challenge', 'PyPoll','Resources','election_data.csv')
printpath = os.path.join(os.getcwd(),'Python Challenge','PyPoll','Analysis','PollAnalysis.text')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Declare Variables: Votes to tally totals, candidates as list, Tally as list to count individual candidate votes, and Tally Dictionary to calc Max. 
    Votes = 0
    Candidates = []
    Tally = []
    TallyDict = {}

    #Loop through csv file to tally votes and create candidate list. 
    for row in csvreader:

        #Total = Total + int(row[1])
        Votes = Votes + 1

        Tally.append(row[2])
        if row[2] not in Candidates:
            Candidates.append(row[2])

    #declare new variables
    TallyLoopList = len(Candidates)
    TallyLoop = len(Tally)
    printlist = []

    #loop through candidate list, looping through tally list to count individual votes
    for i in range(TallyLoopList):
        TallyCount = 0
        for j in range(TallyLoop):
            if Tally[j] == Candidates[i]: 
                TallyCount = TallyCount + 1

        #Calculate Percent of votes each candidate earned. 
        TallyPercent = "{:.2%}".format(TallyCount/Votes)  

        #Add Candidate, Tally % and Tally Count to list for future printing
        printlist.append(f'{Candidates[i]}: {TallyPercent} ({TallyCount})') 
        TallyDict[Candidates[i]] = [TallyCount]

    #Calculate winner and assigning name
    winnervote = max(TallyDict.items(), key=lambda x : x[1])
    winner = winnervote[0]
    
    #Print to Terminal

    print(f'Election Results \n------------------------- \nTotal Votes: {Votes} \n-------------------------')
    for i in range (len(printlist)):
        print(printlist[i])
    print(f'------------------------- \nWinner: {winner} \n-------------------------')

    #Print to .text
    f = open(printpath, 'w')
    f.write(f'Election Results \n------------------------- \nTotal Votes: {Votes} \n-------------------------')
    for i in range (len(printlist)):
        f.write(f'\n{printlist[i]}')
    f.write(f'\n------------------------- \nWinner: {winner} \n-------------------------')
    
   
