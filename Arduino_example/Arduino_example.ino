#include "RSA.h"
#include "message.h"

// 预先定义的消息
char msg_hello[PLAINTEXT_SIZE] = "hello";
char msg_ryou[PLAINTEXT_SIZE] = "ryou";
char msg_error[PLAINTEXT_SIZE] = "error";

int publicKey_up[2] = {14351, 11};
int publicKey[2] = {9379, 11};
int privateKey[2] = {9379, 835};

void setup()
{
  Serial.begin(9600);
}
void loop()
{
    // 生成变量并且初始化（清零）
    char cipher[CIPHERTEXT_SIZE];
    char plain[PLAINTEXT_SIZE];
    char verificationCode[VERIFICATION_SIZE];
    int i;
  
    memset(cipher, 0, CIPHERTEXT_SIZE);
    memset(plain, 0, PLAINTEXT_SIZE);
    memset(verificationCode, 0, VERIFICATION_SIZE);
    
    // 当串口有数据时，读取数据，长度为CIPHERTEXT_SIZE
    while(!Serial.available());
    if(Serial.available() > 0)
        Serial.readBytes(cipher, CIPHERTEXT_SIZE);

    
    // 调用我封装好的函数解密
    decrypt(plain, cipher, verificationCode, privateKey);

    // 判断密文并执行相应的功能
    if(rsa.compare(plain, msg_ryou, PLAINTEXT_SIZE))
    {
        // 首次接入验证
        memset(plain, 0, PLAINTEXT_SIZE);
        strncpy(plain, msg_hello, PLAINTEXT_SIZE);
    }else{
        // 处理未识别字符
        memset(plain, 0, PLAINTEXT_SIZE);
        strncpy(plain, msg_error, PLAINTEXT_SIZE);
    }

    // 调用我封装好的函数加密
    encrypt(plain, cipher, verificationCode, publicKey_up);

    // 发送加密后的密文
    for(i=0;i<CIPHERTEXT_SIZE;i++)
        Serial.write(cipher[i]);
    Serial.print("\n"); 
}