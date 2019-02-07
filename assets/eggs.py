import csv
import matplotlib.pyplot as plt
import numpy as np

categories = []
rainbow = []
brown = []

with open('data/traa_data.csv', encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[0] == "Rainbow Trout":
			rainbow.append([row[0], int(row[1]), row[3]])
			line_count += 1
		elif row[0] == "Brown Trout":
			brown.append([row[0], int(row[1]), row[3]])

totalRainbow = int(80000 + 120000 + 90000 + 40000 + 140000)
totalBrown = int(70000 + 70000 + 70000 + 70000 + 90000)

print("Total number of Rainbow Trout eggs hatched/released:", totalRainbow)
print("Total number of Brown Trout eggs hatched/released:", totalBrown)

totalEggs = totalRainbow + totalBrown

rainbow_percentage = int(totalRainbow / totalEggs * 100)
brown_percentage = int(totalBrown / totalEggs * 100)

# chart one
labels = "Rainbow Trout", "Brown Trout"
sizes = [rainbow_percentage, brown_percentage]
colors = ["#5d7132", "#9abd4b"]
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Eggs hatched/released from TRAA - Rainbow Trout VS Brown Trout")
plt.xlabel("Total number of eggs hatched/released from 2014 to 2018")
plt.show()