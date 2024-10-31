from . import RSA

def arduino_to_latin1(arduino_bytes):
    """
    将 Arduino 格式的字节序列转换为 Latin-1 编码格式。
    即每4个字节中，去掉其中的两个\x00字节。
    """
    latin1_bytes = bytearray()
    for i in range(0, len(arduino_bytes), 4):
        latin1_bytes.extend(arduino_bytes[i:i+2])  # 取前两个字节，跳过后两个\x00
    return bytes(latin1_bytes)

def latin1_to_arduino(latin1_bytes):
    """
    将 Latin-1 编码的字节序列转换为 Arduino 格式的字节序列。
    即每两个字节后面加两个\x00字节。
    """
    arduino_bytes = bytearray()
    for i in range(0, len(latin1_bytes), 2):
        arduino_bytes.extend(latin1_bytes[i:i+2])  # 取前两个字节
        arduino_bytes.extend(b'\x00\x00')  # 添加两个\x00字节
    return bytes(arduino_bytes)

def encrypt(plainText, verificationCode, publicKey):
    text_plain = plainText + verificationCode
    text_encrypt = RSA.encrypt(text_plain, publicKey)
    text_encrypt_encode = text_encrypt.encode('latin-1')
    return latin1_to_arduino(text_encrypt_encode)

def decrypt(cipherText, verificationCode, privateKey):
    cipherText = arduino_to_latin1(cipherText).decode('latin-1')
    text_decrypt = RSA.decrypt(cipherText, privateKey).rstrip('\x00')
    verificationCode_detected = text_decrypt[-len(verificationCode):]
    if verificationCode_detected != verificationCode:
        return None
    text_plain = text_decrypt[:-len(verificationCode)]
    return text_plain