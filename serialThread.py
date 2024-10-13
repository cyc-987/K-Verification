from PyQt5.QtCore import QThread, pyqtSignal

import time
import sys
import serial

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64
import binascii

class SerialThread(QThread):
    # signals
    connect_status = pyqtSignal(int) # 0: success, 1: start connecting, 2: start verification, 3: holding, 4: failed    

    def __init__(self, port=None, baudrate=9600):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None
        self.is_running = True
        self.connection = None
        self.public_key = self.load_public_key("keys/public_key.pem")
    
    def load_public_key(self, file_path):
        with open(file_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key

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
            if self.verifyDevice(self.serial_connection):
                self.is_verified = True
                break
            time.sleep(1)
        else:
            print("公钥验证失败")
            self.serial_connection.close()
            self.is_connected = False
            self.connect_status.emit(4)
            return
    
    def verifyDevice(self, connection):
        # send data to enable verify process
        self.send_data("verify\n")
        time.sleep(0.1)
        message = str(time.time())
        self.send_data("ryou" + message + "\n")
        
        # receive data from the board
        time.sleep(0.1)
        try:
            signature_base64 = connection.read(16)
            signature = base64.b64decode(signature_base64)
        except binascii.Error as e:
            print(f"Base64 解码错误: {e}")
            return False

        # calculate hash
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(message.encode('utf-8'))
        message_hash = digest.finalize()
        
        if self.verify_signature(self.public_key, message_hash, signature):
            print("签名验证成功，设备可信")
            return True
        else:
            print("签名验证失败，设备不可信")
            return False
    def verify_signature(self, public_key, message, signature):
        try:
            public_key.verify(
                signature,
                message,
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"签名验证失败: {e}")
            return False

    
    def send_data(self, data):
        try:
            if self.serial_connection is not None:
                self.serial_connection.write(data.encode('utf-8'))
            else:
                print("连接无效或未验证，无法发送数据。")
        except serial.SerialTimeoutException as e:
            print(f"发送数据超时: {e}")
        except Exception as e:
            print(f"发送数据时发生未知错误: {e}")

    def stop(self):
        if self.serial_connection:
            self.serial_connection.close()