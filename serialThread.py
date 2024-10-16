from PyQt5.QtCore import QThread, pyqtSignal

import time
import sys
import serial

from RSA import encrypt, decrypt

class SerialThread(QThread):
    # signals
    connect_status = pyqtSignal(int) # 0: success, 1: start connecting, 2: start verification, 3: holding, 4: failed    

    def __init__(self, port=None, baudrate=9600):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None
        self.is_running = True
        self.is_connected = False
        
        self.privateKey_local = [14351, 1283]
        self.publicKey_local = [14351, 11]
        self.publicKey_arduino = [14351, 11] 

    def run(self):
        # 第一个循环：尝试建立连接，最多尝试三次
        self.connect_status.emit(1)
        for _ in range(3):
            try: 
                self.serial_connection = serial.Serial(self.port, baudrate=self.baudrate, timeout=1)
                print("串口连接已建立")
                self.is_connected = True
                break
            except: time.sleep(1)
        else:
            print("连接失败")
            self.connect_status.emit(4)
            return
        

        # 第二个循环：验证客户端公钥，最多尝试三次
        self.connect_status.emit(2)
        for _ in range(3):
            if self.verifyDevice():
                self.is_verified = True
                break
            time.sleep(1)
        else:
            print("公钥验证失败")
            self.serial_connection.close()
            self.is_connected = False
            self.connect_status.emit(4)
            return
        
        # 大循环：保持连接
        while True:
            self.connect_status.emit(3)
            # 测试连接状态
            time1 = time.time()
            if time.time() - time1 > 10:
                if not self.verifyDevice():
                    print("设备验证失败")
                    self.serial_connection.close()
                    self.connect_status.emit(4)
                else:
                    time1 = time.time()
            
            time.sleep(0.1)
    
    def verifyDevice(self):
        # send data
        current_time = time.time()
        message = ("ryou"+str(int(current_time)%114514)+"\n")
        message_encrypt = encrypt(message, self.publicKey_arduino)
        if self.send_data(message):
            pass
        else: return False
        
        # receive data
        received_message_encrypt = self.receive_data()
        if received_message_encrypt == False:
            return False
        received_message = decrypt(received_message_encrypt, self.privateKey_local)
        
        # judge
        if received_message == message:
            return True
        else:
            return False

    
    def send_data(self, data, max_wating_time_second=1):
        
        # 超时
        start_time = time.time()
        while self.serial_connection.readline() != -1:
            if time.time() - start_time < max_wating_time_second:
                pass
            else:
                break
        if time.time() - start_time >= max_wating_time_second:
            print(f"发送超时{max_wating_time_second}秒")
            return 0
        
        try:
            if self.serial_connection is not None:
                self.serial_connection.write(data.encode('utf-8'))
            else:
                print("连接无效或未验证，无法发送数据。")
        except serial.SerialTimeoutException as e:
            print(f"发送数据超时: {e}")
        except Exception as e:
            print(f"发送数据时发生未知错误: {e}")
        return 0
    
    def receive_data(self, max_wating_time_second=3):
        # 超时
        start_time = time.time()
        while self.serial_connection.readline() == -1:
            if time.time() - start_time < max_wating_time_second:
                pass
            else:
                break
        if time.time() - start_time >= max_wating_time_second:
            print(f"接收超时{max_wating_time_second}秒")
            return 0
                
        try:
            if self.serial_connection is not None:
                data = self.serial_connection.readline()
                return data.decode('utf-8')
            else:
                print("连接无效或未验证，无法接收数据。")
        except serial.SerialTimeoutException as e:
            print(f"接收数据超时: {e}")
        except Exception as e:
            print(f"接收数据时发生未知错误: {e}")
        return 0

    def stop(self):
        # if self.is_connected:
        #     self.serial_connection.close()
        return