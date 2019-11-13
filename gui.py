import osumap_download_script
import osumap_compilation_script
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Beatmap Sharing'
        self.left = 1000
        self.top = 500
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Open Download Script', self)
        button.move(25,70)
        button.clicked.connect(self.on_click)


        button1 = QPushButton('Open Compilation Script', self)
        button1.move(150,70)
        button1.clicked.connect(self.on_click1)
        
        self.show()

        

    @pyqtSlot()
    def on_click(self):
        osumap_download_script.download()
    @pyqtSlot()
    def on_click1(self):
        osumap_compilation_script.compile()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
