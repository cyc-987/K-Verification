#ifndef __MESSAGE_H__
#define __MESSAGE_H__

#include "RSA.h"
#define VERIFICATION_SIZE 5

void decrypt(char *plainText, char *chipherText, char *verificationCode, int *privateKey);
void encrypt(char *plainText, char *chipherText, char *verificationCode, int *publicKey);

#endif