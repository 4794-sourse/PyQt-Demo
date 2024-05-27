from loginfun import loginfun
from userfun import userfun
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer
import sys
import subprocess
import os



if '__main__' == __name__:
    app = QApplication([])
    login = loginfun()
    result = login.show()
    login.loginResult.connect(lambda result, name: handleLoginResult(result, name))


    def handleLoginResult(result, name):
        if result == 1:
            login.hide()
            #user = userfun(name)
            subprocess.call(['python', 'userfun.py', name], creationflags=subprocess.CREATE_NO_WINDOW)
            #user.show()
        elif result == 2:
            login.hide()
            subprocess.call(['python', 'adminfun.py', name], creationflags=subprocess.CREATE_NO_WINDOW)
    sys.exit(app.exec_())


