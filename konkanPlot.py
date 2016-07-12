#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.dates
import csv, sys, re, random, os, datetime, time
#import getch # for user prompt. note: use msvcrt and not getch for windows

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
trainNo=[]
#trainNo.append('')
dis = []
dis1 = []
stn = []
stn1 = []
tim = []
tim1 = [0]
tim2 = [0]
runDays = []
runDays1 = []
dayOfJourney = []
days = {'MON':'01/01/01','TUE':'02/01/01','WED':'03/01/01','THU':'04/01/01','FRI':'05/01/01','SAT':'06/01/01','SUN':'07/01/01'}

trainCount = 0
linNum = 0
for line in Mcsv:
    linNum+=1
#    print linNum
    if 'Train No' in line[0]:
        tim1[0] = tim2[0] 
        for temp in runDays1:
            trainNo.append(line[0].strip().replace('\xef','').replace('\xc2','').replace('\xa0',''))
            dis.append(dis1)
            stn.append(stn1)
            tempTime = map(lambda r:days[temp]+' '+r,tim1)
            tempCount = 0
            for (x,y) in zip(tempTime,dayOfJourney):
                if y <> 1:
                    temp1 = int(x[1]) + int(y) - 1
                    temp1 = (temp1%7)
                    if temp1 == 0:
                        temp1 = 7
                    temp2 = list(x)
                    temp2[1] = str(temp1)
                    x = ''.join(temp2)
                    tempTime[tempCount] = x 
                tempCount += 1
            tim.append(tempTime)
            tempTime = []
            runDays.append(runDays1)
        dis1 = []
        stn1 = []
        tim1 = []
        tim2 = []
        runDays1 = []
        dayOfJourney = []
        trainCount+=1
    else:
        if 'runs on' in line[0].lower():
            runDays1 = line[0].split(':')[1].split(',')
            runDays1 = map(lambda r: r.strip().replace('\xef','').replace('\xc2','').replace('\xa0',''),runDays1)
            if 'DAILY' in runDays1:
                runDays1 = ['MON','TUE','WED','THU','FRI','SAT','SUN']
        if line[2]:
            dis1.append(line[7])
            stn1.append(line[2])
            tim1.append(line[4])
            tim2.append(line[5])
            dayOfJourney.append(line[6])
            

for i in range(trainCount):
    print 'train No = ',trainNo[i]
    for j in range(len(tim[i])):
        print tim[i][j],dis[i][j]
    s=raw_input()
#assert False
#    time_col = map(lambda r: datetime.datetime.strptime(r,"%d/%m/%y %H:%M") , tim[i])
#    plt.plot(time_col, dis[i], 'b',marker="|", markersize=9, mew=2, linewidth=.5)
#
#plt.show()
print trainCount
trainUpDown=[]
for x in range(trainCount):
    print "train - ",x+1
    distanceNotZero = 0
    upDown = 'NA'
    prevDistance = 0
    prevStn=''
    currDistance = 0
    for a,b,c in zip(tim[x],dis[x],stn[x]):
        print c,a,b
        currDistance = int(b)
        if currDistance<>0 and distanceNotZero==0:
            distanceNotZero = 1
        if distanceNotZero==1 and upDown=='NA':
            if prevDistance <> 0:
                if prevDistance < currDistance:
                    upDown = 'Down'
                elif prevDistance > currDistance and currDistance<>0:
                    upDown = 'Up'
        prevDistance = currDistance
        prevStn = c
    print upDown
    trainUpDown.append(upDown)
    if upDown =='NA':
        assert False
    s = raw_input()
    continue
for x in range(trainCount):
    print x+1,trainNo[x],trainUpDown[x]
    upDown=trainUpDown[x]
    for a,b,c in zip(tim[x],dis[x],stn[x]):
#        print c,a,b
        if upDown=='Down': 
            if currDistance==0 and prevDistance>0:
                print "WATCHDOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                if prevStn <> 'KNKD' and prevStn<>'MAQ':
                    print trainNo[x]
                    assert False
            elif currDistance>0 and prevDistance==0:
                print "WATCHDOWN--------------------------------------"
                if prevStn <> 'ROH' and prevStn<>'PNVL':
                    print trainNo[x]
                    assert False
        elif upDown=='Up': 
            if currDistance>0 and prevDistance==0:
                print "UPWATCH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                if c<>'KNKD' and c<>'MAQ':
                    print trainNo[x]
                    assert False
            elif currDistance==0 and prevDistance>0:
                print "UPWATCH--------------------------------------"
                if c<>'ROH' and c<>'PNVL':
                    print trainNo[x]
                    assert False
    s=raw_input()
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
