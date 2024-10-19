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
        self.ui.connect_abort.connect(self.abortConnection)
        
        self.ui.record.connect(self.handle_record)
        self.serial_thread.record_data.connect(self.handle_record_result)
        
    
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
            self.connected = False
        elif status == 3:
            self.ui.label_connect_status.setText("Holding...")
            self.connected = True
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
    
    def handle_record(self):
        # check board status
        if not self.connected:
            self.handle_record_error(1)
            return
        
        if self.ui.record_status:
            return
        
        self.ui.clearButton.setEnabled(False)
        self.ui.label_keyboard_status.setText("Recording...")
        self.serial_thread.record = True
        self.ui.record_status = True
        return
    
    def handle_record_result(self, result):
        try: result_data = float(result)
        except: result_data = 0
        
        if result_data > 0.75:
            self.ui.label_keyboard_status.setText("Pass - " + str(result_data*100) + "%")
            self.ui.keyboard_result = True
        else:
            self.ui.label_keyboard_status.setText("Failed - " + str(result_data*100) + "%")
            self.ui.keyboard_result = False
        self.ui.clearButton.setEnabled(True)
        return
    
    def handle_record_error(self, error):
        if error == 1:
            self.ui.label_error_content.setText("Board not connected.")
        elif error == 0:
            self.ui.label_error_content.setText("None")
        return
        

    def handle_send_data(self, data):
        # 处理发送数据
        self.serial_thread.send_data(data)

    def update_ui_with_data(self, data):
        # 将串口接收到的数据更新到UI
        self.ui.textEdit.append(f"收到: {data}")
