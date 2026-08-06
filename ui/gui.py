from PySide6.QtWidgets import (QMainWindow, QHeaderView, QTableWidgetItem, \
                               QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator, QColor

from .mainwindow import Ui_MainWindow as mainGUIform


class GUIMain(QMainWindow):
    '''
    todo write me
    '''
    def __init__(self, cache):
        '''
        todo write me
        '''
        super(GUIMain, self).__init__()
        self.ui = mainGUIform()
        self.ui.setupUi(self)

        self.refTracker = cache.tracker

        # =====================================================================
        # Dice Stats table construction
        # =====================================================================

        # column names and widths
        self.tableDiceStatsHeader = {
            'Dice': 40,
            'Rolls': 40,
            'Diffs': 55,
            'Luck': 60,
            'P1': 22,
            'P1 Yield': 60,
            'P1 Diffs': 60,
            'P1 Luck': 60,
            'P2': 22,
            'P2 Yield': 60,
            'P2 Diffs': 60,
            'P2 Luck': 60,
            'P3': 22,
            'P3 Yield': 60,
            'P3 Diffs': 60,
            'P3 Luck': 60,
            'P4': 22,
            'P4 Yield': 60,
            'P4 Diffs': 60,
            'P4 Luck': 60,
        }
        # column and row settings
        self.ui.tableDiceStats.setColumnCount(len(self.tableDiceStatsHeader))
        self.ui.tableDiceStats.setHorizontalHeaderLabels(self.tableDiceStatsHeader.keys())
        self.ui.tableDiceStats.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableDiceStats.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        for i, w in enumerate(self.tableDiceStatsHeader.values()):
            self.ui.tableDiceStats.setColumnWidth(i, w)

        for i in range(11):
            self.ui.tableDiceStats.insertRow(i)
            for j in range(len(self.tableDiceStatsHeader)):
                self.ui.tableDiceStats.setItem(i, j, QTableWidgetItem())
                self.ui.tableDiceStats.item(i, j).setTextAlignment(Qt.AlignCenter)
            self.ui.tableDiceStats.item(i, 0).setText(str(i+2))
            self.ui.tableDiceStats.item(i, 4).setCheckState(Qt.Unchecked)
            self.ui.tableDiceStats.item(i, 8).setCheckState(Qt.Unchecked)
            self.ui.tableDiceStats.item(i, 12).setCheckState(Qt.Unchecked)
            self.ui.tableDiceStats.item(i, 16).setCheckState(Qt.Unchecked)
            if i == 5: # for 7 roll
                self.ui.tableDiceStats.item(i, 4).setFlags(Qt.ItemIsEnabled)
                self.ui.tableDiceStats.item(i, 8).setFlags(Qt.ItemIsEnabled)
                self.ui.tableDiceStats.item(i, 12).setFlags(Qt.ItemIsEnabled)
                self.ui.tableDiceStats.item(i, 16).setFlags(Qt.ItemIsEnabled)

        # =====================================================================
        # Rolls table construction
        # =====================================================================

        self.tableRollsHeader = {
            'Roll': 35,
            'P1': 25,
            'P2': 25,
            'P3': 25,
            'P4': 25
        }
        # column and row settings
        self.ui.tableRolls.setColumnCount(len(self.tableRollsHeader))
        self.ui.tableRolls.setHorizontalHeaderLabels(self.tableRollsHeader.keys())
        self.ui.tableRolls.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableRolls.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        for i, w in enumerate(self.tableRollsHeader.values()):
            self.ui.tableRolls.setColumnWidth(i, w)

        
        # =====================================================================
        # Events Stitching and Other Adjustments
        # =====================================================================
        
        self.ui.tableDiceStats.cellChanged.connect(self.lockInDice)
        self.ui.buttonDeleteLastRoll.clicked.connect(self.deleteLastRoll)
        self.ui.buttonNewRoll.clicked.connect(self.newRoll)
        self.ui.lineNewRoll.editingFinished.connect(self.newRoll)
        self.ui.lineNewRoll.setValidator(QIntValidator(2, 12))

        self.updateFields()


    def closeEvent(self, event):
        '''
        Class method override. Promps the user before closing the application 
        and all child windows.
        '''
        result = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', 
                                      QMessageBox.Yes, QMessageBox.Cancel)
        if result == QMessageBox.Yes:
            event.accept() 
        else:
            event.ignore()


    def updateFields(self, roll=None):
        '''
        todo write me
        '''
        self.ui.lineNewRoll.clear()

        self.ui.tableDiceStats.cellChanged.disconnect(self.lockInDice)
        for i in range(11):
            self.ui.tableDiceStats.item(i, 1).setText(f'{self.refTracker.sampleRolls[i+2]}')
            self.ui.tableDiceStats.item(i, 2).setText(f'{self.refTracker.rollDiffs[i+2]:+.2f}')
            self.ui.tableDiceStats.item(i, 2).setBackground(self.interpolateColour(self.refTracker.rollDiffs[i+2], -2, 2))
            self.ui.tableDiceStats.item(i, 3).setText(f'{self.refTracker.luckDiffs[i+2]:+.2%}')
            self.ui.tableDiceStats.item(i, 3).setBackground(self.interpolateColour(self.refTracker.luckDiffs[i+2], -.1, .1))

            for p in (0,1,2,3):
                self.ui.tableDiceStats.item(i, 4*p+5).setText(f'{self.refTracker.playerYields[p][i+2]}')
                self.ui.tableDiceStats.item(i, 4*p+6).setText(f'{self.refTracker.playerYieldDiffs[p][i+2]:+.2f}')
                self.ui.tableDiceStats.item(i, 4*p+6).setBackground(self.interpolateColour(self.refTracker.playerYieldDiffs[p][i+2], -2, 2))
                self.ui.tableDiceStats.item(i, 4*p+7).setText(f'{self.refTracker.playerYieldLuck[p][i+2]:+.2%}')
                self.ui.tableDiceStats.item(i, 4*p+7).setBackground(self.interpolateColour(self.refTracker.playerYieldLuck[p][i+2], -.1, .1))

        self.ui.tableDiceStats.cellChanged.connect(self.lockInDice)

        if roll is not None:
            i = self.ui.tableRolls.rowCount()
            self.ui.tableRolls.insertRow(i)
            self.ui.tableRolls.scrollToBottom()
            for j in range(len(self.tableRollsHeader)):
                self.ui.tableRolls.setItem(i, j, QTableWidgetItem())
                self.ui.tableRolls.item(i, j).setTextAlignment(Qt.AlignCenter)
                if j == 0:
                    self.ui.tableRolls.item(i, j).setText(str(roll[0]))
                else:
                    self.ui.tableRolls.item(i, j).setText('\u2714' if roll[1][j-1] else '\u2717')
                    self.ui.tableRolls.item(i, j).setBackground(QColor('lightgreen') if roll[1][j-1] else QColor('lightcoral'))


    def interpolateColour(self, val, minLim, maxLim):
        '''
        todo write me
        '''
        ratio = max(0.0, min(1.0, (val - minLim) / (maxLim - minLim)))
        colourMin = QColor('lightcoral')
        colourMax = QColor('lightgreen')

        return QColor(int(colourMin.red() + ratio * (colourMax.red() - colourMin.red())), \
                      int(colourMin.green() + ratio * (colourMax.green() - colourMin.green())), \
                      int(colourMin.blue() + ratio * (colourMax.blue() - colourMin.blue())))


    def newRoll(self):
        '''
        todo write me
        '''
        try:
            dice = None
            dice = int(self.ui.lineNewRoll.text())
            if not (2 <= dice <= 12):
                raise
        except:
            print(f'Invalid dice: {dice}')
        else:
            roll = (dice, 
                    (self.ui.tableDiceStats.item(dice-2, 4).checkState() == Qt.Checked,
                     self.ui.tableDiceStats.item(dice-2, 8).checkState() == Qt.Checked,
                     self.ui.tableDiceStats.item(dice-2, 12).checkState() == Qt.Checked,
                     self.ui.tableDiceStats.item(dice-2, 16).checkState() == Qt.Checked))
            self.refTracker.newRoll(roll)
            self.updateFields(roll)
        

    def deleteLastRoll(self):
        '''
        todo write me
        '''
        self.refTracker.deleteLastRoll()
        self.ui.tableRolls.removeRow(self.ui.tableRolls.rowCount()-1)
        self.updateFields()

    def lockInDice(self, row, col):
        '''
        todo write me
        '''
        self.ui.tableDiceStats.cellChanged.disconnect(self.lockInDice)
        self.ui.tableDiceStats.item(row, col).setFlags(Qt.ItemIsEnabled)
        self.ui.tableDiceStats.item(row, col).setBackground(QColor('lightblue'))
        self.ui.tableDiceStats.cellChanged.connect(self.lockInDice)

        self.refTracker.lockInDice(col//4-1, row+2)
        