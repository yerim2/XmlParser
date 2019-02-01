import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import xml.etree.ElementTree as ET
import csv
import os
from os import listdir
from os.path import isfile,join
import datetime




class MyApp(QWidget):
    def parser(self):
        ERBS = 1541
        Num = str(ERBS)
        ERBSID = "ERBS" + Num

        input_path = self.filepath


        input_order = self.order
        fileorder = int(input_order)-1

        dirPATH = input_path + '\\MeContext=' + ERBSID

        files = [f for f in listdir(dirPATH) if isfile(join(dirPATH, f))]
        firstfile = dirPATH + '/' + files[fileorder]
        print(files)

        mt = ['ERBS Id', 'Date', 'Hour', 'Min', 'Cell Id']
        tree = ET.parse(firstfile)
        root = tree.getroot()
        i = 0
        ########## result 부분을 mt라는 배열에 넣음 (i는 개수) ##########################
        for child in root[1][1].findall('mt'):
            mt.append(child.text)
            i = i + 1

        ######### csv의 첫줄 ########################################################
        with open('output.csv', 'w', newline='')as fd:
            fieldnames = ['mt']
            fields = mt
            writer = csv.writer(fd)
            writer.writerow(fields)

        for roof in range(ERBS, 1551):
            ERBSID = "ERBS" + str(roof)
            dirPATH = 'C:\\Users\ekmxrmx\Desktop\SubNetwork=NETSIM_ERBS\MeContext=' + ERBSID
            files = [f for f in listdir(dirPATH) if isfile(join(dirPATH, f))]
            filePATH = dirPATH + '/' + files[fileorder]
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

            cellnum = len(count) // i  # 셀의 개수 구하기

            cellarray = []
            for z in range(0, len(count)):
                ID = count[z].split(',')
                if (len(ID) > 1):
                    IDNum = ID[2].split('=')
                    cellarray.append(IDNum[1])

            ########## count만 찍는부분 ###############################################
            for y in range(0, cellnum):  # 0~5번 돌기
                # cell number 빼기
                ID = count[cellId * (i + 1)].split(',')
                cellId = cellarray.index(str(y))

                mts = [ERBSID, date, hour, min, y]
                for x in range(cellId * (i + 1) + 1, (i + 1) * (cellId + 1)):
                    mts.append(count[x])

                with open('output.csv', 'a', newline='')as fd:
                    writer = csv.writer(fd)
                    fields2 = mts
                    writer.writerow(fields2)
                mts.clear()

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Output xml file to csv")
        self.move(300, 300)
        self.resize(500, 200)

        QToolTip.setFont(QFont('SansSerif',10))

        self.label1 = QLabel('Enter your <b>SubNetwork</b> file path & <b>Order</b>',self)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont('SansSerif',15))
        self.label1.move(55,25)

        self.qle = QLineEdit(self)
        self.qle.move(185,80)

        self.qle2 = QLineEdit(self)
        self.qle2.move(185, 110)



        Enter_btn = QPushButton('Enter', self)
        Enter_btn.move(170, 150)
        Enter_btn.resize(Enter_btn.sizeHint())
        Enter_btn.setToolTip('This is <b>Test</b>')
        #Enter_btn.clicked.connect(QCoreApplication.instance().quit)
        Enter_btn.clicked.connect(self.on_click)


        Quit_btn = QPushButton('Quit',self)
        Quit_btn.move(255,150)
        Quit_btn.resize(Quit_btn.sizeHint())
        Quit_btn.setToolTip('This is <b>Test</b>')
        Quit_btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()

    def on_click(self):
        self.filepath = self.qle.text()
        self.order = self.qle2.text()
        self.parser()
        print(self.filepath)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())