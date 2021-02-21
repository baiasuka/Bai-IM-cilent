from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QFormLayout, \
    QLineEdit
from PyQt5.QtGui import QIcon, QFont

from request import http_request_sender


class PageRegist(QWidget):
    """
    注册窗口
    """
    def __init__(self):
        super().__init__()
        QToolTip.setFont(QFont('SansSerif', 10))

        # 登录项表单
        form_regist = QFormLayout()
        self.input_account = QLineEdit()
        self.input_account.setFixedWidth(240)
        self.input_password = QLineEdit()
        self.input_password.setFixedWidth(240)
        self.input_password_again = QLineEdit()
        self.input_password_again.setFixedWidth(240)

        form_regist.addRow("用户名", self.input_account)
        form_regist.addRow("密码", self.input_password)
        form_regist.addRow("再次输入密码", self.input_password_again)

        self.input_account.setEchoMode(QLineEdit.Normal)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password_again.setEchoMode(QLineEdit.Password)

        # 按钮
        btn_login = QPushButton('提交', self)
        btn_login.setToolTip('点击提交')
        btn_login.clicked.connect(self.submit_regist)
        btn_login.resize(btn_login.sizeHint())
        btn_login.move(180, 280)

        btn_quit = QPushButton('退出', self)
        btn_quit.setToolTip('点击退出')
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(320, 280)

        # 设置logo
        self.setGeometry(400, 400, 480, 320)
        self.setWindowTitle('注册')

        self.setLayout(form_regist)

    def open(self):
        self.show()

    def submit_regist(self):
        """
        提交注册请求
        :return:
        """
        ua = self.input_account.text()
        up = self.input_password.text()
        upa = self.input_password_again.text()

        if ua == '':
            info = QMessageBox(QMessageBox.Warning, '提示', '请输入用户名！')
            info.exec_()
            return True
        if up == '':
            info = QMessageBox(QMessageBox.Warning, '提示', '请输入密码！')
            info.exec_()
            return True
        if upa == '':
            info = QMessageBox(QMessageBox.Warning, '提示', '请再次输入密码！')
            info.exec_()
            return True
        r = http_request_sender.signup(ua, up)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    regist_page = PageRegist()
    regist_page.open()

    sys.exit(app.exec_())