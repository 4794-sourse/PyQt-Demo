from login import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer, pyqtSignal
from regeditfun import regeditfun

class loginfun(QDialog, Ui_Dialog):
    loginResult = pyqtSignal(int, str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('系统登录')
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.connect_db()
        self.pushButton.clicked.connect(self.On_Login)
        self.comboBox.addItem('登录')
        self.comboBox.addItem('注册')
        self.comboBox.addItem('管理员登录')
    def connect_db(self):  # 2
        self.db.setDatabaseName('./user.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def On_Login(self):
        self.connect_db()
        query = QSqlQuery()
        if self.comboBox.currentIndex() == 0:
            query.exec("SELECT rowid, username, password class FROM usertable")
            while query.next():
                self.stu_name = query.value(1)
                self.stu_class = query.value(2)
                user = self.lineEdit.text()
                password = self.lineEdit_2.text()
                if self.stu_name == user and self.stu_class == password:
                    QMessageBox.information(self, '提醒', '登录成功')
                    self.db.close()
                    self.accept(user)
        elif self.comboBox.currentIndex() == 1:
            if self.lineEdit.text() and self.lineEdit_2.text():
                insert_query = "INSERT INTO usertable (username, password) VALUES (?, ?)"
                query.prepare(insert_query)
                query.addBindValue(self.lineEdit.text())
                query.addBindValue(self.lineEdit_2.text())
                if query.exec_():
                    regedit = regeditfun(self.lineEdit.text())
                    regedit.exec_()
                QMessageBox.information(self, '提醒', '注册成功')
            else:
                QMessageBox.critical(self, '提醒', '请填写账号或密码信息')
        elif self.comboBox.currentIndex() == 2:
            query.exec("SELECT rowid, username, password class FROM usertable")
            while query.next():
                self.stu_name = query.value(1)
                self.stu_class = query.value(2)
                user = self.lineEdit.text()
                password = self.lineEdit_2.text()
                if self.stu_name == user and self.stu_class == password:
                    QMessageBox.information(self, '提醒', '登录成功')
                    self.db.close()
                    self.reject(user)
        self.db.close()

    def accept(self, name):
        self.loginResult.emit(1, name)
        super().accept()

    def reject(self, name):
        self.loginResult.emit(2, name)
        super().reject()