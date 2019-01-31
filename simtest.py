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


ERBS_FILE = open('lcm_erbs.list','w')
EXP_RESULT = open('expected_result1.csv','w')


def make_erbs_list():
    ERBS_FILE.write(ERBSID+"=10.183.170.80:32768")
    print(ERBSID+"=10.183.170.80:32768")

def make_seed():
    cellid = count % 6
    CELLID = str(cellid)
    SEED_FILE = open('lcm_seed.seed', 'w')
    SEED_FILE.write("INTERNAL_CALL_START,"+CELLID)
    print("INTERNAL_CALL_START,"+CELLID)
    content = []
    content.append(array[0])
    for i in range(1,len(array)+1):
        content.append(array[i])

    SEED_FILE = open('lcm_seed.seed', 'a')
    SEED_FILE.wrivte(content)

def write_csv():
    global attribute
    ATTR_FILE = open('attribute.txt', 'r')
    while (1):
        line = ATTR_FILE.readline()
        if line:
            TITLES.append(line)
        else:
            break

    result =[]
    result.append(attribute)
    CNT = []
    for i in range(0,len(TITLES)+1):
        CNT[i]=0
    for RE in result:
        INDEX = 0
        for TIT in TITLES:
            if(TIT == RE):
                print("MATCH:" + str(INDEX) + ":" + TIT)
                CNT[INDEX] = CNT[INDEX] + 1
            else:
                INDEX = INDEX + 1

    date = datetime.now()
    DATE = date.year + '/' + date.month + '/' + date.day
    HH = date.hour
    MM = date.month
    print("MM :" + MM)
    ROP = (MM / 5) * 5

    LINE = [ERBSID, DATE, HH, ROP, cellid]

    for ITEM in CNT:
        LINE.append(ITEM)

    EXP_RESULT = open('expected_result1.csv', 'a', newline='')
    writer = csv.writer(EXP_RESULT)
    writer.writerow(LINE)
    attribute.clear()
    global count
    count = count + 1


def execute():
    make_erbs_list()
    print("./start_sim_script.sh")
    print("count :"+ str(count))
    subprocess.call(['./sh_start_test_L19A.sh'])

    if os.path.isfile('lcm_seed.seed'):
       os.remove('lcm_seed.seed')

    global ERBS
    ERBS = ERBS + 1

    date = datetime.now()
    SEC = date.second
    if(SEC > 50):
        print(date)
        print('SLEEP')
        sleep(10)

def make_csv():
    EXP_RESULT = open('expected_result1.csv','a',newline='')
    writer = csv.writer(EXP_RESULT)
    writer.writerow(" ")
    writer.writerow({"Report1"})
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

SEEDSinput = input('seed fild : ')
print('*************Seed file is : ' + SEEDSinput +'*************')
SEEDS = open(SEEDSinput,'r')
make_csv()
while (1):
    line = SEEDS.readline()
    if line:
        array.append(line)
        FIRST = array[0]
        print(FIRST)
        FIRST = array[0]
        if(FIRST == 'INTERNAL_PROC_HO_PREP_S1_OUT'):
            make_seed()
        elif(FIRST == 'INTERNAL_PROC_HO_EXEC_S1_OUT'):
            make_seed()
        else:
            attribute = line
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
print("START : " + START)
print("END : " + END)



