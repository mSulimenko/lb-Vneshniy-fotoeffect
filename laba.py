# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laba.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(570, 170, 241, 121))
        self.widget.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                  "")
        self.widget.setObjectName("widget")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(30, 20, 100, 40))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.name_fototok = QtWidgets.QLabel(self.widget)
        self.name_fototok.setGeometry(QtCore.QRect(45, 70, 71, 16))
        self.name_fototok.setObjectName("name_fototok")
        self.limit_tok_dial = QtWidgets.QDial(self.widget)
        self.limit_tok_dial.setGeometry(QtCore.QRect(170, 20, 50, 64))
        self.limit_tok_dial.setMinimum(999)
        self.limit_tok_dial.setMaximum(999)
        self.limit_tok_dial.setWrapping(True)
        self.limit_tok_dial.setObjectName("limit_tok_dial")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lcdNumber_2.raise_()
        self.name_fototok.raise_()
        self.limit_tok_dial.raise_()
        self.label_2.raise_()
        self.radioButton_2.raise_()
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(40, 170, 481, 281))
        self.widget_2.setWhatsThis("")
        self.widget_2.setStyleSheet("background-color: rgb(136, 136, 136);\n"
                                    "border-color: rgb(45, 45, 45);")
        self.widget_2.setObjectName("widget_2")
        self.lighter_switch = QtWidgets.QSlider(self.widget_2)
        self.lighter_switch.setGeometry(QtCore.QRect(90, 30, 22, 61))
        self.lighter_switch.setStyleSheet("")
        self.lighter_switch.setMaximum(1)
        self.lighter_switch.setSingleStep(1)
        self.lighter_switch.setPageStep(1)
        self.lighter_switch.setProperty("value", 0)
        self.lighter_switch.setTracking(False)
        self.lighter_switch.setOrientation(QtCore.Qt.Vertical)
        self.lighter_switch.setObjectName("lighter_switch")
        self.blue_color = QtWidgets.QLabel(self.widget_2)
        self.blue_color.setGeometry(QtCore.QRect(20, 20, 51, 21))
        self.blue_color.setObjectName("blue_color")
        self.green_color = QtWidgets.QLabel(self.widget_2)
        self.green_color.setGeometry(QtCore.QRect(20, 70, 47, 21))
        self.green_color.setObjectName("green_color")
        self.blue_dot = QtWidgets.QLabel(self.widget_2)
        self.blue_dot.setGeometry(QtCore.QRect(50, -50, 111, 101))
        self.blue_dot.setStyleSheet("color: rgb(0, 0, 255);\n"
                                    "font: 72pt \"MS Shell Dlg 2\";")
        self.blue_dot.setObjectName("blue_dot")
        self.green_dot = QtWidgets.QLabel(self.widget_2)
        self.green_dot.setGeometry(QtCore.QRect(60, 0, 111, 101))
        self.green_dot.setStyleSheet("color: rgb(0, 170, 0);\n"
                                     "font: 72pt \"MS Shell Dlg 2\";")
        self.green_dot.setObjectName("green_dot")
        self.polarity_switch = QtWidgets.QSlider(self.widget_2)
        self.polarity_switch.setGeometry(QtCore.QRect(280, 210, 31, 22))
        self.polarity_switch.setMaximum(1)
        self.polarity_switch.setPageStep(1)
        self.polarity_switch.setOrientation(QtCore.Qt.Horizontal)
        self.polarity_switch.setObjectName("polarity_switch")
        self.polarity = QtWidgets.QLabel(self.widget_2)
        self.polarity.setGeometry(QtCore.QRect(270, 180, 61, 20))
        self.polarity.setObjectName("polarity")
        self.polarity_plus = QtWidgets.QLabel(self.widget_2)
        self.polarity_plus.setGeometry(QtCore.QRect(320, 214, 47, 13))
        self.polarity_plus.setObjectName("polarity_plus")
        self.polarity_minus = QtWidgets.QLabel(self.widget_2)
        self.polarity_minus.setGeometry(QtCore.QRect(260, 214, 51, 16))
        self.polarity_minus.setObjectName("polarity_minus")
        self.lighter_dial = QtWidgets.QDial(self.widget_2)
        self.lighter_dial.setGeometry(QtCore.QRect(400, 190, 50, 64))
        self.lighter_dial.setAutoFillBackground(False)
        self.lighter_dial.setMinimum(1)
        self.lighter_dial.setMaximum(4)
        self.lighter_dial.setSingleStep(2)
        self.lighter_dial.setPageStep(1)
        self.lighter_dial.setProperty("value", 4)
        self.lighter_dial.setOrientation(QtCore.Qt.Vertical)
        self.lighter_dial.setWrapping(False)
        self.lighter_dial.setNotchesVisible(False)
        self.lighter_dial.setObjectName("lighter_dial")
        self.lighter_1 = QtWidgets.QLabel(self.widget_2)
        self.lighter_1.setGeometry(QtCore.QRect(400, 240, 47, 13))
        self.lighter_1.setObjectName("lighter_1")
        self.lighter_4 = QtWidgets.QLabel(self.widget_2)
        self.lighter_4.setGeometry(QtCore.QRect(450, 240, 47, 13))
        self.lighter_4.setObjectName("lighter_4")
        self.lighter_2 = QtWidgets.QLabel(self.widget_2)
        self.lighter_2.setGeometry(QtCore.QRect(400, 200, 47, 13))
        self.lighter_2.setObjectName("lighter_2")
        self.lighter_3 = QtWidgets.QLabel(self.widget_2)
        self.lighter_3.setGeometry(QtCore.QRect(450, 200, 47, 13))
        self.lighter_3.setObjectName("lighter_3")
        self.lighter = QtWidgets.QLabel(self.widget_2)
        self.lighter.setGeometry(QtCore.QRect(400, 180, 61, 16))
        self.lighter.setObjectName("lighter")
        self.polarity_plus_dial = QtWidgets.QDial(self.widget_2)
        self.polarity_plus_dial.setGeometry(QtCore.QRect(150, 190, 50, 64))
        self.polarity_plus_dial.setMaximum(200)
        self.polarity_plus_dial.setSingleStep(1)
        self.polarity_plus_dial.setPageStep(1)
        self.polarity_plus_dial.setProperty("value", 0)
        self.polarity_plus_dial.setSliderPosition(0)
        self.polarity_plus_dial.setWrapping(False)
        self.polarity_plus_dial.setNotchesVisible(True)
        self.polarity_plus_dial.setObjectName("polarity_plus_dial")
        self.polarity_minus_dial = QtWidgets.QDial(self.widget_2)
        self.polarity_minus_dial.setGeometry(QtCore.QRect(40, 190, 50, 64))
        self.polarity_minus_dial.setMinimum(-1)
        self.polarity_minus_dial.setMaximum(0)
        self.polarity_minus_dial.setPageStep(1)
        self.polarity_minus_dial.setProperty("value", 0)
        self.polarity_minus_dial.setSliderPosition(0)
        self.polarity_minus_dial.setTracking(False)
        self.polarity_minus_dial.setOrientation(QtCore.Qt.Horizontal)
        self.polarity_minus_dial.setInvertedAppearance(False)
        self.polarity_minus_dial.setInvertedControls(False)
        self.polarity_minus_dial.setWrapping(False)
        self.polarity_minus_dial.setNotchesVisible(True)
        self.polarity_minus_dial.setObjectName("polarity_minus_dial")
        self.max_plus_polarity = QtWidgets.QLabel(self.widget_2)
        self.max_plus_polarity.setGeometry(QtCore.QRect(190, 240, 47, 13))
        self.max_plus_polarity.setObjectName("max_plus_polarity")
        self.min_plus_polarity = QtWidgets.QLabel(self.widget_2)
        self.min_plus_polarity.setGeometry(QtCore.QRect(150, 240, 47, 13))
        self.min_plus_polarity.setObjectName("min_plus_polarity")
        self.max_minus_polarity = QtWidgets.QLabel(self.widget_2)
        self.max_minus_polarity.setGeometry(QtCore.QRect(80, 240, 47, 13))
        self.max_minus_polarity.setObjectName("max_minus_polarity")
        self.min_minus_polarity = QtWidgets.QLabel(self.widget_2)
        self.min_minus_polarity.setGeometry(QtCore.QRect(40, 240, 47, 13))
        self.min_minus_polarity.setObjectName("min_minus_polarity")
        self.vkl_lighter = QtWidgets.QSlider(self.widget_2)
        self.vkl_lighter.setGeometry(QtCore.QRect(420, 80, 22, 51))
        self.vkl_lighter.setMaximum(1)
        self.vkl_lighter.setPageStep(1)
        self.vkl_lighter.setOrientation(QtCore.Qt.Vertical)
        self.vkl_lighter.setObjectName("vkl_lighter")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(410, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.blue_color.raise_()
        self.green_dot.raise_()
        self.green_color.raise_()
        self.blue_dot.raise_()
        self.lighter_switch.raise_()
        self.polarity.raise_()
        self.polarity_plus.raise_()
        self.polarity_minus.raise_()
        self.polarity_switch.raise_()
        self.lighter_1.raise_()
        self.lighter_4.raise_()
        self.lighter_2.raise_()
        self.lighter_3.raise_()
        self.lighter.raise_()
        self.lighter_dial.raise_()
        self.min_plus_polarity.raise_()
        self.max_plus_polarity.raise_()
        self.min_minus_polarity.raise_()
        self.max_minus_polarity.raise_()
        self.polarity_minus_dial.raise_()
        self.polarity_plus_dial.raise_()
        self.vkl_lighter.raise_()
        self.label_3.raise_()
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(569, 330, 241, 121))
        self.widget_3.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.widget_3.setObjectName("widget_3")
        self.voltmeter = QtWidgets.QLCDNumber(self.widget_3)
        self.voltmeter.setGeometry(QtCore.QRect(30, 20, 100, 40))
        self.voltmeter.setSmallDecimalPoint(False)
        self.voltmeter.setDigitCount(5)
        self.voltmeter.setProperty("value", 0.0)
        self.voltmeter.setObjectName("voltmeter")
        self.limit_volt_dial = QtWidgets.QDial(self.widget_3)
        self.limit_volt_dial.setGeometry(QtCore.QRect(170, 20, 50, 64))
        self.limit_volt_dial.setWrapping(False)
        self.limit_volt_dial.setObjectName("limit_volt_dial")
        self.vkl_voltmeter = QtWidgets.QRadioButton(self.widget_3)
        self.vkl_voltmeter.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.vkl_voltmeter.setObjectName("vkl_voltmeter")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label.setObjectName("label")
        self.label.raise_()
        self.voltmeter.raise_()
        self.limit_volt_dial.raise_()
        self.vkl_voltmeter.raise_()
        self.widget_2.raise_()
        self.widget.raise_()
        self.widget_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.polarity_plus_dial.valueChanged.connect(self.change_volt_plus)
        self.polarity_minus_dial.valueChanged.connect(self.change_volt_minus)
        self.vkl_voltmeter.toggled.connect(self.vkl_volt)
        # self.voltmeter..connect

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_fototok.setText(_translate("MainWindow", "Фототок 1мА"))
        self.radioButton_2.setText(_translate("MainWindow", "  Сеть"))
        self.label_2.setText(_translate("MainWindow", "Сделано в СССР"))
        self.blue_color.setText(_translate("MainWindow", "Синий "))
        self.green_color.setText(_translate("MainWindow", "Зеленый"))
        self.blue_dot.setText(_translate("MainWindow", "."))
        self.green_dot.setText(_translate("MainWindow", "."))
        self.polarity.setText(_translate("MainWindow", "Полярность"))
        self.polarity_plus.setText(_translate("MainWindow", "+"))
        self.polarity_minus.setText(_translate("MainWindow", "   -"))
        self.lighter_1.setText(_translate("MainWindow", "1"))
        self.lighter_4.setText(_translate("MainWindow", "4"))
        self.lighter_2.setText(_translate("MainWindow", "2"))
        self.lighter_3.setText(_translate("MainWindow", "3"))
        self.lighter.setText(_translate("MainWindow", "Освеитель"))
        self.max_plus_polarity.setText(_translate("MainWindow", "20 В"))
        self.min_plus_polarity.setText(_translate("MainWindow", "0"))
        self.max_minus_polarity.setText(_translate("MainWindow", "0"))
        self.min_minus_polarity.setText(_translate("MainWindow", "-1 В"))
        self.label_3.setText(_translate("MainWindow", "  Сеть"))
        self.vkl_voltmeter.setText(_translate("MainWindow", "  Сеть"))
        self.label.setText(_translate("MainWindow", "Сделано в СССР"))

    def change_volt_minus(self):
            value = 0
            if self.vkl_voltmeter.isChecked() and self.polarity_minus_dial.valueChanged:
                value = self.polarity_minus_dial.value()
                self.voltmeter.display(value)


    def change_volt_plus(self):
        value = 0
        if self.vkl_voltmeter.isChecked() and self.polarity_plus_dial.valueChanged:
            value = self.polarity_plus_dial.value()
            self.voltmeter.display(value)


    def vkl_volt(self):
        value = self.polarity_plus_dial.value()
        if self.vkl_voltmeter.isChecked():
            value = self.polarity_plus_dial.value()
            self.voltmeter.display(value)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())