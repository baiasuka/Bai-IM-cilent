from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QFormLayout, \
    QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

from request import http_request_sender
from pages.regist import PageRegist


class PageLogin(QWidget):
    """
    首页登录页
    """
    def __init__(self):
        super().__init__()
        QToolTip.setFont(QFont('SansSerif', 10))

        # 登录项表单
        form_login = QFormLayout()
        self.input_account = QLineEdit()
        self.input_account.setFixedWidth(320)
        self.input_password = QLineEdit()
        self.input_password.setFixedWidth(320)

        form_login.addRow("用户名", self.input_account)
        form_login.addRow("密码", self.input_password)

        self.input_account.setEchoMode(QLineEdit.Normal)
        self.input_password.setEchoMode(QLineEdit.Password)

        # 按钮
        btn_login = QPushButton('登录', self)
        btn_login.setToolTip('点击登录')
        btn_login.clicked.connect(self.click_login)
        btn_login.resize(btn_login.sizeHint())
        btn_login.move(120, 400)

        btn_regist = QPushButton('注册', self)
        btn_regist.setToolTip('点击注册')
        btn_regist.clicked.connect(self.click_regist)
        btn_regist.resize(btn_regist.sizeHint())
        btn_regist.move(240, 400)

        btn_quit = QPushButton('退出', self)
        btn_quit.setToolTip('点击退出')
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(360, 400)

        # 设置logo
        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('Bai-IM')
        self.setWindowIcon(QIcon('./static/icon/logo.png'))

        self.setLayout(form_login)
        self.show()

    def quitEvent(self, event):
        reply = QMessageBox.question(self, '确认退出', '确认退出Bai-IM？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def click_login(self):
        """
        点击登录按钮登录
        :return:
        """
        ua = self.input_account.text()
        up = self.input_password.text()
        if ua == '':
            info = QMessageBox(QMessageBox.Warning, '提示', '请输入用户名！')
            info.exec_()
            return True
        if up == '':
            info = QMessageBox(QMessageBox.Warning, '提示', '请输入密码！')
            info.exec_()
            return True
        r = http_request_sender.login(ua, up)
        if r["code"] == 200:
            http_request_sender.set_headers_key("auth-token", r["data"]["token"])
            # info = QMessageBox(QMessageBox.Warning, '提示', '登陆成功！')
            self.close()
        else:
            info = QMessageBox(QMessageBox.Warning, '错误', r["msg"])
            info.exec_()
            return True

    def click_regist(self):
        """
        点击打开注册窗口
        :return:
        """
        self.regist_page = PageRegist()
        self.regist_page.open()
