import xml.etree.ElementTree as ET
import csv
import os
from os import listdir
from os.path import isfile,join
import datetime

ERBS = 1541
Num = str(ERBS)
ERBSID = "ERBS"+ Num

dirPATH =  'C:\\Users\ekmxrmx\Desktop\SubNetwork=NETSIM_ERBS\MeContext='+ERBSID
files = [f for f in listdir(dirPATH) if isfile(join(dirPATH,f))]
firstfile = dirPATH+ '/' + files[2]

mt = ['ERBS Id', 'Date', 'Hour', 'Min', 'Cell Id']
tree = ET.parse(firstfile)
root = tree.getroot()
i = 0
########## result 부분을 mt라는 배열에 넣음 (i는 개수) ##########################
for child in root[1][1].findall('mt'):
     mt.append(child.text)
     i = i + 1
print(i)

######### csv의 첫줄 ########################################################
with open('ex1.csv','w',newline='')as fd:
    fieldnames = ['mt']
    #writer = csv.DictWriter(fd, fieldnames=fieldnames)
    fields = mt
    writer = csv.writer(fd)
    writer.writerow(fields)



for roof in range(ERBS, 1551):
    ERBSID = "ERBS" + str(roof)
    dirPATH = 'C:\\Users\ekmxrmx\Desktop\SubNetwork=NETSIM_ERBS\MeContext=' + ERBSID
    print(dirPATH)
    files = [f for f in listdir(dirPATH) if isfile(join(dirPATH, f))]
    filePATH = dirPATH + '/' + files[2]
    print(filePATH)

    ctime = os.path.getctime(filePATH)
    timeinfo = datetime.datetime.fromtimestamp(ctime)
    date = timeinfo.date()
    hour = timeinfo.hour
    min = timeinfo.minute
    cellId = 0

    tree = ET.parse(filePATH)
    root = tree.getroot()

    count = []
    k = 0



    ######### count value를 count라는 배열에 넣음 ##############################
    for child in root[1][1].findall('mv'):
        for r in child:
            count.append(r.text)
    print(len(count))

    cellnum = len(count) // i #셀의 개수 구하기
    print(cellnum)

    cellarray =[]
    for z in range(0,len(count)):
        ID = count[z].split(',')
        if(len(ID) > 1):
            IDNum = ID[2].split('=')
            cellarray.append(IDNum[1])
    print(cellarray)
    #print(cellarray.index('0'))

    ########## count만 찍는부분 ###############################################
    for y in range(0, cellnum):  #0~5번 돌기
        # cell number 빼기
        ID = count[cellId * (i + 1)].split(',')
        #print(ID[2])
        #IDNum = ID[2].split('=')
        #print(IDNum[1])
        print(cellarray.index(str(y)))

        cellId = cellarray.index(str(y))


        mts = [ERBSID, date, hour, min, y]
        for x in range(cellId * (i + 1) + 1, (i + 1) * (cellId + 1)):
            mts.append(count[x])

        with open('ex1.csv', 'a', newline='')as fd:
            writer = csv.writer(fd)
            fields2 = mts
            writer.writerow(fields2)
        mts.clear()
        #cellId = cellId + 1