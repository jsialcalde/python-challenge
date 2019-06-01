# import modules 
import csv
import os

# create file path
csvpath = os.path.join( 'Resources', 'election_data.csv')


# initiate total number of votes cast
vote_total  = 0
# initiate dictionary of candidates and votes per candidate
candidates = {}

# open file
with open(csvpath, newline="", mode='r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    # skip header
    csv_header = next(election_data)

    for row in election_data:
        candidate = row[2]

        # if candidate is not in candidate dictionary add candidate and vote
        if candidate not in candidates:
            candidates[candidate]=1
        # otherwise add vote to appropriate candidate
        else:
            candidates[candidate]+=1
        # add to vote
        vote_total += 1

print('\n')
print('Election Results')
print('-----------------------------')
print(f'Total Votes: {vote_total}')
print('-----------------------------')

# print and calculate votes, % of votes each candidate won by iterating through candidate dictionary
winner = {}
votes = 0
for candidate in candidates:
    # determine the winner based on popular vote
    if (candidates[candidate] > votes):
        winner[candidate]= candidate
    votes = candidates[candidate]
    vote_percentage = '{0:.3f}'.format((votes*100/vote_total))
    print(f'{candidate}: {vote_percentage}% ({votes})')

print('-----------------------------')

for key in winner:
    print(f'Winner: {key}')
print('-----------------------------')




# Specify the file to write to
output_path = os.path.join("output", "election_summary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')

    # Write the summary
    csvwriter.writerow('Election Results')
    csvwriter.writerow('\n')
    csvwriter.writerow('Election Results')
    csvwriter.writerow('-----------------------------')
    csvwriter.writerow(f'Total Votes: {vote_total}')
    csvwriter.writerow('-----------------------------')

    votes = 0
    for candidate in candidates:
    # determine the winner based on popular vote
        if (candidates[candidate] > votes):
            winner[candidate]= candidate
        votes = candidates[candidate]
        vote_percentage = '{0:.3f}'.format((votes*100/vote_total))
        csvwriter.writerow(f'{candidate}: {vote_percentage}% ({votes})')

    csvwriter.writerow('-----------------------------')

    for key in winner:
        csvwriter.writerow(f'Winner: {key}')
    csvwriter.writerow('-----------------------------')
