
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 600)
        Form.setFixedSize(850, 600)
        Form.setAutoFillBackground(False)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(40, 420, 781, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 821, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ustanovka.png"))
        self.label.setObjectName("label")
        self.InfoFon = QtWidgets.QLabel(Form)
        self.InfoFon.setGeometry(QtCore.QRect(-10, 0, 861, 601))
        self.InfoFon.setText("")
        self.InfoFon.setPixmap(QtGui.QPixmap("back.jpg"))
        self.InfoFon.setObjectName("InfoFon")
        self.InfoFon_2 = QtWidgets.QWidget(Form)
        self.InfoFon_2.setGeometry(QtCore.QRect(280, 0, 241, 41))
        self.InfoFon_2.setStyleSheet("background-color: rgb(127, 127, 127);\n"
"")
        self.InfoFon_2.setObjectName("InfoFon_2")
        self.Scheme = QtWidgets.QLabel(self.InfoFon_2)
        self.Scheme.setGeometry(QtCore.QRect(0, 0, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Scheme.setFont(font)
        self.Scheme.setObjectName("Scheme")
        self.InfoFon.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.InfoFon_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:133%;\"><span style=\" font-size:8pt;\">Переключатель </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">S</span><span style=\" font-size:8pt; vertical-align:sub;\">3</span><span style=\" font-size:8pt;\"> предназначен для управления освещенностью Ф фотокатода.</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"><br /></span><span style=\" font-size:8pt;\">Он обеспечивает протекание тока разной величины в нити лампы накаливания </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">Л</span><span style=\" font-size:8pt; vertical-align:sub;\">1</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">. <br />С помощью переключателя </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">S</span><span style=\" font-size:8pt; vertical-align:sub;\">2</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> </span><span style=\" font-size:8pt;\"> обеспечивается прямое или обратное подключение фотоэлемента ФЭ к источнику напряжения. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:133%;\"><span style=\" font-size:8pt;\">Для изменения прямого и обратного напряжения между электродами ФЭ электрическая схема содержит, соответственно, потенциометры R</span><span style=\" font-size:8pt; vertical-align:sub;\">1</span><span style=\" font-size:8pt;\"> и R</span><span style=\" font-size:8pt; vertical-align:sub;\">2</span><span style=\" font-size:8pt;\"> - R</span><span style=\" font-size:8pt; vertical-align:sub;\">3</span><span style=\" font-size:8pt;\">. Сила фототока фотоэлемента измеряется микропмперметром PA, а напряжение между его электродами контролируется вольтметром PU</span></p></body></html>"))
        self.Scheme.setText(_translate("Form", "Схема установки"))
