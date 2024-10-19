from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import MyMainWindow
    from serialThread import SerialThread

class Controller:
    
    def __init__(self, ui: 'MyMainWindow', serial_thread: 'SerialThread'):
        self.ui = ui
        self.serial_thread = serial_thread
        
        # status
        self.connected = False

        # connect the signal
        self.ui.connect_port.connect(self.startThread)
        self.serial_thread.connect_status.connect(self.handle_connect_status)
        self.ui.record.connect(self.handle_record)
        self.ui.connect_abort.connect(self.abortConnection)
    
    def startThread(self, port):
        if self.connected: 
            self.serial_thread.stop()
            self.connected = False
        
        self.serial_thread.port = port
        self.serial_thread.start()
        self.ui.connectButton.setEnabled(False)
        # self.serial_thread.stop()
        # self.ui.connectButton.setEnabled(True)
    
    def abortConnection(self):
        self.serial_thread.abort = True
        self.connected = False
        self.ui.connectButton.setEnabled(True)
        self.ui.label_connect_status.setText("No connection")
    
    def handle_connect_status(self, status):
        if status == 1: 
            self.ui.label_connect_status.setText("Connecting...")
        elif status == 2:
            self.ui.label_connect_status.setText("Verifying...")
        elif status == 3:
            self.ui.label_connect_status.setText("Holding...")
        elif status == 4:
            self.ui.label_connect_status.setText("Failed")
            self.connected = False
            self.serial_thread.stop()
            self.ui.connectButton.setEnabled(True)
        elif status == 0:
            self.ui.label_connect_status.setText("No Connection")
            self.connected = False
            self.serial_thread.stop()
            self.ui.connectButton.setEnabled(True)
        else:
            self.ui.label_connect_status.setText("Unknown")
    
    def handle_record(self, status):
        return
        

    def handle_send_data(self, data):
        # 处理发送数据
        self.serial_thread.send_data(data)

    def update_ui_with_data(self, data):
        # 将串口接收到的数据更新到UI
        self.ui.textEdit.append(f"收到: {data}")
