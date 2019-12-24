import sys
import json
import requests
from time import sleep

from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets 
from pyhugeconnector import pyhugeconnector as HUGE # API BIG HUGE DICTIONARY


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 610)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ## Title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(60, 0, 271, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")


        ## USER INPUT LINES
        # sentence line
        self.sentence_line = QtWidgets.QLineEdit(self.centralwidget)
        self.sentence_line.setGeometry(QtCore.QRect(50, 40, 291, 20))
        self.sentence_line.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.sentence_line.setAutoFillBackground(False)
        self.sentence_line.setInputMask("")
        self.sentence_line.setText("Sentence")
        self.sentence_line.setObjectName("sentence_line")

        # word line
        self.wrd_line = QtWidgets.QLineEdit(self.centralwidget)
        self.wrd_line.setGeometry(QtCore.QRect(50, 70, 291, 20))
        self.wrd_line.setText("Word")
        self.wrd_line.setObjectName("wrd_line")


        ## Main Buttons & RadioButton
        # PushButton Analyze
        self.analyze = QtWidgets.QPushButton(self.centralwidget)
        self.analyze.setGeometry(QtCore.QRect(50, 100, 111, 31))
        self.analyze.setObjectName("analyze")
        self.analyze.clicked.connect(self.analyze_it)

        # RadioButton Adjective
        self.adjective = QtWidgets.QRadioButton(self.centralwidget)
        self.adjective.setGeometry(QtCore.QRect(190, 122, 84, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.adjective.setFont(font)
        self.adjective.setObjectName("adjective")
        self.adjective.setChecked(True)

        # RadioButton Noun
        self.noun = QtWidgets.QRadioButton(self.centralwidget)
        self.noun.setGeometry(QtCore.QRect(190, 107, 61, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.noun.setFont(font)
        self.noun.setObjectName("noun")

        # RadioButton Verb
        self.verb = QtWidgets.QRadioButton(self.centralwidget)
        self.verb.setGeometry(QtCore.QRect(190, 92, 61, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verb.setFont(font)
        self.verb.setObjectName("verb")


        # INPUT BOX Resultbox
        self.result_box = QtWidgets.QListWidget(self.centralwidget)
        self.result_box.setGeometry(QtCore.QRect(50, 140, 291, 391))
        self.result_box.setObjectName("result_box")

        ## Help & SAVE Buttons
        self.HELP = QtWidgets.QPushButton(self.centralwidget)
        self.HELP.setGeometry(QtCore.QRect(50, 540, 71, 20))
        self.HELP.setObjectName("HELP")
        self.HELP.clicked.connect(self.help_it)
        '''
        self.SAVE = QtWidgets.QPushButton(self.centralwidget)
        self.SAVE.setGeometry(QtCore.QRect(270, 540, 71, 20))
        self.SAVE.setObjectName("SAVE")
        self.SAVE.clicked.connect(self.saveFileDialog)
        '''
        ## Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.adjective.setText(_translate("MainWindow", "Adjective"))
        self.noun.setText(_translate("MainWindow", "Noun"))
        self.analyze.setText(_translate("MainWindow", "Analyze"))
        self.title.setText(_translate("MainWindow", "Probably Knot"))
        self.HELP.setText(_translate("MainWindow", "HELP"))
        self.verb.setText(_translate("MainWindow", "Verb"))
        #self.SAVE.setText(_translate("MainWindow", "SAVE"))
        self.sentence_line.setStatusTip(_translate("MainWindow", "Sentence goes here..."))
        self.wrd_line.setStatusTip(_translate("MainWindow", "one 'Word' from Sentence goes here..."))
    def analyze_it(self):
        self.result_box.clear() # clear result list view for next analyze_it
        # user inputs variables
        txt = self.sentence_line.text().lower()
        wrd = self.wrd_line.text().lower()
        
        if txt != '':
            API_KEY = 'a701e74e453ee6695e450310340401f5'
            URL = f'http://words.bighugelabs.com/api/2/{API_KEY}/{wrd}/json'
            
            # RELATIONSHIP_ABBR = {'syn':'Synonyms','ant':'Antonyms','rel':'Related terms',
            #                       'sim':'Similar terms','usr':'User suggestions'}

            if wrd not in txt:
                self.result_box.addItem(f"Word: '{wrd}' is not in\n\n'{txt}'")
            elif wrd in txt:
                # setup API HUGE BIG Thesaurus
                r = requests.get(URL) # get's url json file
                j = json.loads(r.text) # loads json into 'j' as a dict
                
                if type(j) == dict: # check is 'j' variable is coming in as a Dict

                    if self.adjective.isChecked():
                        # holds the new sentences
                        new = ''
                        try:
                            for num, w in enumerate(j['adjective']['syn'], 1):
                                new += f"{num}: {txt.replace(wrd, w)}\n"

                            self.result_box.addItem(f"Original Sentence:\n{txt}\n")       
                            self.result_box.addItem(new)
                        except KeyError:
                            print(f'{wrd} is not found.')
                            warning = f"Word --> '{wrd}'\nis not an on our list! Please try 'Noun' button\n{txt}"
                            self.result_box.addItem(warning)
                    if self.noun.isChecked():
                        # holds the new sentences
                        new = ''
                        try:
                            for num, w in enumerate(j['noun']['syn'], 1):
                                new += f"{num}: {txt.replace(wrd, w)}\n"

                            self.result_box.addItem(f"Original Sentence:\n{txt}\n")       
                            self.result_box.addItem(new)
                        except KeyError:
                            print(f'{wrd} is not found.')
                            warning = f"Word --> '{wrd}'\nis not an on our list! Please try 'Adjective' button\n{txt}"
                            self.result_box.addItem(warning)
                    if self.verb.isChecked():
                        # holds the new sentences
                        new = ''
                        try:
                            for num, w in enumerate(j['verb']['syn'], 1):
                                new += f"{num}: {txt.replace(wrd, w)}\n"

                            self.result_box.addItem(f"Original Sentence:\n{txt}\n")       
                            self.result_box.addItem(new)
                        except KeyError:
                            print(f'{wrd} is not found.')
                            warning = f"Word --> '{wrd}'\nis not an on our list! Please try 'Noun' button\n{txt}"
                            self.result_box.addItem(warning)

                    self.sentence_line.clear()
                    self.wrd_line.clear()
                
                if type(j) == list: # check is 'j' variable is coming in as a List

                    if self.adjective.isChecked():
                        # holds the new sentences
                        new = ''
                        try:
                            for num, w in enumerate(j, 1):
                                new += f"{num}: {txt.replace(wrd, w)}\n"

                            self.result_box.addItem(f"Original:\n{txt}\n")       
                            self.result_box.addItem(new)
                        except KeyError:
                            print(f'{wrd} is not found.')
                            warning = f"Word --> '{wrd}'\nis not an on our list! Please try 'Noun' button"
                            self.result_box.addItem(warning)
                    if self.noun.isChecked():
                        # holds the new sentences
                        new = ''
                        try:
                            for num, w in enumerate(j, 1):
                                new += f"{num}: {txt.replace(wrd, w)}\n"

                            self.result_box.addItem(f"Original:\n{txt}\n")       
                            self.result_box.addItem(new)
                        except KeyError:
                            print(f'{wrd} is not found.')
                            warning = f"Word --> '{wrd}'\nis not an on our list! Please try 'Adjective' button"
                            self.result_box.addItem(warning)
                    if self.verb.isChecked():
                        # holds the new sentences
                        new = ''
                        try:
                            for num, w in enumerate(j, 1):
                                new += f"{num}: {txt.replace(wrd, w)}\n"

                            self.result_box.addItem(f"Original Sentence:\n{txt}\n")       
                            self.result_box.addItem(new)
                        except KeyError:
                            print(f'{wrd} is not found.')
                            warning = f"Word --> '{wrd}'\nis not an on our list! Please try 'Noun' button\n{txt}"
                            self.result_box.addItem(warning)

                    self.sentence_line.clear()
                    self.wrd_line.clear()
        else:
            self.result_box.addItem('Please enter a\nSentence & Word to Analyze')
    

    def help_it(self):
        self.result_box.addItem("Welcome to 'Probably Knot'!\nA program designed to help you better understand\nyour problems. "
                                "\n\n1. Type a 'Problem Sentence' in the first line above.\n2. Select a word from that 'Problem Sentence' and\ntype it in the second line below it.\n\n"
                                "Typically the word you pick should be an adjective\nor a noun to better help you rephrase the question.\n\n*This is to help you understand the problem from\na different view point.")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
