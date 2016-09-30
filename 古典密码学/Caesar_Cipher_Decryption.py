# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:57:36 2016

@author: 李厚峰

暴力破解凯撒密码
这里的偏移量指向右移动，即偏移量为2时，向右移动2
"""

cipher_text = input("密文（区分大小写及空格）： ")

Alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets = 'abcdefghijklmnopqrstuvwxyz'

for key in range(len(cipher_text)):
    plain_text = ''
    for char in cipher_text:
        if char in Alphabets:
            plain_text += Alphabets[(Alphabets.index(char) + key ) %26]
        elif char in alphabets:
            plain_text += alphabets[(alphabets.index(char) + key ) %26]
        else:
            plain_text += char
    print('Key #%s：%s' % (key,plain_text))