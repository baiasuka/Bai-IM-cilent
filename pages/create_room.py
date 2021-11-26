from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QFormLayout, \
    QLineEdit
from PyQt5.QtGui import QIcon, QFont

from request import http_request_sender


class PageCreateRoom(QWidget):
    """
    创建房间弹窗
    """
    def __init__(self):
        super().__init__()
        QToolTip.setFont(QFont('SansSerif', 10))

        # 登录项表单
        form_regist = QFormLayout()
        self.input_room_name = QLineEdit()
        self.input_room_name.setFixedWidth(240)
        self.input_password = QLineEdit()
        self.input_password.setFixedWidth(240)

        form_regist.addRow("房间名", self.input_room_name)
        form_regist.addRow("密码", self.input_password)

        self.input_room_name.setEchoMode(QLineEdit.Normal)
        self.input_password.setEchoMode(QLineEdit.Password)

        # 按钮
        btn_login = QPushButton('提交', self)
        btn_login.setToolTip('点击提交')
        btn_login.clicked.connect(self.submit_create_room)
        btn_login.resize(btn_login.sizeHint())
        btn_login.move(180, 280)

        btn_quit = QPushButton('退出', self)
        btn_quit.setToolTip('点击退出')
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(320, 280)

        # 设置logo
        self.setGeometry(400, 400, 480, 320)
        self.setWindowTitle('创建房间')

        self.setLayout(form_regist)

    def open(self):
        """
        显示页面
        :return:
        """
        self.show()

    def submit_create_room(self):
        """
        提交创建房间表单
        :return:
        """
        rn = self.input_room_name.text()
        rp = self.input_password.text()

        if rn == '':
            info = QMessageBox(QMessageBox.Warning, '提示', '请输入用户名！')
            info.exec_()
            return True
        if rp == '':
            info = QMessageBox(QMessageBox.Warning, '提示', '请输入密码！')
            info.exec_()
            return True
        r = http_request_sender.signup(rn, rp)
        if r["code"] == 200:
            info = QMessageBox(QMessageBox.Information, '提示', '创建账号成功')
            self.close()
        else:
            info = QMessageBox(QMessageBox.Warning, '提示', r["msg"])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    regist_page = PageCreateRoom()
    regist_page.open()

    sys.exit(app.exec_())