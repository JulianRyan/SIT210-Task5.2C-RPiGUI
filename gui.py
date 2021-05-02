from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(167, 176)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.rdRed = QtWidgets.QRadioButton(self.centralwidget)
		self.rdRed.setGeometry(QtCore.QRect(50, 40, 80, 20))
		self.rdRed.setObjectName("rdRed")
		self.rdRed.toggled.connect(self.redClicked)

		self.rdBlue = QtWidgets.QRadioButton(self.centralwidget)
		self.rdBlue.setGeometry(QtCore.QRect(50, 65, 80, 20))
		self.rdBlue.setObjectName("rdBlue")
		self.rdBlue.toggled.connect(self.blueClicked)

		self.rdGreen = QtWidgets.QRadioButton(self.centralwidget)
		self.rdGreen.setGeometry(QtCore.QRect(50, 90, 80, 20))
		self.rdGreen.setObjectName("rdGreen")
		self.rdGreen.toggled.connect(self.greenClicked)

		self.btnExit = QtWidgets.QPushButton(self.centralwidget)
		self.btnExit.setGeometry(QtCore.QRect(100, 120, 80, 30))
		self.btnExit.setObjectName("btnExit")
		self.btnExit.clicked.connect(self.btnClicked)

		MainWindow.setCentralWidget(self.centralwidget)
		self.retranslateUI(MainWindow)

	def retranslateUI(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

		self.rdRed.setText(_translate("MainWindow", "Red"))
		self.rdBlue.setText(_translate("MainWindow", "Blue"))
		self.rdGreen.setText(_translate("MainWindow", "Green"))
		self.btnExit.setText(_translate("MainWindow", "Exit"))

	def btnClicked(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(19, GPIO.OUT)
		GPIO.setup(21, GPIO.OUT)
		GPIO.setup(23, GPIO.OUT)
		GPIO.output(19, GPIO.LOW)
		GPIO.output(21, GPIO.LOW)
		GPIO.output(23, GPIO.LOW)
		GPIO.cleanup()
		sys.exit(app.exec_())
        
	def redClicked(self):
		if self.rdRed.isChecked():
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(19, GPIO.OUT)
			GPIO.setup(21, GPIO.OUT)
			GPIO.setup(23, GPIO.OUT)
			GPIO.output(19, GPIO.HIGH)
			GPIO.output(21, GPIO.LOW)
			GPIO.output(23, GPIO.LOW)
	def blueClicked(self):
		if self.rdBlue.isChecked():
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(19, GPIO.OUT)
			GPIO.setup(21, GPIO.OUT)
			GPIO.setup(23, GPIO.OUT)
			GPIO.output(21, GPIO.HIGH)
			GPIO.output(19, GPIO.LOW)
			GPIO.output(23, GPIO.LOW)
	def greenClicked(self):
		if self.rdGreen.isChecked():
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(19, GPIO.OUT)
			GPIO.setup(21, GPIO.OUT)
			GPIO.setup(23, GPIO.OUT)
			GPIO.output(23, GPIO.HIGH)
			GPIO.output(19, GPIO.LOW)
			GPIO.output(21, GPIO.LOW)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(19, GPIO.OUT)
	GPIO.setup(21, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.output(19, GPIO.LOW)
	GPIO.output(21, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.cleanup()
	sys.exit(app.exec_())