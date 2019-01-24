# XmlParser
Xml to csv program 
==================
> 파이썬의 기본 모듈 ElementTree를 이용하여 xml을 파서한 후 csv파일로 변환하는 프로그램입니다

### 1. 코드
> 1-1. source.py

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

### 2. 사용한 xml파일들
> eNodeB의 동작 여부를 확인하는 simulator결과 값을 가진 mxl파일

