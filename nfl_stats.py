# open the csv file called "nfl_offensive_stats.csv" and read in the csv data from the file

import csv

nfl_stats = []

with open("nfl_offensive_stats.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        nfl_stats.append(row)

print(nfl_stats)

# In the data we just read in, the fourth column is the player and the 8th column is the passing yards. Get the sum of yards from column 8 where the 4th column value is "Aaron Rodgers"
# Aaron Rodgers is the 16th row

total = 0
for row in nfl_stats:
    if row[3] == "Aaron Rodgers":
        total += int(row[7])

print(total)

# the 3rd column in data is player position, the fourth column is the player, and the 8th column is the passing yards.For each player whose position in column 3 is "QB", determine the sum of yards from column 8

qb_yards = {}
for row in nfl_stats:
    if row[2] == "QB":
        if row[3] in qb_yards:
            qb_yards[row[3]] += int(row[7])
        else:
            qb_yards[row[3]] = int(row[7])

print(qb_yards)


# print the sum of the passing yards sorted by sum of passing yards in descending order

for player in sorted(qb_yards, key=qb_yards.get, reverse=True):
    print(player, qb_yards[player])
    
    
    