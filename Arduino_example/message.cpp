#include "message.h"

void decrypt(char *plainText, char *chipherText, char *verificationCode, int *privateKey)
{
    rsa.decrypt(plainText, chipherText, privateKey);

    int len = strlen(plainText);
    int count = 0;
    for (int i = len - 1; i >= 0 && count < 5; i--) {
        if (plainText[i] != ' ') {
            verificationCode[4 - count] = plainText[i];
            plainText[i] = '\0';
            count++;
        }
    }
}

void encrypt(char *plainText, char *chipherText, char *verificationCode, int *publicKey)
{
    int len = strlen(plainText);
    for (int i = 0; i < 5; i++) {
        plainText[len + i] = verificationCode[i];
    }

    rsa.encrypt(plainText, chipherText, publicKey);
}