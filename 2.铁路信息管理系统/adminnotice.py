from PyQt5.QtSql import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer, pyqtSignal
from noticeui import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
class adminnoticefun(QDialog, Ui_Dialog):
    def __init__(self, username):
        super().__init__()
        #self.name = username
        self.setupUi(self)
        #self.db = QSqlDatabase.addDatabase('QSQLITE')
        #self.connect_db()
        self.pushButton.clicked.connect(self.On_Login)

    def connect_db(self):  # 2
        self.db.setDatabaseName('./user.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def On_Login(self):
        query = QSqlQuery()
        if self.lineEdit.text():
            insert_query = "INSERT INTO usernotice (text) VALUES (?)"
            query.prepare(insert_query)
            query.addBindValue(self.lineEdit.text())
            if query.exec_():
                QMessageBox.information(self, 'Connection', '成功')
            else:
                QMessageBox.critical(self, 'Connection', '插入数据失败')



