import csv
import os
import subprocess
from datetime import datetime
from time import sleep

ERBS = 1541
Num = str(ERBS)
ERBSID = "ERBS"+ Num

cellid = 0
number = 0
count = 0
array = []
attribute = []
TITLES =[]

ATTR_FILE = open('attribute.txt','r')
while(1):
        line = ATTR_FILE.readline()
        if line:
                TITLES.append(line)
        else:
                break
ERBS_FILE = open('lcm_erbs.list','w')
EXP_RESULT = open('expected_result1.csv','w')
SEED_FILE = open('lcm_seed.seed', 'w')


def make_erbs_list():
    ERBS_FILE.write(ERBSID+"=10.183.170.80:32768")
    print(ERBSID+"=10.183.170.80:32768")

def make_seed():
    global cellid
    cellid = count % 6
    CELLID = str(cellid)
    SEED_FILE = open('lcm_seed.seed', 'a')
    SEED_FILE.write("INTERNAL_CALL_START,"+CELLID)
    print("INTERNAL_CALL_START,"+CELLID)
    content = INTERNAL
    print(content)
    SEED_FILE = open('lcm_seed.seed', 'a')
    SEED_FILE.write(content)

def write_csv():
    global attribute
    global cellid
    global ERBSID
    result =[]
    result.append(attribute)
    print(result)
    CNT = [None]*(len(TITLES))
    for i in range(0,len(TITLES)):
        CNT[i]=0
    print(CNT)
    for RE in result:
        INDEX = 0
        for TIT in TITLES:
            if(TIT == RE):
                print("MATCH:" + str(INDEX) + ":" + TIT)
                CNT[INDEX] = CNT[INDEX] + 1
                print(CNT[INDEX])
            else:
                INDEX = INDEX + 1

    date = datetime.now()
    DATE = str(date.year) + '/' + str(date.month) + '/' + str(date.day)
    HH = date.hour
    MM = date.month
    print("MM :" + str(MM))
    ROP = (MM / 5) * 5

    LINE = [ERBSID, DATE, HH, ROP, cellid]

    for ITEM in CNT:
        LINE.append(ITEM)
    EXP_RESULT = open('expected_result1.csv', 'a' )
    writer = csv.writer(EXP_RESULT)
    writer.writerow(LINE)
    attribute=""
    global count
    count = count + 1

    print(count)

def execute():
    make_erbs_list()
    print("./start_sim_script.sh")
    print("count :"+ str(count))
    subprocess.call('./sh_start_test_L19A.sh',shell=True)

    if os.path.isfile('lcm_seed.seed'):
       os.remove('lcm_seed.seed')

    global ERBS
    ERBS = ERBS + 1
    global ERBSID
    Num = str(ERBS)
    ERBSID = "ERBS" + Num

    date = datetime.now()
    SEC = date.second
    if(SEC > 50):
        print(date)
        print('SLEEP')
        sleep(10)

def make_csv():
    EXP_RESULT = open('expected_result1.csv','a')
    writer = csv.writer(EXP_RESULT)
    writer.writerow(" ")
    writer.writerow(" ")

    TIT = ['ERBSID', 'Date', 'Hour', 'Min', 'Cell ID']
    ATTR_FILE = open('attribute.txt', 'r')
    while(1):
        line = ATTR_FILE.readline()
        if line:
            TIT.append(line)
        else:
            break
    writer.writerow(TIT)

print('*************START LCM TEST***************')
date = datetime.now()
START = date.now()

if os.path.isfile('lcm_seed.seed'):
    os.remove('lcm_seed.seed')

SEEDS = open('seed3.txt','r')
make_csv()
while (1):
    line = SEEDS.readline()
    if line:
        INTERNAL = line.split("\t")[0]
        array.append(line.split("\t")[1])
        a = INTERNAL.split(",")[0]
        b = line.split("\t")[1]
        FIRST_ARRAY = [a,b]
        for i in range(0,2):
                FIRST = FIRST_ARRAY[i]
                if(FIRST == 'INTERNAL_PROC_HO_PREP_S1_OUT'):
                        make_seed()
                elif(FIRST == 'INTERNAL_PROC_HO_EXEC_S1_OUT'):
                        make_seed()
                else:
                        attribute =FIRST
                        write_csv()
                        number = number +1
                        if(number == 6 ):
                                number=0
                                execute()
    else:
        break

if(number >0):
    execute()

END = date.now()
print("START : " + str(START))
print("END : " + str(END))
