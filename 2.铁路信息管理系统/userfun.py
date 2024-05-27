from PyQt5.QtSql import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer, pyqtSignal
from user import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from moveinfo import moveinfo
import sys
import time
import subprocess
class userfun(QWidget, Ui_Form):
    def __init__(self, username):
        super().__init__()
        self.name = username
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.connect_db()
        #On_Notice()
        self.pushButton.clicked.connect(self.On_info)
        self.pushButton_2.clicked.connect(self.On_infoMove)
        self.pushButton_3.clicked.connect(self.On_Card)
        self.pushButton_4.clicked.connect(self.On_localAi)
        self.pushButton_5.clicked.connect(self.On_Ai)
        self.pushButton_6.clicked.connect(self.On_history)
        self.On_Notice()

    def On_Card(self):
        current_time = time.strftime("%Y-%m-%d", time.localtime())
        query = QSqlQuery()
        insert_query = "INSERT INTO userCard (time, name) VALUES (?, ?)"
        query.prepare(insert_query)
        query.addBindValue(current_time)
        query.addBindValue(self.name)
        query.exec_()
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText('签到成功')
    def On_history(self):
        query = QSqlQuery()
        self.plainTextEdit.clear()
        query.exec("SELECT rowid, text class FROM usernotice")
        while query.next():
            self.notice = query.value(1)
            self.plainTextEdit.appendPlainText(self.notice)
    def On_Notice(self):
        query = QSqlQuery()
        query.exec("SELECT rowid, text class FROM usernotice")
        while query.next():
            self.notice = query.value(1)
        self.plainTextEdit_2.clear()
        self.plainTextEdit_2.appendPlainText(self.notice)
    def On_Ai(self):
        subprocess.call(['python', 'localAi.py', name], creationflags=subprocess.CREATE_NO_WINDOW)
    def On_localAi(self):
        subprocess.call(['python', 'ai.py', name], creationflags=subprocess.CREATE_NO_WINDOW)
    def connect_db(self):  # 2
        self.db.setDatabaseName('./user.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def On_infoMove(self):
        info = moveinfo(self.name)
        info.exec_()
    def On_info(self):
        query = QSqlQuery()
        query.exec("SELECT rowid, 姓名, 出生日期, 籍贯, 学历, 性别, 实习开始时间, 实习结束时间, 所属区段 class FROM userinfo")
        while query.next():
            self.stu_name = query.value(1)
            self.stu_date = query.value(2)
            self.stu_bron = query.value(3)
            self.stu_sty = query.value(4)
            self.stu_sex = query.value(5)
            self.stu_start = query.value(6)
            self.stu_end = query.value(7)
            self.stu_space = query.value(8)
            if self.stu_name == self.name:
                self.plainTextEdit.clear()
                self.plainTextEdit.appendPlainText('姓名:' + self.stu_name)
                self.plainTextEdit.appendPlainText('出生日期:' + self.stu_date)
                self.plainTextEdit.appendPlainText('籍贯:' + self.stu_bron)
                self.plainTextEdit.appendPlainText('学历:' + self.stu_sty)
                self.plainTextEdit.appendPlainText('性别:' + self.stu_sex)
                self.plainTextEdit.appendPlainText('实习开始时间:' + self.stu_start)
                self.plainTextEdit.appendPlainText('实习结束时间:'+ self.stu_end)
                self.plainTextEdit.appendPlainText('所属区段:' + self.stu_space)



if '__main__' == __name__:
    name = sys.argv[1]
    app = QApplication([])
    login = userfun(name)
    result = login.show()
    sys.exit(app.exec_())