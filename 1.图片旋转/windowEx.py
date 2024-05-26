from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer
from show import Ui_Form

class WindowEx(QWidget, Ui_Form):
	def init(self):
		super(WindowEx, self).init()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.On_file)
		self.pushButton_2.clicked.connect(self.check)
		self.pushButton_3.clicked.connect(self.Stop)
		self.timer = QTimer()
		self.timer.timeout.connect(self.updateRotation)
		self.rotationAngle = 0
    
	def check(self):
		self.timer.start(30)

	def On_file(self):
		options = QFileDialog.Options()
		options |= QFileDialog.ReadOnly
	
		self.fileName, _ = QFileDialog.getOpenFileName(self, '打开文件', '', 'All Files (*);;Text Files (*.txt)', options=options)
		if self.fileName:
			pixmap = QPixmap(self.fileName)
			self.label_4.setPixmap(pixmap)
			self.comboBox.clear()
			self.comboBox_2.clear()
			self.comboBox_2.addItem('1')
			self.comboBox_2.addItem('2')
			self.comboBox_2.addItem('3')
			self.comboBox_2.addItem('4')
			self.comboBox.addItem('顺时针')
			self.comboBox.addItem('逆时针')

	def updateRotation(self):
		dir = self.comboBox.currentIndex()
		index = self.comboBox_2.currentIndex()
		if dir == 0:
			if index == 0:
				self.rotationAngle += 1
			elif index == 1:
				self.rotationAngle += 2
			elif index == 2:
				self.rotationAngle += 3
			elif index == 3:
				self.rotationAngle += 4
		elif dir == 1:
			if index == 0:
				self.rotationAngle -= 1
			elif index == 1:
				self.rotationAngle -= 2
			elif index == 2:
				self.rotationAngle -= 3
			elif index == 3:
				self.rotationAngle -= 4

		self.label_4.setText(self.fileName)
		pixmap = QPixmap(self.fileName)
		rotated_pixmap = pixmap.transformed(QTransform().rotate(self.rotationAngle))
		self.label_4.setPixmap(rotated_pixmap)
	def Stop(self):
		self.timer.stop()