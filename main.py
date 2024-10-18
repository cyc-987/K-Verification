# sys tools
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from serial.tools import list_ports
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

# ui class
from ui.mainwindow import Ui_MainWindow

# self defined class
from serialThread import SerialThread
from controller import Controller

class MyMainWindow(QMainWindow, Ui_MainWindow):
    # signals
    connect_port = pyqtSignal(str)
    
    record = pyqtSignal(int)#0: end; 1: start
    
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # info
        self.version_info = ("demo version, insider preview \n " + 
                             "restricted to internal use only \n " +
                             "cyc, 2024-10-12, 0.0.1")
        
        # init behavior
        self.getAvailablePorts()
        self.waiting_for_retrying = False
        
        # signal connections
        self.connectButton.clicked.connect(self.connectPort)
    
    def getAvailablePorts(self): 
        ports = list_ports.comports()
        available_ports = [port.device for port in ports]
        self.comboBox_port.clear()

        if available_ports:
            self.comboBox_port.addItems(available_ports)
        else:
            self.comboBox_port.addItem("no available ports")

    def connectPort(self):
        port = self.comboBox_port.currentText()
        self.connect_port.emit(port)
        print("selected port: ", port)
        
    def verifyPasscode(self):
        password_input = [self.password1.text(), self.password2.text(), self.password3.text(), self.password4.text()]
        # judge empty
        if not all(password_input):
            self.label_error_content.setText("Empty input")
            return
        return
    
    def startRecord(self):
        self.record.emit(1)
    
    def endRecord(self):
        self.record.emit(0)
         
    def printContent(self):
        print(self.password1.text() if self.password1.text() else "empty")
        print(self.password2.text() if self.password2.text() else "empty")
        print(self.password3.text() if self.password3.text() else "empty")
        print(self.password4.text() if self.password4.text() else "empty")
        
    def showAbout(self):
        QMessageBox.about(self, "About", self.version_info)
    
    def jumpToRepo(self):
        QDesktopServices.openUrl(QUrl("https://github.com/cyc-987/K-Verification"))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    mainWindow = MyMainWindow()
    serialF = SerialThread()
    ctrl = Controller(mainWindow, serialF)
    
    mainWindow.show()
    sys.exit(app.exec_())