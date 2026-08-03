from PySide6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator

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
            'Diffs': 50,
            'Luck': 50
        }
        # column and row settings
        self.ui.tableDiceStats.setColumnCount(len(self.tableDiceStatsHeader))
        self.ui.tableDiceStats.setHorizontalHeaderLabels(self.tableDiceStatsHeader.keys())
        self.ui.tableDiceStats.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableDiceStats.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        for i, w in enumerate(self.tableDiceStatsHeader.values()):
            self.ui.tableDiceStats.setColumnWidth(i, w)

        for i in range(12):
            self.ui.tableDiceStats.insertRow(i)
            for j in range(len(self.tableDiceStatsHeader)):
                self.ui.tableDiceStats.setItem(i, j, QTableWidgetItem())
                self.ui.tableDiceStats.item(i, j).setTextAlignment(Qt.AlignCenter)
            self.ui.tableDiceStats.item(i, 0).setText(str(i+1))

        # =====================================================================
        # Events Stitching and Other Adjustments
        # =====================================================================

        self.ui.lineNewRoll.setValidator(QIntValidator(2, 12))
