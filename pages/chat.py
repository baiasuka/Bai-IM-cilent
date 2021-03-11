from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QFormLayout, \
    QTextEdit, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from bs4 import BeautifulSoup

from message import HisMsgContainer
from pages.handler.text_handler import replace_remote_pic_to_local

his_text = HisMsgContainer()


class PageChat(QWidget):
    """
    私聊窗口
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

    def open(self):
        self.show()

    def send_msg(self):
        content = self.input_content.toHtml()
        soup = BeautifulSoup(content, 'html.parser')
        soup = replace_remote_pic_to_local(soup)
        self.input_content.clear()
        his_text.addText(content)
        self.his_content.insertHtml(soup.prettify())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    regist_page = PageChat()
    regist_page.open()

    sys.exit(app.exec_())
