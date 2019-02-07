import csv
import matplotlib.pyplot as plt
import numpy as np

categories = []
year = []

with open('data/traa_data.csv', encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		

# data to plot
komoka = (15, 14, 23)
oxbow = (10, 18, 12)
dingman = (13, 15, 14)

# create plot
fig, ax = plt.subplots()
n_groups = 3
index = np.arange(n_groups)
bar_width = 0.30
opacity = 0.8
 
rects1 = plt.bar(index, komoka, bar_width, alpha=opacity, color='#5d7132', label='Komoka')
 
rects2 = plt.bar(index + bar_width, oxbow, bar_width, alpha=opacity, color='gold', label='Oxbow')

rects2 = plt.bar(index + bar_width + bar_width, dingman, bar_width, alpha=opacity, color='#9abd4b', label='Dingman')
 
plt.xlabel('Years')
plt.ylabel('Numbers')
plt.title('Numbers of Rainbow Trout Caught at Different Creek from 2016 to 2018')
plt.xticks(index + bar_width, ("2002", "2006", "2010", "2014"))
plt.legend()
 
plt.tight_layout()
plt.show()