# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1209, 445)
        MainWindow.setMinimumSize(QSize(315, 445))
        MainWindow.setMaximumSize(QSize(1315, 445))
        MainWindow.setWindowTitle(u"Catan Dice Tracker")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableDiceStats = QTableWidget(self.centralwidget)
        self.tableDiceStats.setObjectName(u"tableDiceStats")
        self.tableDiceStats.setGeometry(QRect(190, 80, 1011, 356))
        font = QFont()
        font.setPointSize(10)
        self.tableDiceStats.setFont(font)
        self.tableDiceStats.setFrameShape(QFrame.Shape.Box)
        self.tableDiceStats.setLineWidth(1)
        self.tableDiceStats.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableDiceStats.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableDiceStats.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableDiceStats.setTabKeyNavigation(False)
        self.tableDiceStats.setProperty(u"showDropIndicator", False)
        self.tableDiceStats.setDragDropOverwriteMode(False)
        self.tableDiceStats.setAlternatingRowColors(True)
        self.tableDiceStats.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableDiceStats.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableDiceStats.setSupportedDragActions(Qt.DropAction.IgnoreAction)
        self.tableDiceStats.horizontalHeader().setMinimumSectionSize(10)
        self.tableDiceStats.verticalHeader().setVisible(False)
        self.labelRollStatsStatic = QLabel(self.centralwidget)
        self.labelRollStatsStatic.setObjectName(u"labelRollStatsStatic")
        self.labelRollStatsStatic.setGeometry(QRect(190, 50, 146, 29))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.labelRollStatsStatic.setFont(font1)
        self.labelRollStatsStatic.setText(u"Roll statistics:")
        self.labelRollsStatic = QLabel(self.centralwidget)
        self.labelRollsStatic.setObjectName(u"labelRollsStatic")
        self.labelRollsStatic.setGeometry(QRect(10, 50, 169, 29))
        self.labelRollsStatic.setFont(font1)
        self.labelRollsStatic.setText(u"Rolls and Yields:")
        self.labelNewRollStatic = QLabel(self.centralwidget)
        self.labelNewRollStatic.setObjectName(u"labelNewRollStatic")
        self.labelNewRollStatic.setGeometry(QRect(10, 10, 99, 29))
        self.labelNewRollStatic.setFont(font1)
        self.labelNewRollStatic.setText(u"New roll:")
        self.buttonNewRoll = QPushButton(self.centralwidget)
        self.buttonNewRoll.setObjectName(u"buttonNewRoll")
        self.buttonNewRoll.setGeometry(QRect(150, 10, 61, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.buttonNewRoll.setFont(font2)
        self.buttonNewRoll.setText(u"Enter")
        self.lineNewRoll = QLineEdit(self.centralwidget)
        self.lineNewRoll.setObjectName(u"lineNewRoll")
        self.lineNewRoll.setGeometry(QRect(110, 10, 31, 31))
        self.lineNewRoll.setFont(font2)
        self.lineNewRoll.setMaxLength(2)
        self.buttonDeleteLastRoll = QPushButton(self.centralwidget)
        self.buttonDeleteLastRoll.setObjectName(u"buttonDeleteLastRoll")
        self.buttonDeleteLastRoll.setGeometry(QRect(220, 10, 91, 31))
        self.buttonDeleteLastRoll.setFont(font2)
        self.buttonDeleteLastRoll.setText(u"Del last roll")
        self.tableRolls = QTableWidget(self.centralwidget)
        self.tableRolls.setObjectName(u"tableRolls")
        self.tableRolls.setGeometry(QRect(10, 80, 171, 356))
        self.tableRolls.setFont(font)
        self.tableRolls.setFrameShape(QFrame.Shape.Box)
        self.tableRolls.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableRolls.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableRolls.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableRolls.setTabKeyNavigation(False)
        self.tableRolls.setProperty(u"showDropIndicator", False)
        self.tableRolls.setDragDropOverwriteMode(False)
        self.tableRolls.setAlternatingRowColors(True)
        self.tableRolls.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableRolls.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableRolls.setSupportedDragActions(Qt.DropAction.IgnoreAction)
        self.tableRolls.horizontalHeader().setMinimumSectionSize(10)
        self.tableRolls.verticalHeader().setVisible(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        pass
    # retranslateUi

