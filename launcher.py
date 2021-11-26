import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont

from pages.login import PageLogin



def main():
    app = QApplication(sys.argv)

    login_page = PageLogin()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
