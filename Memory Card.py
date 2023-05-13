import random
from PyQt5.QtWidgets import *
from dsdfsdsdf import*
from dsdfsdsdf import*
from dani import*
from dani2 import*
app = QApplication([])
mainWin = QWidget()
mainWin.resize(500, 500)
menuBtn = QPushButton("Меню")
breakBtn = QPushButton("Відпочити")
spinBox = QSpinBox()
minLbl = QLabel("Хвилин")
quest = QLabel("Яблуко")
resultLbl = QLabel("Правильно")
resultLbl.hide()
groupBox = QGroupBox("Варіанти відповідей")
ans1Btn = QRadioButton("home")
ans2Btn = QRadioButton("apple")
ans3Btn = QRadioButton("car")
ans4Btn = QRadioButton("aple")

answerBtn = QPushButton("Відповісти")
reg = QPushButton("Редагувати")
nextBtn = QPushButton("Наступна відповідь")
nextBtn.hide()
answers = [ans1Btn, ans2Btn, ans3Btn, ans4Btn]
hLineButtons = QHBoxLayout()
hLineButtons.addWidget(ans1Btn)
hLineButtons.addWidget(ans2Btn)
hLineButtons.addWidget(ans3Btn)
hLineButtons.addWidget(ans4Btn)
hLineButtons.addWidget(resultLbl)
groupBox.setLayout(hLineButtons)

mainLine = QVBoxLayout()
hline = QHBoxLayout()
hline.addWidget(menuBtn)
hline.addStretch(1)
hline.addWidget(breakBtn)
hline.addWidget(spinBox)
hline.addWidget(minLbl)
mainLine.addLayout(hline)
mainLine.addWidget(quest)
mainLine.addWidget(groupBox)
mainLine.addWidget(answerBtn)
mainLine.addWidget(nextBtn)
mainLine.addWidget(reg)
def shaffleAnswers():
    global currntQuest
    random.shuffle(answers)
    quest.setText(listQuestion[currntQuest]["питання"])
    answers[0].setText(listQuestion[currntQuest]["правильна відповідь"])
    answers[1].setText(listQuestion[currntQuest]["не правильна1"])
    answers[2].setText(listQuestion[currntQuest]["не правильна2"])
    answers[3].setText(listQuestion[currntQuest]["не правильна3"])

def showMenu():
    mainWin.hide()
    showMenuWindow()
    mainWin.show()

def showResult():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    resultLbl.show()
    if answers[0].isChecked():
        resultLbl.setText("Правильно")
    else:
        resultLbl.setText("Не правильно")
    answerBtn.hide()
    nextBtn.show()

def nextQust():
    global currntQuest
    currntQuest += 1
    for btn in answers:
        btn.show()

    resultLbl.hide()
    answerBtn.show()
    nextBtn.hide()
    shaffleAnswers()

def edit():
    mainWin.hide()
    showEditWindow()
    mainWin.show()
    shaffleAnswers()
shaffleAnswers()

menuBtn.clicked.connect(showMenu)
answerBtn.clicked.connect(showResult)
nextBtn.clicked.connect(nextQust)
reg.clicked.connect(edit)

mainWin.setLayout(mainLine)
mainWin.show()
app.exec_()
