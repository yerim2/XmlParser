# XmlParser
Xml to csv program 
==================
> 파이썬의 기본 모듈 ElementTree를 이용하여 xml을 파서한 후 csv파일로 변환하는 프로그램입니다

### 1. 코드
> 1-1. xmlParser.py
>> 파싱할 디렉토리의 path와 path내 파일의 order를 사용자 입력받아 하나의 csv로 변환,
>> 개발/ 실행환경 : window

```ruby

//----------filepath(xml file)의 root를 얻어서 원하는 태그의 내용을 출력----------
tree = ET.parse(filepath)
root = tree.getroot()

for child in root[1][1].findall('mt'):
     mt.append(child.text)
     i = i + 1
print(i)

//-----------파일 생성시간, 날짜를 저장------------------------------------------
ctime = os.path.getctime(filePATH)
    timeinfo = datetime.datetime.fromtimestamp(ctime)
    date = timeinfo.date()
    hour = timeinfo.hour
    min = timeinfo.minute
    cellId = 0
    
```
> 1-2. simtest.py
>> LTE simulator를 사용하여 특정 seed값에 대해 원하는 결과가 나오는지 확인하기 위함
>> seed.txt의 값을 읽어 lcm_test.seed를 만들어 테스트하여 결과는 expected_result라는 csv파일을 생성,
>> 개발/ 실행 환경 : linux 

```ruby

------------LTE simulator를 실행시키고 ERBSID를 +1 하여 업데이트 하기위함-----------------
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
```

```ruby
-------------csv의 첫줄을 작성하기 위함 ---------------------------------------------------
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
```

```ruby
------------seed파일을 만들기 위함 --------------------------------------------------------
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
```

```ruby
------------counter 값을 찍기 위함 --------------------------------------------------------
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
```


### 2. 사용한 xml파일들
> eNodeB의 동작 여부를 확인하는 simulator결과 값을 가진 mxl파일

![image](https://user-images.githubusercontent.com/24403704/51648132-d047e580-1fc2-11e9-890c-992702a98f4b.png)

> 사용한 폴더 이름 예시

![image](https://user-images.githubusercontent.com/24403704/51648193-eeade100-1fc2-11e9-957f-95875ff3438a.png)

> 결과물

![image](https://user-images.githubusercontent.com/24403704/51648227-05ecce80-1fc3-11e9-8281-f33f6d0e745c.png)
