from PyQt5.QtSql import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer, pyqtSignal
from adminRegedit import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
class adminregeditfun(QDialog, Ui_Dialog):
    def __init__(self, username):
        super().__init__()
        #self.name = username
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
            query.prepare(
                "UPDATE userinfo SET 出生日期=?, 籍贯=?, 学历=?, 性别=?, 实习开始时间=?, 实习结束时间=?, 所属区段=? WHERE 姓名=?")
            query.addBindValue(self.lineEdit.text())
            query.addBindValue(self.lineEdit_2.text())
            query.addBindValue(self.lineEdit_3.text())
            query.addBindValue(self.lineEdit_4.text())
            query.addBindValue(self.lineEdit_5.text())
            query.addBindValue(self.lineEdit_6.text())
            query.addBindValue(self.comboBox.currentText())
            query.addBindValue(self.lineEdit_7.text())

            if not query.exec():
                print('Failed to update user info:', query.lastError().text())
            else:
                QMessageBox.information(self, '提示', '修改成功')
                self.accept()
        else:
            QMessageBox.critical(self, '提示', '请将信息填写完整')

