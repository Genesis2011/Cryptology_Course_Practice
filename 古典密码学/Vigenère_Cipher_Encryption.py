# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:48:58 2016

@author: 李厚峰

维吉尼亚密码：
恺撒密码的基础上扩展的多表密码
"""

secret_key = ( input("密钥： ")).replace(' ','').upper()

Alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets = 'abcdefghijklmnopqrstuvwxyz'

plain_text = input("明文（区分大小写及空格）： ")
cipher_text = ''

# 根据是否是字符，以及字符的大小写情况，计算密文
i = 0
for key in range(len(plain_text)):
    offset = Alphabets.find( secret_key[i % len(secret_key)] )
    if plain_text[key].isupper():
        cipher_text += Alphabets[( Alphabets.find(plain_text[key]) + offset )%26]
        i += 1
    elif plain_text[key].islower():
        cipher_text += alphabets[( alphabets.find(plain_text[key]) + offset )%26]
        i += 1
    else:
        cipher_text += plain_text[key]

print(cipher_text)