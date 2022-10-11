# The data we need to retrieve
#The total number of votes cast
#The percentage of votes each candidate won
#The total number of votes each canditate won
#The winner of the election based on popular vote.
# Open the election results and read the file.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

#Read the file object with the reader function.


# Print the header row
       file_reader=csv.reader(election_data)
       #for row in file_reader:
          # print(row)
#Read the file object with the reader function.
       headers = next(file_reader)
       print(headers)
  # To do: read and analyze the data here