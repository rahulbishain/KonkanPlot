#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.dates
import csv, sys, re, random, os, datetime, time

datfile="Konkan1.csv"
Mcsv = csv.reader(open(datfile, 'rb'), delimiter=',', quotechar='"')

# Mapping from column name to column index
I = {}

# Matrix of all the rows
M = []

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

plt.plot(arrival_time_col, dat_col, label=dat, ls=lss[dat], color=colors[dat], marker=markers[dat], markersize=9, mew=2, linewidth=2)
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
#plt.figure(figsize=(20, 2))
plt.savefig("time_table.pdf")
plt.show()
#plt.plot_date(arrival_time_col,dat_col)
#plt.show()
