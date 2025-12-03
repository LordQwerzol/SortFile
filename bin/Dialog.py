# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class CustomMessageBox(QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgb(153, 180, 209); color:rgb(0, 0, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/lexa/SortFile/img/Setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
    
    def show_question_box(self, title, text):
        self.setWindowTitle(title)
        self.setText(text)
        self.setStandardButtons(QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        self.setIcon(QMessageBox.Question)
        retval = self.exec_()
        return retval == QtWidgets.QMessageBox.Yes
    
    def show_warning_box(self, title, text):
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.exec_()

    def show_information_box(self, title, text):
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(QMessageBox.Information)
        self.exec_()
