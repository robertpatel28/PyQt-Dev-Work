# Form implementation generated from reading ui file 'averagescore.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_averageScore(object):
    def setupUi(self, averageScore):
        averageScore.setObjectName("averageScore")
        averageScore.resize(1117, 852)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        averageScore.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=averageScore)
        self.centralwidget.setObjectName("centralwidget")
        self.lblScore = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblScore.setGeometry(QtCore.QRect(390, 180, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblScore.setFont(font)
        self.lblScore.setObjectName("lblScore")
        self.txtScore = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtScore.setGeometry(QtCore.QRect(600, 180, 113, 22))
        self.txtScore.setObjectName("txtScore")
        self.btnStore = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnStore.setGeometry(QtCore.QRect(610, 270, 93, 28))
        self.btnStore.setObjectName("btnStore")
        self.btnAverage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAverage.setGeometry(QtCore.QRect(610, 340, 93, 28))
        self.btnAverage.setObjectName("btnAverage")
        self.btnClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(610, 420, 93, 28))
        self.btnClear.setObjectName("btnClear")
        self.lstScores = QtWidgets.QListWidget(parent=self.centralwidget)
        self.lstScores.setGeometry(QtCore.QRect(820, 170, 231, 311))
        self.lstScores.setObjectName("lstScores")
        self.lblStudentScores = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblStudentScores.setGeometry(QtCore.QRect(850, 130, 161, 21))
        self.lblStudentScores.setObjectName("lblStudentScores")
        averageScore.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=averageScore)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 23))
        self.menubar.setObjectName("menubar")
        averageScore.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=averageScore)
        self.statusbar.setObjectName("statusbar")
        averageScore.setStatusBar(self.statusbar)

        self.retranslateUi(averageScore)
        QtCore.QMetaObject.connectSlotsByName(averageScore)
        
        # Creating an empty python list named student_scores_lst to store student scores
        self.student_scores_lst = []
        
        self.btnStore.clicked.connect(self.store_score)
        
        self.btnAverage.clicked.connect(self.calculate_average)
        
        self.btnClear.clicked.connect(self.clear)
        
        
    def store_score(self):
        if(self.txtScore.text().isnumeric()):
            student_score = float(self.txtScore.text())
            self.student_scores_lst.append(student_score)
            self.lstScores.addItem(str(student_score))
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Average Score")
            msg.setText("Please enter a numeric student score")
            msg.exec()
            
    def calculate_average(self):
        
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Average Score")
        
        if(len(self.student_scores_lst) > 0):
            average_score = sum(self.student_scores_lst)/len(self.student_scores_lst)
            
            msg.setText(str(average_score))
        else:
            msg.setText("No student scores stored")
        
        msg.exec()  

    def clear(self):
        self.txtScore.clear()
        self.lstScores.clear()
        self.student_scores_lst.clear()        
            

    def retranslateUi(self, averageScore):
        _translate = QtCore.QCoreApplication.translate
        averageScore.setWindowTitle(_translate("averageScore", "Average Score"))
        self.lblScore.setText(_translate("averageScore", "Enter Student Score"))
        self.btnStore.setText(_translate("averageScore", "Store"))
        self.btnAverage.setText(_translate("averageScore", "Average"))
        self.btnClear.setText(_translate("averageScore", "Clear"))
        self.lblStudentScores.setText(_translate("averageScore", "Stored Student Scores"))
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    averageScore = QtWidgets.QMainWindow()
    ui = Ui_averageScore()
    ui.setupUi(averageScore)
    averageScore.show()
    sys.exit(app.exec())