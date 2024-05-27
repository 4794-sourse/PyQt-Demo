from PyQt5.QtSql import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer, pyqtSignal
from regedit import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
class regeditfun(QDialog, Ui_Dialog):
    def __init__(self, username):
        super().__init__()
        self.name = username
        self.setupUi(self)
        #self.db = QSqlDatabase.addDatabase('QSQLITE')
        #self.connect_db()
        self.pushButton.clicked.connect(self.On_Login)
        self.comboBox.addItem("车务段")
        self.comboBox.addItem("机务段")
        self.comboBox.addItem("车务段")
        self.comboBox.addItem("电务段")
        self.comboBox.addItem("车辆段")
        self.comboBox.addItem("工务段")
        self.comboBox.addItem("客运段")
        self.comboBox.addItem("通信段")
        self.comboBox.addItem("供电段")

    def connect_db(self):  # 2
        self.db.setDatabaseName('./user.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def On_Login(self):
        query = QSqlQuery()

        if (self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text() and self.lineEdit_5.text() and self.lineEdit_6.text()):
            insert_query = "INSERT INTO userinfo (姓名, 出生日期, 籍贯, 学历, 性别, 实习开始时间, 实习结束时间, 所属区段) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            query.prepare(insert_query)
            query.addBindValue(self.name)
            query.addBindValue(self.lineEdit.text())
            query.addBindValue(self.lineEdit_2.text())
            query.addBindValue(self.lineEdit_3.text())
            query.addBindValue(self.lineEdit_4.text())
            query.addBindValue(self.lineEdit_5.text())
            query.addBindValue(self.lineEdit_6.text())
            query.addBindValue(self.comboBox.currentText())
            if query.exec_():
                self.accept()
        else:
            QMessageBox.critical(self, '提示', '请将信息填写完整')

