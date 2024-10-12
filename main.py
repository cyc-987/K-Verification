from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from ui.mainwindow import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # info
        self.version_info = ("demo version, insider preview \n " + 
                             "restricted to internal use only \n " +
                             "cyc, 2024-10-12, 0.0.1")
    
    def printContent(self):
        print(self.password1.text() if self.password1.text() else "empty")
        print(self.password2.text() if self.password2.text() else "empty")
        print(self.password3.text() if self.password3.text() else "empty")
        print(self.password4.text() if self.password4.text() else "empty")
        
    def showAbout(self):
        QMessageBox.about(self, "About", self.version_info)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())