# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendario.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calender(object):
    def setupUi(self, Calender):
        Calender.setObjectName("Calender")
        Calender.resize(326, 186)
        self.calendarWidget = QtWidgets.QCalendarWidget(Calender)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 0, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Calender)
        QtCore.QMetaObject.connectSlotsByName(Calender)

    def retranslateUi(self, Calender):
        _translate = QtCore.QCoreApplication.translate
        Calender.setWindowTitle(_translate("Calender", "Fecha alta"))