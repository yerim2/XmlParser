# XmlParser
Xml to csv program 
==================
> 파이썬의 기본 모듈 ElementTree를 이용하여 xml을 파서한 후 csv파일로 변환하는 프로그램입니다

### 1. 코드
> 1-1. xmlParser.py
>> 파싱할 디렉토리의 path와 path내 파일의 order를 사용자 입력받아 하나의 csv로 변환

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
>> LTE simulator를 사용하여 특정 seed값에 대해 원하는 결과가 나오는지 확인하기 위해 expected_result를 생성
>> seed.txt의 값을 읽어 lcm_test.seed를 만들어 테스트하여 결과는 expected_result라는 csv파일로 

### 2. 사용한 xml파일들
> eNodeB의 동작 여부를 확인하는 simulator결과 값을 가진 mxl파일

![image](https://user-images.githubusercontent.com/24403704/51648132-d047e580-1fc2-11e9-890c-992702a98f4b.png)

> 사용한 폴더 이름 예시

![image](https://user-images.githubusercontent.com/24403704/51648193-eeade100-1fc2-11e9-957f-95875ff3438a.png)

> 결과물

![image](https://user-images.githubusercontent.com/24403704/51648227-05ecce80-1fc3-11e9-8281-f33f6d0e745c.png)
