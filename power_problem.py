'''
Use the power_data.csv file AND the zipcode database
to answer the questions below.  Make sure all answers
are printed in a readable format. (i.e. "The city with the highest electricity cost in Illinois is XXXXX."

The power_data dataset, compiled by NREL using data from ABB,
the Velocity Suite and the U.S. Energy Information
Administration dataset 861, provides average residential,
commercial and industrial electricity rates by zip code for
both investor owned utilities (IOU) and non-investor owned
utilities. Note: the file includes average rates for each
utility, but not the detailed rate structure data found in the
OpenEI U.S. Utility Rate Database.

This is a big dataset.
Below are some questions that you likely would not be able
to answer without some help from a programming language.
It's good geeky fun.  Enjoy

FOR ALL THE RATES, ONLY USE THE BUNDLED VALUES (NOT DELIVERY).  This rate includes transmission fees and grid fees that are part of the true rate.
'''

#1  What is the average residential rate for YOUR zipcode? You will need to read the power_data into your program to answer this.  (7pts)

import csv

#reading data in
file = open("power_data.csv", 'r')
power = []
reader = csv.reader(file, delimiter=',')
for line in reader:
    power.append(line)
print(power)

#making a list of all zip codes and of all the resedential rates
zip_list = []
res_list = []
for i in range(len(power)-1):
    zip = power[i][0]
    res = power[i][8]
    zip_list.append(zip)
    res_list.append(res)
#print(res_list)
#print(zip_list)

#finding index of specific zip code, and seeing what the res. rate using the same index
zip_index = zip_list.index('60614')
#print(zip_index)
print("the average residential rate in my zipcode is", res_list[zip_index])

#2 What is the MEDIAN rate for all BUNDLED RESIDENTIAL rates in Illinois? Use the data you extracted to check all "IL" zipcodes to answer this. (10pts)

illinois = []

#creating a list of illinois bundled res. rates
for i in range(len(power)-1):
    if power[i][3] == 'IL' and power[i][4] == 'Bundled':
        illinois.append(power[i])

sorted = []

for i in range(len(illinois)):
    sorted.append(illinois[i][8])

#sorting by res. rate
for pos in range(len(sorted)-1):
    min_pos= pos
    for scan_pos in range(min_pos, len(sorted)):
        if sorted[scan_pos] < sorted[min_pos]:
            min_pos = scan_pos
    temp = sorted[pos]
    sorted[pos] = sorted[min_pos]
    sorted[min_pos] = temp

median_place = len(sorted)//2
print("the median residential rate in Illinois is", sorted[median_place])

#3 What city in Illinois has the lowest residential rate?  Which has the highest?  You will need to go through the database and compare each value for this one. Then you will need to reference the zipcode dataset to get the city.  (15pts)

for pos in range(len(illinois)):
    min_pos= pos
    for scan_pos in range(min_pos, len(illinois)):
        if illinois[scan_pos][8] < illinois[min_pos][8]:
            min_pos = scan_pos
    temp = illinois[pos]
    illinois[pos] = illinois[min_pos]
    illinois[min_pos] = temp
#print(illinois)

#getting a list of all the cities with lowest/highest res. rates
lowest_res = illinois[0][8]
low = []
highest_res = illinois[-1][8]
high = []
for i in range(len(illinois)-1):
    if illinois[i][8] == lowest_res:
        low.append(illinois[i][0])
    if illinois[i][8] == highest_res:
        high.append(illinois[i][0])

#reading zip codes into list
file2 = open("free-zipcode-database-Primary.csv", 'r')
zip_codes = []
reader2 = csv.reader(file2, delimiter=',')
for line in reader2:
    zip_codes.append(line)



#going through zip code list and list of high/low res. rates and seeing what zip codes are in each list, and from there finding the city names.
abc = []
xyz = []
for i in range(len(zip_codes)-1):
    for j in range(len(low)):
        if low[j] == zip_codes[i][0]:
            abc.append(zip_codes[i][2])
    for k in range(len(high)):
        if high[k] == zip_codes[i][0]:
            xyz.append(zip_codes[i][2])


print("the cities with the lowest resedential rate are:", abc)
print("the cities with the highest resedential rate are:", xyz)



#FOR #4  CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS. The first one is easier than the second.
#4  (Easier) USING ONLY THE ZIP CODE DATA... Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.  Make the marker size vary depending on the population contained in that zip code.  Add an alpha value to the marker so that you can see overlapping markers.



import matplotlib.pyplot as plt
import random


xval = []
yval = []
color_list = []
size_list = []

#adding all the longitudes and lattitudes to lists
new = zip_codes[1:]
for i in range(len(new)-1):
    xval.append(str(new[i][5]))
    yval.append(new[i][6])

#setting the size so higher population will be bigger
    try:
        size = float(new[i][10]) / 75
    except:
        size = 35

    size_list.append(size)

my_scatterplot = plt.scatter(xval, yval, s = size_list)  #the color and size at the back are how you set the color and size





#4 (Harder) USING BOTH THE ZIP CODE DATA AND THE POWER DATA... Make a scatterplot of all zip codes in Illinois according to their Lat/Long.  Make the marker red for the top 25% in residential power rate.  Make the marker yellow for the middle 25 to 50 percentile. Make the marker green if customers pay a rate in the bottom 50% of residential power cost.  This one is very challenging.  You are using data from two different datasets and merging them into one.  There are many ways to solve. (20pts)


