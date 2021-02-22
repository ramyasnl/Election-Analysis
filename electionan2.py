# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
#1:Create a county list and county votes dictionary

county_options = []
county_votes = {}

#2:  Track the winning candidate, vote count, percentage, and largest county turnout.
winning_candidate = ''
winning_count = 0
winning_percentage = 0
largest_turnout_county = ''

# Open the election results and read the file and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        #3: Get the candidate name and county name from each row.
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #4a: If the county does not match any existing county, add the
        # the county list.
        if county_name not in county_options:
            #4b: Add the county name to the county list.
            county_options.append(county_name)
            #4c: And begin tracking that county's voter count.
            county_votes[county_name] = 0
        #5: Add a vote to that counties's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)
#6a:write a for loop to get the county from the county dictionary
    for county in county_votes:

        # 6b: Retrieve vote count and percentage.
        votes = county_votes[county]
        #6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        #6d: Print each county's voter count and percentage to the terminal.

        print(county_results)

        # 6e: Save the county results to our text file.
        txt_file.write(county_results)

        #6f: write an if statement to determine largest county vote count
        if (votes > winning_count) or (county == ''):
            winning_count = votes
            largest_turnout_county = county

    # 7:Print the counties's results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)

    #8: Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)

    winning_count = 0
#9:Save the final candidate vote count to the text file
    for candidate in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #10: Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #11: Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    #12: Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
