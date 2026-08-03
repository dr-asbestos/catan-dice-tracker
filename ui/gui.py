from PySide6.QtWidgets import QMainWindow

from .mainwindow import Ui_MainWindow as mainGUIform


class GUIMain(QMainWindow):
    '''
    todo write me
    '''
    def __init__(self):
        '''
        todo write me
        '''
        super(GUIMain, self).__init__()
        self.ui = mainGUIform()
        self.ui.setupUi(self)
        