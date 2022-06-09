import os
import math
import random
import PyQt5
import new
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMessageBox
from new import Ui_Form
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2057, 938)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(back.jpg)}")
        MainWindow.setFixedSize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(730, 130, 421, 275))
        self.widget.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                  "")
        self.widget.setObjectName("widget")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(20, 30, 191, 150))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.name_fototok = QtWidgets.QLabel(self.widget)
        self.name_fototok.setGeometry(QtCore.QRect(60, 180, 121, 31))
        self.name_fototok.setStyleSheet("font: 75 12pt \"Arial\";")
        self.name_fototok.setObjectName("name_fototok")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 230, 101, 31))
        self.radioButton_2.setStyleSheet("font: 75 16pt \"Arial\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalSlider_2 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(320, 50, 22, 160))
        self.verticalSlider_2.setMaximum(2)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(310, 230, 70, 13))
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(350, 120, 41, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(350, 190, 41, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(350, 50, 41, 16))
        self.label_15.setObjectName("label_15")
        self.lcdNumber_2.raise_()
        self.name_fototok.raise_()
        self.radioButton_2.raise_()
        self.verticalSlider_2.raise_()
        self.label_8.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(30, 130, 681, 571))
        self.widget_2.setWhatsThis("")
        self.widget_2.setStyleSheet("background-color: rgb(136, 136, 136);\n"
                                    "border-color: rgb(45, 45, 45);")
        self.widget_2.setObjectName("widget_2")
        self.lighter_switch = QtWidgets.QSlider(self.widget_2)
        self.lighter_switch.setGeometry(QtCore.QRect(380, 145, 41, 81))
        self.lighter_switch.setStyleSheet("")
        self.lighter_switch.setMaximum(1)
        self.lighter_switch.setSingleStep(1)
        self.lighter_switch.setPageStep(1)
        self.lighter_switch.setProperty("value", 0)
        self.lighter_switch.setTracking(False)
        self.lighter_switch.setOrientation(QtCore.Qt.Vertical)
        self.lighter_switch.setObjectName("lighter_switch")
        self.blue_color = QtWidgets.QLabel(self.widget_2)
        self.blue_color.setGeometry(QtCore.QRect(170, 60, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.blue_color.setFont(font)
        self.blue_color.setObjectName("blue_color")
        self.green_color = QtWidgets.QLabel(self.widget_2)
        self.green_color.setGeometry(QtCore.QRect(120, 180, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.green_color.setFont(font)
        self.green_color.setObjectName("green_color")
        self.blue_dot = QtWidgets.QLabel(self.widget_2)
        self.blue_dot.setGeometry(QtCore.QRect(320, 50, 121, 90))
        self.blue_dot.setStyleSheet("color: rgb(0, 0, 255);\n"
                                    "font: 72pt \"MS Shell Dlg 2\";")
        self.blue_dot.setObjectName("blue_dot")
        self.green_dot = QtWidgets.QLabel(self.widget_2)
        self.green_dot.setGeometry(QtCore.QRect(320, 150, 121, 90))
        self.green_dot.setStyleSheet("color: rgb(0, 170, 0);\n"
                                     "font: 72pt \"MS Shell Dlg 2\";")
        self.green_dot.setObjectName("green_dot")
        self.polarity_switch = QtWidgets.QSlider(self.widget_2)
        self.polarity_switch.setGeometry(QtCore.QRect(580, 230, 51, 31))
        self.polarity_switch.setMaximum(1)
        self.polarity_switch.setPageStep(1)
        self.polarity_switch.setOrientation(QtCore.Qt.Horizontal)
        self.polarity_switch.setObjectName("polarity_switch")
        self.polarity = QtWidgets.QLabel(self.widget_2)
        self.polarity.setGeometry(QtCore.QRect(510, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.polarity.setFont(font)
        self.polarity.setObjectName("polarity")
        self.polarity_plus = QtWidgets.QLabel(self.widget_2)
        self.polarity_plus.setGeometry(QtCore.QRect(620, 250, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.polarity_plus.setFont(font)
        self.polarity_plus.setObjectName("polarity_plus")
        self.polarity_minus = QtWidgets.QLabel(self.widget_2)
        self.polarity_minus.setGeometry(QtCore.QRect(510, 250, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.polarity_minus.setFont(font)
        self.polarity_minus.setObjectName("polarity_minus")
        self.lighter_2 = QtWidgets.QLabel(self.widget_2)
        self.lighter_2.setGeometry(QtCore.QRect(560, 480, 21, 41))
        self.lighter_2.setStyleSheet("font: 75 16pt \"Arial\";")
        self.lighter_2.setObjectName("lighter_2")
        self.lighter_4 = QtWidgets.QLabel(self.widget_2)
        self.lighter_4.setGeometry(QtCore.QRect(630, 480, 21, 41))
        self.lighter_4.setStyleSheet("font: 75 16pt \"Arial\";")
        self.lighter_4.setObjectName("lighter_4")

        self.lighter_3 = QtWidgets.QLabel(self.widget_2)
        self.lighter_3.setGeometry(QtCore.QRect(597, 400, 15, 32))
        self.lighter_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.lighter_3.setStyleSheet("font: 75 16pt \"Arial\";")
        self.lighter_3.setObjectName("lighter_3")
        self.lighter = QtWidgets.QLabel(self.widget_2)
        self.lighter.setGeometry(QtCore.QRect(510, 350, 171, 41))
        self.lighter.setStyleSheet("font: 75 14pt \"Arial\";")
        self.lighter.setObjectName("lighter")
        self.polarity_plus_dial = QtWidgets.QDial(self.widget_2)
        self.polarity_plus_dial.setGeometry(QtCore.QRect(300, 380, 151, 151))
        self.polarity_plus_dial.setMaximum(20000)
        self.polarity_plus_dial.setSingleStep(1)
        self.polarity_plus_dial.setPageStep(1)
        self.polarity_plus_dial.setProperty("value", 0)
        self.polarity_plus_dial.setSliderPosition(0)
        self.polarity_plus_dial.setOrientation(QtCore.Qt.Horizontal)
        self.polarity_plus_dial.setWrapping(False)
        self.polarity_plus_dial.setNotchTarget(3.699999999999999)
        self.polarity_plus_dial.setNotchesVisible(True)
        self.polarity_plus_dial.setObjectName("polarity_plus_dial")
        self.polarity_minus_dial = QtWidgets.QDial(self.widget_2)
        self.polarity_minus_dial.setGeometry(QtCore.QRect(70, 380, 151, 151))
        self.polarity_minus_dial.setMinimum(0)
        self.polarity_minus_dial.setMaximum(1000)
        self.polarity_minus_dial.setPageStep(1)
        self.polarity_minus_dial.setProperty("value", 0)
        self.polarity_minus_dial.setSliderPosition(0)
        self.polarity_minus_dial.setTracking(True)
        self.polarity_minus_dial.setOrientation(QtCore.Qt.Horizontal)
        self.polarity_minus_dial.setInvertedAppearance(False)
        self.polarity_minus_dial.setInvertedControls(False)
        self.polarity_minus_dial.setWrapping(False)
        self.polarity_minus_dial.setNotchesVisible(True)
        self.polarity_minus_dial.setObjectName("polarity_minus_dial")
        self.max_plus_polarity = QtWidgets.QLabel(self.widget_2)
        self.max_plus_polarity.setGeometry(QtCore.QRect(420, 510, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.max_plus_polarity.setFont(font)
        self.max_plus_polarity.setObjectName("max_plus_polarity")
        self.min_plus_polarity = QtWidgets.QLabel(self.widget_2)
        self.min_plus_polarity.setGeometry(QtCore.QRect(310, 510, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.min_plus_polarity.setFont(font)
        self.min_plus_polarity.setObjectName("min_plus_polarity")
        self.max_minus_polarity = QtWidgets.QLabel(self.widget_2)
        self.max_minus_polarity.setGeometry(QtCore.QRect(90, 510, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.max_minus_polarity.setFont(font)
        self.max_minus_polarity.setObjectName("max_minus_polarity")
        self.min_minus_polarity = QtWidgets.QLabel(self.widget_2)
        self.min_minus_polarity.setGeometry(QtCore.QRect(160, 510, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.min_minus_polarity.setFont(font)
        self.min_minus_polarity.setObjectName("min_minus_polarity")
        self.vkl_lighter = QtWidgets.QSlider(self.widget_2)
        self.vkl_lighter.setGeometry(QtCore.QRect(600, 70, 41, 61))
        self.vkl_lighter.setMaximum(1)
        self.vkl_lighter.setPageStep(1)
        self.vkl_lighter.setOrientation(QtCore.Qt.Vertical)
        self.vkl_lighter.setObjectName("vkl_lighter")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(570, 20, 91, 41))
        self.label_3.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(120, 530, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(370, 530, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lighter_5 = QtWidgets.QLabel(self.widget_2)
        self.lighter_5.setGeometry(QtCore.QRect(320, 350, 131, 41))
        self.lighter_5.setStyleSheet("font: 75 14pt \"Arial\";")
        self.lighter_5.setObjectName("lighter_5")
        self.lighter_6 = QtWidgets.QLabel(self.widget_2)
        self.lighter_6.setGeometry(QtCore.QRect(90, 350, 131, 41))
        self.lighter_6.setStyleSheet("font: 75 14pt \"Arial\";")
        self.lighter_6.setObjectName("lighter_6")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lighter_dial = QtWidgets.QDial(self.widget_2)
        self.lighter_dial.setGeometry(QtCore.QRect(565, 420, 81, 91))
        self.lighter_dial.setAutoFillBackground(False)
        self.lighter_dial.setMinimum(2)
        self.lighter_dial.setMaximum(4)
        self.lighter_dial.setSingleStep(2)
        self.lighter_dial.setPageStep(1)
        self.lighter_dial.setProperty("value", 2)
        self.lighter_dial.setOrientation(QtCore.Qt.Vertical)
        self.lighter_dial.setWrapping(False)
        self.lighter_dial.setNotchesVisible(False)
        self.lighter_dial.setObjectName("lighter_dial")
        self.green_dot.raise_()
        self.green_color.raise_()
        self.polarity.raise_()
        self.polarity_plus.raise_()
        self.polarity_minus.raise_()
        self.polarity_switch.raise_()
        self.lighter_2.raise_()
        self.lighter_4.raise_()
        self.lighter_3.raise_()
        self.lighter.raise_()
        self.min_plus_polarity.raise_()
        self.polarity_plus_dial.raise_()
        self.vkl_lighter.raise_()
        self.label_3.raise_()
        self.blue_color.raise_()
        self.blue_dot.raise_()
        self.lighter_switch.raise_()
        self.min_minus_polarity.raise_()
        self.polarity_minus_dial.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.max_plus_polarity.raise_()
        self.max_minus_polarity.raise_()
        self.lighter_dial.raise_()
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(730, 421, 421, 280))
        self.widget_3.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.widget_3.setObjectName("widget_3")
        self.voltmeter = QtWidgets.QLCDNumber(self.widget_3)
        self.voltmeter.setGeometry(QtCore.QRect(20, 80, 191, 121))
        self.voltmeter.setFrameShape(QtWidgets.QFrame.Box)
        self.voltmeter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voltmeter.setDigitCount(5)
        self.voltmeter.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.voltmeter.setProperty("value", 0.0)
        self.voltmeter.setObjectName("voltmeter")
        self.vkl_voltmeter = QtWidgets.QRadioButton(self.widget_3)
        self.vkl_voltmeter.setGeometry(QtCore.QRect(300, 210, 111, 51))
        self.vkl_voltmeter.setStyleSheet("font: 75 16pt \"Arial\";")
        self.vkl_voltmeter.setObjectName("vkl_voltmeter")

        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(100, 210, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_16 = QtWidgets.QLabel(self.widget_3)
        self.label_16.setGeometry(QtCore.QRect(230, 15, 201, 41))
        self.label_16.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label_16.setObjectName("label_16")
        self.label_16.raise_()
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(220, 0, 201, 31))
        self.label_17.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label_17.setObjectName("label_17")
        self.label_17.raise_()
        self.voltmeter.raise_()
        self.vkl_voltmeter.raise_()
        self.label_9.raise_()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-80, -40, 2131, 1080))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("физика/back.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.widget_2.raise_()
        self.widget.raise_()
        self.widget_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        ###############################################################
        self.Additional = QtWidgets.QLabel(self.centralwidget)
        self.Additional.setGeometry(QtCore.QRect(165, 40, 235, 31))
        self.Additional.setFont(font)
        self.Additional.setObjectName("Additional")
        self.Additional.raise_()

        self.InfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.InfoButton.setGeometry(QtCore.QRect(210, 80, 130, 28))
        self.InfoButton.setText("")
        self.InfoButton.setObjectName("InfoButton")
        self.InfoButton.raise_()

        self.InfoFon = QtWidgets.QWidget(self.centralwidget)
        self.InfoFon.setGeometry(QtCore.QRect(150, 30, 255, 91))
        self.InfoFon.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "")
        self.InfoFon.setObjectName("InfoFon")
        self.InfoFon.raise_()
        self.InfoFon.setObjectName("InfoFon")
        self.InfoFon.raise_()
        self.label_6.raise_()
        self.widget_2.raise_()
        self.widget.raise_()
        self.widget_3.raise_()
        self.InfoButton.raise_()
        self.Additional.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.polarity_minus_dial.valueChanged.connect(self.change_volt_minus)
        self.polarity_plus_dial.valueChanged.connect(self.change_volt_plus)
        self.verticalSlider_2.valueChanged.connect(self.change_volt_plus)
        self.verticalSlider_2.valueChanged.connect(self.change_volt_minus)
        self.lighter_dial.valueChanged.connect(self.change_volt_plus)
        self.lighter_dial.valueChanged.connect(self.change_volt_minus)
        self.lighter_switch.valueChanged.connect(self.change_volt_plus)
        self.lighter_switch.valueChanged.connect(self.change_volt_minus)
        self.polarity_switch.valueChanged.connect(self.change_volt_plus)
        self.polarity_switch.valueChanged.connect(self.change_volt_minus)
        self.vkl_lighter.valueChanged.connect(self.change_volt_plus)
        self.vkl_lighter.valueChanged.connect(self.change_volt_minus)
        self.vkl_voltmeter.clicked.connect(self.change_volt_plus)
        self.vkl_voltmeter.clicked.connect(self.change_volt_minus)
        self.radioButton_2.clicked.connect(self.change_volt_plus)
        self.radioButton_2.clicked.connect(self.change_volt_minus)

        self.radioButton_2.clicked.connect(self.Sound)

        self.InfoButton.clicked.connect(self.Information)
        self.vkl_voltmeter.clicked.connect(self.erase_vol_1)
        self.radioButton_2.clicked.connect(self.erase_vol_2)
        self.vkl_lighter.actionTriggered.connect(self.erase_vol_3)

        self.status = 1

    def Information(self):
        if not self.InfoButton.isChecked() and self.status:
            self.status = 0
            NewWindow = QtWidgets.QDialog()
            ui = Ui_Form()
            ui.setupUi(NewWindow)
            NewWindow.show()
            NewWindow.exec_()
            self.status = 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_fototok.setText(_translate("MainWindow", "Фототок 1 µА"))
        self.radioButton_2.setText(_translate("MainWindow", "  Сеть"))
        self.label_8.setText(_translate("MainWindow", "Пределы"))
        self.label_13.setText(_translate("MainWindow", "10"))
        self.label_14.setText(_translate("MainWindow", "1"))
        self.label_15.setText(_translate("MainWindow", "100"))
        self.blue_color.setText(_translate("MainWindow", "Синий "))
        self.green_color.setText(_translate("MainWindow", "Зеленый"))
        self.blue_dot.setText(_translate("MainWindow", "."))
        self.green_dot.setText(_translate("MainWindow", "."))
        self.polarity.setText(_translate("MainWindow", "Полярность S2"))
        self.polarity_plus.setText(_translate("MainWindow", "+"))
        self.polarity_minus.setText(_translate("MainWindow", "   -"))
        self.lighter_2.setText(_translate("MainWindow", "2"))
        self.lighter_4.setText(_translate("MainWindow", "4"))
        self.lighter_3.setText(_translate("MainWindow", "3"))
        self.lighter.setText(_translate("MainWindow", "Осветитель S3"))
        self.lighter_5.setText(_translate("MainWindow", "Ручка R1"))
        self.lighter_6.setText(_translate("MainWindow", "Ручка R3"))
        self.max_plus_polarity.setText(_translate("MainWindow", "20 "))
        self.min_plus_polarity.setText(_translate("MainWindow", "0"))
        self.max_minus_polarity.setText(_translate("MainWindow", "0"))
        self.min_minus_polarity.setText(_translate("MainWindow", "-1000"))
        self.label_3.setText(_translate("MainWindow", "  Сеть"))
        self.label_4.setText(_translate("MainWindow", "мВ"))
        self.label_5.setText(_translate("MainWindow", "В"))
        self.vkl_voltmeter.setText(_translate("MainWindow", "  Сеть"))
        self.label_9.setText(_translate("MainWindow", "В"))

        self.Additional.setText(_translate("MainWindow", "Схема Установки"))
        self.label_16.setText(_translate("MainWindow", "Вольтметр PU"))
        self.label_17.setText(_translate("MainWindow", "Амперметр PA"))



    def change_volt_plus(self):
        if self.vkl_lighter.value() == 1 and self.polarity_switch.value() == 1:  # плюс полярность
            if self.vkl_voltmeter.isChecked() and (
                    self.polarity_plus_dial.valueChanged or self.verticalSlider_2.valueChanged or self.lighter_dial.valueChanged or self.lighter_switch.valueChanged or self.polarity_switch.valueChanged):
                value = self.polarity_plus_dial.value()
                self.voltmeter.display(value * 0.001)

                if self.radioButton_2.isChecked() and self.lighter_dial.value() == 2 and self.lighter_switch.value() == 0:
                    z = ((-2 - math.exp(-(value * 0.001 - 2.55) * 0.4)) * 0.25 + 1.3) * 2.5
                    if self.verticalSlider_2.value() == 0:
                        self.lcdNumber_2.display(z * 100)
                    if self.verticalSlider_2.value() == 1:
                        self.lcdNumber_2.display(z * 1000)
                    if self.verticalSlider_2.value() == 2:
                        self.lcdNumber_2.display(z * 10000)

                if self.radioButton_2.isChecked() and self.lighter_dial.value() == 3 and self.lighter_switch.value() == 0:
                    z = ((-2 - math.exp(-(value * 0.001 - 2.55) * 0.4)) * 0.25 + 1.3) * 1.5
                    if self.verticalSlider_2.value() == 0:
                        self.lcdNumber_2.display(z * 100)
                    if self.verticalSlider_2.value() == 1:
                        self.lcdNumber_2.display(z * 1000)
                    if self.verticalSlider_2.value() == 2:
                        self.lcdNumber_2.display(z * 10000)

                if self.radioButton_2.isChecked() and self.lighter_dial.value() == 4 and self.lighter_switch.value() == 0:
                    z = ((-2 - math.exp(-(value * 0.001 - 2.55) * 0.4)) * 0.25 + 1.3) * 0.75
                    if self.verticalSlider_2.value() == 0:
                        self.lcdNumber_2.display(z * 100)
                    if self.verticalSlider_2.value() == 1:
                        self.lcdNumber_2.display(z * 1000)
                    if self.verticalSlider_2.value() == 2:
                        self.lcdNumber_2.display(z * 10000)

                if self.radioButton_2.isChecked() and self.lighter_dial.value() == 2 and self.lighter_switch.value() == 1:
                    z = ((-2 - math.exp(-(value * 0.001 - 2.55) * 0.4)) * 0.25 + 1.3) * 2.087
                    if self.verticalSlider_2.value() == 0:
                        self.lcdNumber_2.display(z * 100)
                    if self.verticalSlider_2.value() == 1:
                        self.lcdNumber_2.display(z * 1000)
                    if self.verticalSlider_2.value() == 2:
                        self.lcdNumber_2.display(z * 10000)

                if self.radioButton_2.isChecked() and self.lighter_dial.value() == 3 and self.lighter_switch.value() == 1:
                    z = ((-2 - math.exp(-(value * 0.001 - 2.55) * 0.4)) * 0.25 + 1.3) * 1.2525
                    if self.verticalSlider_2.value() == 0:
                        self.lcdNumber_2.display(z * 100)
                    if self.verticalSlider_2.value() == 1:
                        self.lcdNumber_2.display(z * 1000)
                    if self.verticalSlider_2.value() == 2:
                        self.lcdNumber_2.display(z * 10000)

                if self.radioButton_2.isChecked() and self.lighter_dial.value() == 4 and self.lighter_switch.value() == 1:
                    z = ((-2 - math.exp(-(value * 0.001 - 2.55) * 0.4)) * 0.25 + 1.3) * 0.62625
                    if self.verticalSlider_2.value() == 0:
                        self.lcdNumber_2.display(z * 100)
                    if self.verticalSlider_2.value() == 1:
                        self.lcdNumber_2.display(z * 1000)
                    if self.verticalSlider_2.value() == 2:
                        self.lcdNumber_2.display(z * 10000)

    def change_volt_minus(self):  # минус полярность
        if self.vkl_lighter.value() == 1 and self.polarity_switch.value() == 0 and self.lighter_switch.value() == 0:
            if self.vkl_voltmeter.isChecked() and (
                    self.polarity_minus_dial.valueChanged or self.verticalSlider_2.valueChanged or self.lighter_dial.valueChanged or self.lighter_switch.valueChanged or self.polarity_switch.valueChanged):
                value = -self.polarity_minus_dial.value()
                # if value == 0:
                #     self.voltmeter.display(0)
                # else:
                self.voltmeter.display(value)

                if self.radioButton_2.isChecked():
                    z = ((-2 - math.exp(-(value * 0.001 - 2.55) * 0.4)) * 0.25 + 1.3) * 2.5
                    # if z < 0:
                    #     self.lcdNumber_2.display(0)
                    # if z == 0:
                    #     self.lcdNumber_2.display(z)
                    #     self.voltmeter.display((value + random.randint(0, 50))*1000)
                    # if z > 0:
                    if -358 >= value >= -360:
                        z=0
                        self.lcdNumber_2.display(0)
                    elif z < 0:
                        z = -0.002  #################################################################
                        if self.verticalSlider_2.value() == 0:
                            self.lcdNumber_2.display(z * 100)
                        if self.verticalSlider_2.value() == 1:
                            self.lcdNumber_2.display(z * 1000)
                        if self.verticalSlider_2.value() == 2:
                            self.lcdNumber_2.display(z * 10000)
                    else:
                        if self.verticalSlider_2.value() == 0:
                            self.lcdNumber_2.display(z * 100)
                        if self.verticalSlider_2.value() == 1:
                            self.lcdNumber_2.display(z * 1000)
                        if self.verticalSlider_2.value() == 2:
                            self.lcdNumber_2.display(z * 10000)

        if self.vkl_lighter.value() == 1 and self.polarity_switch.value() == 0 and self.lighter_switch.value() == 1:
            if self.vkl_voltmeter.isChecked() and (self.polarity_minus_dial.valueChanged or self.verticalSlider_2.valueChanged or self.lighter_dial.valueChanged or self.lighter_switch.valueChanged or self.polarity_switch.valueChanged):
                value = -self.polarity_minus_dial.value()
                self.voltmeter.display(value)

                if self.radioButton_2.isChecked():
                    z = ((-2 - math.exp(-(value * 0.001 - 2.5) * 0.4)) * 0.25 + 1.3) * 2.5
                    if -408 >= value >= -410:
                        z=0
                        self.lcdNumber_2.display(0)
                    if z < 0:
                        z = -0.002  #################################################################
                        if self.verticalSlider_2.value() == 0:
                            self.lcdNumber_2.display(z * 100)
                        if self.verticalSlider_2.value() == 1:
                            self.lcdNumber_2.display(z * 1000)
                        if self.verticalSlider_2.value() == 2:
                            self.lcdNumber_2.display(z * 10000)
                    else:
                        if self.verticalSlider_2.value() == 0:
                            self.lcdNumber_2.display(z * 100)
                        if self.verticalSlider_2.value() == 1:
                            self.lcdNumber_2.display(z * 1000)
                        if self.verticalSlider_2.value() == 2:
                            self.lcdNumber_2.display(z * 10000)

    def erase_vol_1(self):
        self.voltmeter.display(0)

    def erase_vol_2(self):
        self.lcdNumber_2.display(0)

    def erase_vol_3(self):
        self.lcdNumber_2.display(0)
        self.voltmeter.display(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
