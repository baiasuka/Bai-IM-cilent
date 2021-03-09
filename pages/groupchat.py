from threading import Thread
import socket
import json
import time
import random

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QFormLayout, \
    QTextEdit, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QTextCursor

from message.core import MsgHandler


msg_handler = MsgHandler()


class PageGroupChat(QWidget):
    """
    群聊窗口
    """
    def __init__(self):
        super().__init__()
        QToolTip.setFont(QFont('SansSerif', 10))

        self.his_content = QTextEdit()
        self.his_content.setReadOnly(True)
        self.his_content.resize(600, 240)
        self.input_content = QTextEdit()
        self.his_content.resize(600, 120)

        # 按钮
        btn_send = QPushButton('发送', self)
        btn_send.setToolTip('点击发送')
        btn_send.clicked.connect(self.send_msg)
        btn_send.resize(btn_send.sizeHint())
        btn_send.move(240, 400)

        btn_quit = QPushButton('退出', self)
        btn_quit.setToolTip('点击退出')
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(360, 400)

        self.setGeometry(300, 300, 640, 480)
        layout = QVBoxLayout()
        layout.addWidget(self.his_content)
        layout.addWidget(self.input_content)
        layout.addWidget(btn_send)
        layout.addWidget(btn_quit)
        self.setWindowTitle('Bai-IM')
        self.setWindowIcon(QIcon('./static/icon/logo.png'))
        self.setLayout(layout)

        nick_list = ["红牛", "皮皮犬", "驴", "谭"]
        self.nick = random.choice(nick_list)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认退出', '确认退出Bai-IM？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            msg_handler.send({"content": self.nick + "离开房间\n"})
            msg_handler.close()
            event.accept()
        else:
            event.ignore()

    def open(self):
        msg_handler.send({"content": self.nick + "进入房间\n"})
        self.show()
        rev_thread = Thread(target=msg_handler.listening, args=(self,))
        rev_thread.start()

    def send_msg(self):
        content = self.input_content.toPlainText()
        self.input_content.clear()
        msg_handler.send({"content": self.nick + ":" + content + "\n"})


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    regist_page = PageGroupChat()
    regist_page.open()

    sys.exit(app.exec_())
