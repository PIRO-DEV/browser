from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt.QtWebKitWidgets import *


import sys

class MainWindow(QMainWindow):

	def __init__(self,*args,**kwargs):
		super(MainWindow,self).__init__(*args,**kwargs)

		self.show()

		self.setWindowTitle("Google Browser")
		self.serWindowIcon( QIcon( os.path.join('icons','nameoftheimage.type')))

		self.browser = QWebView()
		self.browser.setUrl( QUrl("http://www.google.com/ncr"))

		self.setCentralWidget(self.browser)


app = QApplication(sys.argv)
app.setApplicationName("browser")
app.setOrganizationName("pirosoft")
app.setOrganizationDomain("class.netlify.com")
window = MainWindow()
window.show()


app.exec_()