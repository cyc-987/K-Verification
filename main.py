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
    connect_abort = pyqtSignal()
    
    record = pyqtSignal()
    
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # info
        self.version_info = ("demo version, insider preview \n " + 
                             "restricted to internal use only \n " +
                             "cyc, 2024-10-12, 0.0.1")
        
        # init behavior
        self.getAvailablePorts()
        self.verificaiton_status = True
        self.record_status = False
        
        # verification result
        self.password_result = False
        self.keyboard_result = False
        
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
    
    def abortConnection(self):
        self.connect_abort.emit()
        print("abort connection")
        
    def verifyPasscode(self):
        self.verificaiton_status = False
        self.enterButton.setEnabled(False)
        password_input = [self.password1.text(), self.password2.text(), self.password3.text(), self.password4.text()]
        # judge empty
        if not all(password_input):
            self.label_error_content.setText("Empty input.")
            return
        
        correct_passwords = ["hello", "world", "sick", "hack"]
        correct_count = sum(1 for p in password_input if p in correct_passwords)
        
        if correct_count >= 3:
            self.password_result = True
            self.label_password_status.setText("Pass")
        else:
            self.password_result = False
            self.label_password_status.setText("Failed")
        
        return
    
    def startRecord(self):
        self.record.emit()
    
    def clear(self):
        self.password_result = False
        self.keyboard_result = False
        self.label_error_content.setText("None.")
        self.label_password_status.setText("None")
        self.label_keyboard_status.setText("None")
        self.verificaiton_status = True
        self.record_status = False
        self.enterButton.setEnabled(True)
        return
         
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