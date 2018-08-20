#\Rutgers\Homework\Due 8-25\Resources

import os
import csv
import operator

filename = os.path.join("../../../", "Rutgers", "Homework", "Due 8-25", "Resources", "election_data.csv")

with open(filename, "r") as poll_infile:
    csv_reader = csv.reader(poll_infile, delimiter= ",")
    next(csv_reader, None) #skip the headers

    #store all the records into a list for manipulation
    #columns
    #Voter ID	County	Candidate
    all_votes = [vote for vote in csv_reader]

    #store total votes
    total_votes = len(all_votes)

    #get the unique list of candidates and store their vote counts in a dictionary
    candidate_list = {}
    for vote in all_votes:
        if vote[2] not in candidate_list:
            candidate_list.update({vote[2]:0})
        candidate_list[vote[2]] += 1

    #format output for printing to screen and file
    #headers
    results = []
    results.append("--------------------------------------------")
    results.append("Total Votes: " + str(total_votes))
    results.append("--------------------------------------------")

    #compile the individual line results
    results2 = [candidate + ":  " + str(votes) + " Votes ({:.{}f}".format((votes/total_votes) * 100,2) + "%)" for candidate, votes in candidate_list.items()]
    for result in results2:
        results.append(result)
    
    # the winner
    results.append("--------------------------------------------")
    results.append("The winner: " + max(candidate_list.items(), key=operator.itemgetter(1))[0])
    results.append("--------------------------------------------")

    # print to screen
    for result in results:
        print(result)

    #write the results to a file
    filename = os.path.join("./", "results-file.txt")
    poll_outfile = open(filename, "w")

    #write to the file similar to the terminal output, but adding new line characters
    for result in results:
        poll_outfile.write(result + "\n")

    poll_outfile.close()
    
  
    


