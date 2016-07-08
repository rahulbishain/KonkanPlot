#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.dates
import csv, sys, re, random, os, datetime, time

datfile="Konkan timetable.csv"
#datfile1="Konkan2.csv"
Mcsv = csv.reader(open(datfile, 'rb'), delimiter=',', quotechar='"')
#Mcsv1 = csv.reader(open(datfile1, 'rb'), delimiter=',', quotechar='"')

# Mapping from column name to column index
I = {}
I1 = {}

# Matrix of all the rows
M = []
M1 = []
dis = []
dis1 = []
stn = []
stn1 = []
tim = []
tim1 = [0]
tim2 = [0]

trainCount = 0
for line in Mcsv:
    if 'Train No' in line[0]:
        dis.append(dis1)
        stn.append(stn1)
        tim.append(tim1)
        tim1[0] = tim2[0] 
        dis1 = []
        stn1 = []
        tim1 = []
        tim2 = []
        trainCount+=1
    else:
        if line[2]:
            dis1.append(line[7])
            stn1.append(line[2])
            tim1.append(line[4])
            tim2.append(line[5])
            

#for item in range(len(dis)):
#print tim[1]
#print dis1
time_col = map(lambda r: datetime.datetime.strptime(r,"%H:%M") , tim[1])
plt.plot(time_col, dis[1], 'b')
time_col = map(lambda r: datetime.datetime.strptime(r,"%H:%M") , tim[2])
plt.plot(time_col, dis[2], 'r')
plt.show()
'''
rowNum = 0
for row in Mcsv:
    rowNum += 1
    if (rowNum == 1):
        for i in range(len(row)):
            I[row[i]] = i
        continue
    else:
        M.append(row)

colors = { 'Distance':'blue'}
markers = { 'Distance':'|'}
lss = { 'Distance':'-'}

arrival_time_col = map(lambda r: datetime.datetime.strptime(r[I['Arrival Time']],"%d/%m/%y %H:%M"), M)
dat = 'Distance'
dat_col = map(lambda r: r[I[dat]], M)

rowNum = 0
for row in Mcsv1:
    rowNum += 1
    if (rowNum == 1):
        for i in range(len(row)):
            I1[row[i]] = i
        continue
    else:
        M1.append(row)

colors = { 'Distance':'blue'}
markers = { 'Distance':'|'}
lss = { 'Distance':'-'}

arrival_time_col1 = map(lambda r: datetime.datetime.strptime(r[I1['Arrival Time']],"%d/%m/%y %H:%M"), M1)
dat = 'Distance'
dat_col1 = map(lambda r: r[I1[dat]], M1)
#plt.figure(figsize=(20, 10))
plt.plot(arrival_time_col, dat_col, label=dat, ls=lss[dat], color='blue', marker=markers[dat], markersize=9, mew=2, linewidth=2)
plt.plot(arrival_time_col1, dat_col1, label=dat, ls=lss[dat], color='red', marker=markers[dat], markersize=9, mew=2, linewidth=2)
plt.xlabel('Time of day (24hr)')
plt.ylabel('Distance')
plt.grid(b='on')
#plt.axis(ymin=0,ymax=1000)
#plt.loglog()
#fig, p1 = plt.subplots()
#p1.ticklabel_format(axis='both', style='plain')
#from matplotlib.ticker import ScalarFormatter
#axes = plt.gca()
#axes.xaxis.set_major_formatter(ScalarFormatter())
#axes.yaxis.set_major_formatter(ScalarFormatter())
#axes.ticklabel_format(axis='both', style='plain')
plt.legend()
#plt.savefig("time_table.pdf", bbox_inches='tight')
plt.savefig("time_table.pdf")
plt.show()
#plt.plot_date(arrival_time_col,dat_col)
#plt.show()
'''
