from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QFormLayout, \
    QLineEdit, QVBoxLayout, QHBoxLayout, QListView
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QStringListModel

from pages.create_room import PageCreateRoom


class PageHall(QWidget):
    """
    大厅页
    """
    def __init__(self):
        super().__init__()
        self._room_dict = {}
        self._room_name_list = []

        QToolTip.setFont(QFont('SansSerif', 10))
        # 创建listview对象
        self._list_room = QListView()
        self._list_room.doubleClicked.connect(self.click_room)

        btn_refresh = QPushButton('刷新', self)
        btn_refresh.setToolTip('点击刷新')
        btn_refresh.clicked.connect(self.refresh_roomlist)
        btn_refresh.resize(btn_refresh.sizeHint())
        btn_refresh.move(240, 400)

        btn_create = QPushButton('新建', self)
        btn_create.setToolTip('点击创建房间')
        btn_create.clicked.connect(self.click_create_room)
        btn_create.resize(btn_create.sizeHint())
        btn_create.move(240, 400)

        btn_quit = QPushButton('退出', self)
        btn_quit.setToolTip('点击退出')
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(360, 400)

        self.setGeometry(300, 300, 800, 600)
        layout = QVBoxLayout()
        layout.addWidget(self._list_room)
        layout.addWidget(btn_refresh)
        layout.addWidget(btn_quit)
        self.setLayout(layout)

    def open(self):
        self._room_dict = {"1号房": 1, "2号房": 2}
        self._room_name_list = list(self._room_dict.keys())
        lmode = QStringListModel()
        lmode.setStringList(self._room_dict.keys())
        self._list_room.setModel(lmode)
        self.show()

    def refresh_roomlist(self):
        """
        刷新房间列表
        :return:
        """
        self._room_dict = {"5号房": 6, "6号房": 6}
        self._room_name_list = list(self._room_dict.keys())
        lmode = QStringListModel()
        lmode.setStringList(self._room_dict.keys())
        self._list_room.setModel(lmode)

    def click_create_room(self):
        """
        点击创建房间按钮弹出弹窗
        :return:
        """
        self.create_room_page = PageCreateRoom()
        self.create_room_page.open()

    def click_room(self, qModeIndex):
        """
        双击房间后进入房间
        :param qModeIndex:
        :return:
        """
        QMessageBox.information(self, "QListView", "你选择了: " + self._room_name_list[qModeIndex.row()])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    regist_page = PageHall()
    regist_page.open()

    sys.exit(app.exec_())