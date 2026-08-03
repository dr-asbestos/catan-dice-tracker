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
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 575)
        MainWindow.setMinimumSize(QSize(450, 575))
        MainWindow.setMaximumSize(QSize(450, 575))
        MainWindow.setWindowTitle(u"Catan Dice Tracker")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableDiceStats = QTableWidget(self.centralwidget)
        self.tableDiceStats.setObjectName(u"tableDiceStats")
        self.tableDiceStats.setGeometry(QRect(130, 120, 207, 356))
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
        self.tableDiceStats.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableDiceStats.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableDiceStats.setSupportedDragActions(Qt.DropAction.IgnoreAction)
        self.tableDiceStats.verticalHeader().setVisible(False)
        self.labelRollStatsStatic = QLabel(self.centralwidget)
        self.labelRollStatsStatic.setObjectName(u"labelRollStatsStatic")
        self.labelRollStatsStatic.setGeometry(QRect(130, 80, 146, 29))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.labelRollStatsStatic.setFont(font1)
        self.labelRollStatsStatic.setText(u"Roll statistics:")
        self.labelRollsStatic = QLabel(self.centralwidget)
        self.labelRollsStatic.setObjectName(u"labelRollsStatic")
        self.labelRollsStatic.setGeometry(QRect(20, 80, 82, 58))
        self.labelRollsStatic.setFont(font1)
        self.labelRollsStatic.setText(u"Entered\n"
"rolls:")
        self.listRolls = QListWidget(self.centralwidget)
        self.listRolls.setObjectName(u"listRolls")
        self.listRolls.setGeometry(QRect(20, 140, 51, 351))
        font2 = QFont()
        font2.setPointSize(12)
        self.listRolls.setFont(font2)
        self.listRolls.setFrameShape(QFrame.Shape.Box)
        self.listRolls.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listRolls.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listRolls.setAlternatingRowColors(True)
        self.listRolls.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.listRolls.setMovement(QListView.Movement.Free)
        self.listRolls.setSpacing(2)
        self.listRolls.setSupportedDragActions(Qt.DropAction.IgnoreAction)
        self.labelNewRollStatic = QLabel(self.centralwidget)
        self.labelNewRollStatic.setObjectName(u"labelNewRollStatic")
        self.labelNewRollStatic.setGeometry(QRect(30, 30, 99, 29))
        self.labelNewRollStatic.setFont(font1)
        self.labelNewRollStatic.setText(u"New roll:")
        self.buttonNewRoll = QPushButton(self.centralwidget)
        self.buttonNewRoll.setObjectName(u"buttonNewRoll")
        self.buttonNewRoll.setGeometry(QRect(180, 30, 71, 31))
        self.buttonNewRoll.setFont(font2)
        self.buttonNewRoll.setText(u"Enter")
        self.lineNewRoll = QLineEdit(self.centralwidget)
        self.lineNewRoll.setObjectName(u"lineNewRoll")
        self.lineNewRoll.setGeometry(QRect(140, 30, 31, 31))
        self.lineNewRoll.setFont(font2)
        self.lineNewRoll.setMaxLength(2)
        self.buttonDeleteLastRoll = QPushButton(self.centralwidget)
        self.buttonDeleteLastRoll.setObjectName(u"buttonDeleteLastRoll")
        self.buttonDeleteLastRoll.setGeometry(QRect(10, 510, 131, 31))
        self.buttonDeleteLastRoll.setFont(font2)
        self.buttonDeleteLastRoll.setText(u"Delete last Roll")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        pass
    # retranslateUi

