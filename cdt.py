#! venv/bin/python
import sys
from PySide6.QtWidgets import QApplication

from utils.shared import SharedContent
from utils.tracker import Tracker
from ui.gui import GUIMain


def main():
    '''
    Main entry point.
    '''
    cache = SharedContent()
    cache.load_config('config.toml')

    cache.tracker = Tracker()

    app = QApplication(sys.argv)
    window = GUIMain(cache)
    window.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()
