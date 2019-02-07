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

year = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
membership_numbers = [52, 48, 67, 45, 45, 50, 55, 67, 65, 70, 60, 60, 55, 60, 65, 75, 80]
plt.plot(year, membership_numbers, color='#9abd4b')
plt.xlabel('Year')
plt.ylabel('Memebership Numbers')
plt.title('Membership Numbers from 2002 to 2018')
plt.show()
