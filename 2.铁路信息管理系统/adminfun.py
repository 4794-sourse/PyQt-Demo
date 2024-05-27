from PyQt5.QtSql import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer, pyqtSignal
from adminui import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from moveinfo import moveinfo
import sys
import time
import subprocess
from adminregeditfun import adminregeditfun
from adminnotice import adminnoticefun
class adminfun(QWidget, Ui_Form):
    def __init__(self, username):
        super().__init__()
        self.name = username
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.connect_db()
        self.pushButton.clicked.connect(self.On_info)
        self.pushButton_2.clicked.connect(self.On_infoMove)
        self.pushButton_3.clicked.connect(self.On_Card)
        self.pushButton_4.clicked.connect(self.On_localAi)
        self.pushButton_5.clicked.connect(self.On_Ai)
        self.pushButton_6.clicked.connect(self.On_history)
        self.pushButton_7.clicked.connect(self.On_history_move)
        self.On_Notice()

    def On_Card(self):
        self.tabModel = QSqlTableModel(self, self.db)
        self.tabModel.setTable("userCard")  # 设置数据表
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)  # 数据保存方式
        if not self.tabModel.select():  # 查询数据失败
            QMessageBox.critical(self, "错误信息", "打开数据表错误，错误信息:\n" + self.tabModel.lastError().text())

        # 创建表格视图
        self.tableView.setModel(self.tabModel)

    def On_history(self):
        self.tabModel = QSqlTableModel(self, self.db)
        self.tabModel.setTable("usernotice")  # 设置数据表
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)  # 数据保存方式
        if not self.tabModel.select():  # 查询数据失败
            QMessageBox.critical(self, "错误信息", "打开数据表错误，错误信息:\n" + self.tabModel.lastError().text())

        # 创建表格视图
        self.tableView.setModel(self.tabModel)
    def On_history_move(self):
        notice = adminnoticefun(self.name)
        notice.exec_()
    def On_Notice(self):
        query = QSqlQuery()
        query.exec("SELECT rowid, text class FROM usernotice")
        while query.next():
            self.notice = query.value(1)
        self.label.clear()
        self.label.setText(self.notice)
    def On_Ai(self):
        subprocess.call(['python', 'ai.py', name], creationflags=subprocess.CREATE_NO_WINDOW)
    def On_localAi(self):
        subprocess.call(['python', 'localAi.py', name], creationflags=subprocess.CREATE_NO_WINDOW)
    def connect_db(self):  # 2
        self.db.setDatabaseName('./user.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def On_infoMove(self):
        info = adminregeditfun(self.name)
        info.exec_()
    def On_info(self):
        self.tabModel = QSqlTableModel(self, self.db)
        self.tabModel.setTable("userinfo")  # 设置数据表
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)  # 数据保存方式
        if not self.tabModel.select():  # 查询数据失败
            QMessageBox.critical(self, "错误信息", "打开数据表错误，错误信息:\n" + self.tabModel.lastError().text())

        # 创建表格视图
        self.tableView.setModel(self.tabModel)



if '__main__' == __name__:
    name = sys.argv[1]
    app = QApplication([])
    login = adminfun(name)
    result = login.show()
    sys.exit(app.exec_())