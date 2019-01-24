# XmlParser
Xml to csv program 
==================
> 파이썬의 기본 모듈 ElementTree를 이용하여 xml을 파서한 후 csv파일로 변환하는 프로그램입니다

### 1. 코드
> 1-1. source.py
//------------------xml의 root를 받아 'mt'태그를 받음------------------
tree = ET.parse(firstfile)
root = tree.getroot()
for child in root[1][1].findall('mt'):
