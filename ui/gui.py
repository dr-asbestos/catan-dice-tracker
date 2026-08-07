from PySide6.QtWidgets import (QMainWindow, QHeaderView, QTableWidgetItem, \
                               QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator, QColor

from random import choices

from .mainwindow import Ui_MainWindow as mainGUIform


class GUIMain(QMainWindow):
    '''
    Frontend-backend stitching and advanced GUI setup (ie everything that Qt 
    Designer cannot do). 
    '''
    def __init__(self, cache):
        '''
        Main constructor. Initializes GUI from generated mainwindow.py module, 
        module instance references, table construction, event stitching, etc.
        '''
        super(GUIMain, self).__init__()
        self.ui = mainGUIform()
        self.ui.setupUi(self)
        self.defaultFlags = QTableWidgetItem().flags() # fix for Qt being weird w flags

        self.refTracker = cache.tracker
        self.colours = cache.config['Colours']
        self.colourRanges = cache.config['ColourRange']

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

            if i == 5: # for 7 roll (robber, cant build on 7)
                for j in range(4, 20):
                    self.ui.tableDiceStats.item(i, j).setFlags(Qt.ItemIsEnabled)
                    if j not in (4, 8, 12, 16):
                        self.ui.tableDiceStats.item(i, j).setText('N/A')
                

        # =====================================================================
        # Rolls table construction
        # =====================================================================

        # column names and widths
        self.tableRollsHeader = {
            'Roll': 35,
            'P1': 25,
            'P2': 25,
            'P3': 25,
            'P4': 25
        }
        # column settings
        self.ui.tableRolls.setColumnCount(len(self.tableRollsHeader))
        self.ui.tableRolls.setHorizontalHeaderLabels(self.tableRollsHeader.keys())
        self.ui.tableRolls.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableRolls.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        for i, w in enumerate(self.tableRollsHeader.values()):
            self.ui.tableRolls.setColumnWidth(i, w)
        # rows get generated on roll event in updateFields

        # =====================================================================
        # Totals table construction
        # =====================================================================

        # column names and widths
        self.tableTotalStatsHeader = {
            'Player 1': 80,
            'Player 2': 80,
            'Player 3': 80,
            'Player 4': 80,
        }
        # colunm settings
        self.ui.tableTotalStats.setColumnCount(len(self.tableTotalStatsHeader))
        self.ui.tableTotalStats.setHorizontalHeaderLabels(self.tableTotalStatsHeader.keys())
        self.ui.tableTotalStats.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableTotalStats.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        for i, w in enumerate(self.tableTotalStatsHeader.values()):
            self.ui.tableTotalStats.setColumnWidth(i, w)

        # row settings
        self.tableTotalStatsRows = ('Yield', 'Diffs', 'Luck')
        self.ui.tableTotalStats.setRowCount(len(self.tableTotalStatsRows))
        self.ui.tableTotalStats.setVerticalHeaderLabels(self.tableTotalStatsRows)

        for i in range(len(self.tableTotalStatsRows)):
            for j in range(len(self.tableTotalStatsHeader)):
                self.ui.tableTotalStats.setItem(i, j, QTableWidgetItem())
                self.ui.tableTotalStats.item(i, j).setTextAlignment(Qt.AlignCenter)
        
        # =====================================================================
        # Events Stitching and Other Adjustments
        # =====================================================================
        
        self.ui.tableDiceStats.cellChanged.connect(self.lockInDice)
        self.ui.buttonDeleteLastRoll.clicked.connect(self.deleteLastRoll)
        self.ui.buttonNewRoll.clicked.connect(self.newRoll)
        self.ui.buttonAutoRoll.clicked.connect(lambda: self.newRoll(auto=True))
        self.ui.buttonReset.clicked.connect(self.reset)
        self.ui.lineNewRoll.editingFinished.connect(self.newRoll)
        self.ui.lineNewRoll.setValidator(QIntValidator(2, 12))

        self.updateFields()


    def closeEvent(self, event):
        '''
        Class method override. Promps the user before closing the application 
        and all child windows.
        '''
        result = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', \
                                      QMessageBox.Yes, QMessageBox.Cancel)
        if result == QMessageBox.Yes:
            event.accept() 
        else:
            event.ignore()


    def updateFields(self, roll=None):
        '''
        UI update handler. Populates and colours all the table cells. 
        '''
        self.ui.lineNewRoll.clear()

        # populating and colouring dice stats table
        self.ui.tableDiceStats.cellChanged.disconnect(self.lockInDice)
        for i in range(11):
            self.ui.tableDiceStats.item(i, 1).setText(f'{self.refTracker.sampleRolls[i+2]}')
            self.ui.tableDiceStats.item(i, 2).setText(f'{self.refTracker.rollDiffs[i+2]:+.2f}')
            self.ui.tableDiceStats.item(i, 2).setBackground(self.interpolateColour(self.refTracker.rollDiffs[i+2], *self.colourRanges['diffs']))
            self.ui.tableDiceStats.item(i, 3).setText(f'{self.refTracker.luckDiffs[i+2]:+.2%}')
            self.ui.tableDiceStats.item(i, 3).setBackground(self.interpolateColour(self.refTracker.luckDiffs[i+2], *self.colourRanges['luck']))

            if i == 5: # skip per player stats for 7 roll
                continue

            for p in (0,1,2,3):
                self.ui.tableDiceStats.item(i, 4*p+5).setText(f'{self.refTracker.playerYields[p][i+2]}')
                self.ui.tableDiceStats.item(i, 4*p+6).setText(f'{self.refTracker.playerYieldDiffs[p][i+2]:+.2f}')
                self.ui.tableDiceStats.item(i, 4*p+6).setBackground(self.interpolateColour(self.refTracker.playerYieldDiffs[p][i+2], *self.colourRanges['diffs']))
                self.ui.tableDiceStats.item(i, 4*p+7).setText(f'{self.refTracker.playerYieldLuck[p][i+2]:+.2%}')
                self.ui.tableDiceStats.item(i, 4*p+7).setBackground(self.interpolateColour(self.refTracker.playerYieldLuck[p][i+2], *self.colourRanges['luck']))

        self.ui.tableDiceStats.clearSelection()
        self.ui.tableDiceStats.cellChanged.connect(self.lockInDice)

        # populating and colouring totals table
        self.ui.tableTotalStats.clearSelection()
        for p in (0,1,2,3):
            self.ui.tableTotalStats.item(0, p).setText(f'{sum(self.refTracker.playerYields[p].values())}')
            tempDiffs = sum(self.refTracker.playerYieldDiffs[p].values())
            self.ui.tableTotalStats.item(1, p).setText(f'{tempDiffs:+.2f}')
            self.ui.tableTotalStats.item(1, p).setBackground(self.interpolateColour(tempDiffs, *self.colourRanges['diffs']))
            tempLuck = sum(self.refTracker.playerYieldLuck[p].values())
            self.ui.tableTotalStats.item(2, p).setText(f'{tempLuck:+.2%}')
            self.ui.tableTotalStats.item(2, p).setBackground(self.interpolateColour(tempLuck, *self.colourRanges['luck']))

        # populating and colouring roll+yield history table
        if roll is not None:
            self.ui.tableRolls.clearSelection()
            i = self.ui.tableRolls.rowCount()
            self.ui.tableRolls.insertRow(i)
            self.ui.tableRolls.scrollToBottom()
            for j in range(len(self.tableRollsHeader)):
                self.ui.tableRolls.setItem(i, j, QTableWidgetItem())
                self.ui.tableRolls.item(i, j).setTextAlignment(Qt.AlignCenter)
                if j == 0:
                    self.ui.tableRolls.item(i, j).setText(str(roll[0]))
                else:
                    #                                   unicode tick                  unicode cross
                    self.ui.tableRolls.item(i, j).setText('\u2714' if roll[1][j-1] else '\u2717')
                    self.ui.tableRolls.item(i, j).setBackground(QColor(*self.colours['yieldYes']) if roll[1][j-1] else QColor(*self.colours['yieldNo']))


    def interpolateColour(self, val, minLim, maxLim):
        '''
        Returns a colour matched to the given value's position on the given  
        range. 
        '''
        ratio = max(0.0, min(1.0, (val - minLim) / (maxLim - minLim)))
        colourMin = QColor(*self.colours['rangeMin']) #lightcoral, tomato
        colourMax = QColor(*self.colours['rangeMax']) #lightgreen, limegreen

        return QColor(int(colourMin.red() + ratio * (colourMax.red() - colourMin.red())), 
                      int(colourMin.green() + ratio * (colourMax.green() - colourMin.green())), 
                      int(colourMin.blue() + ratio * (colourMax.blue() - colourMin.blue())))


    def newRoll(self, auto=False):
        '''
        Parses user roll entry and calculates statistics.
        '''
        try: # valid roll?
            dice = None
            if auto:
                dice = choices(list(self.refTracker.diceCombs.keys()), self.refTracker.diceCombs.values(), k=1)[0]
            else:
                dice = int(self.ui.lineNewRoll.text())
            if not (2 <= dice <= 12):
                raise
        except:
            print(f'Invalid dice: {dice}')
        else:
            # fetch and package dice roll and yields
            roll = (dice, 
                    (self.ui.tableDiceStats.item(dice-2, 4).checkState() == Qt.Checked,
                     self.ui.tableDiceStats.item(dice-2, 8).checkState() == Qt.Checked,
                     self.ui.tableDiceStats.item(dice-2, 12).checkState() == Qt.Checked,
                     self.ui.tableDiceStats.item(dice-2, 16).checkState() == Qt.Checked))
            # calculate and update
            self.refTracker.newRoll(roll)
            self.updateFields(roll)
        

    def deleteLastRoll(self):
        '''
        Undoes last roll. Removes any dice locks made on the previous turn. 
        '''
        self.ui.tableDiceStats.cellChanged.disconnect(self.lockInDice)
        for p, k in self.refTracker.diceLocks.items():
            for die, turn in k.items():
                # check if die was locked in last turn
                if turn != -1 and turn + 1 == len(self.refTracker.rolls):
                    # reset cell and die lock
                    self.ui.tableDiceStats.item(die-2, 4*p+4).setFlags(self.defaultFlags)
                    self.ui.tableDiceStats.item(die-2, 4*p+4).setCheckState(Qt.Unchecked)
                    self.ui.tableDiceStats.item(die-2, 4*p+4).setData(Qt.BackgroundRole, None)
                    self.ui.tableDiceStats.item(die-2, 4*p+5).setData(Qt.BackgroundRole, None)
                    self.refTracker.diceLocks[p][die] = -1
        self.ui.tableDiceStats.cellChanged.connect(self.lockInDice)

        self.refTracker.deleteLastRoll()
        self.ui.tableRolls.removeRow(self.ui.tableRolls.rowCount()-1)
        self.updateFields()


    def lockInDice(self, row, col):
        '''
        Locks in a dice roll as a yielding roll for a player, aka "building a 
        settlement" (what this should've been called). Triggered from "cell 
        changed in a table" event, in this case checkmarks. 
        '''
        # update triggered cell
        self.ui.tableDiceStats.cellChanged.disconnect(self.lockInDice)
        self.ui.tableDiceStats.item(row, col).setFlags(Qt.ItemIsEnabled)
        self.ui.tableDiceStats.item(row, col).setBackground(QColor(*self.colours['settlement']))
        self.ui.tableDiceStats.item(row, col+1).setBackground(QColor(*self.colours['settlement']))
        self.ui.tableDiceStats.cellChanged.connect(self.lockInDice)
        # have tracker remember player and dice
        self.refTracker.lockInDice(col//4-1, row+2)


    def reset(self):
        '''
        Prompts the user if they indeed want to reset everything, on positive 
        response resets everything.
        '''
        result = QMessageBox.question(self, 'Reset', 'This action will clear the roll and building history, '\
                                      'as well as all the statistics. Are you sure you want to continue?', \
                                        QMessageBox.Yes, QMessageBox.Cancel)
        if result == QMessageBox.Yes:
            self.ui.tableDiceStats.cellChanged.disconnect(self.lockInDice)
            for i in range(11):
                for p in (0,1,2,3):
                    self.ui.tableDiceStats.item(i, 4*p+4).setFlags(self.defaultFlags)
                    self.ui.tableDiceStats.item(i, 4*p+4).setCheckState(Qt.Unchecked)
                    self.ui.tableDiceStats.item(i, 4*p+4).setData(Qt.BackgroundRole, None)
                    self.ui.tableDiceStats.item(i, 4*p+5).setData(Qt.BackgroundRole, None)
            self.ui.tableDiceStats.cellChanged.connect(self.lockInDice)
                
            self.ui.tableRolls.setRowCount(0)
            self.refTracker.reset()
            self.updateFields()


        