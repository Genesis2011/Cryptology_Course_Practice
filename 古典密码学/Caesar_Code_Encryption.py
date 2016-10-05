# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:19:41 2016

@author: 李厚峰

凯撒密码:
明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文
"""

offset = int( input("偏移量： ") )
Alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets = 'abcdefghijklmnopqrstuvwxyz'

plain_text = input("明文（区分大小写及空格）： ")
cipher_text = ''

# 根据是否是字符，以及字符的大小写情况，计算偏移后的密文
for key in range(len(plain_text)):
    if plain_text[key].isupper():
        cipher_text += Alphabets[( Alphabets.find(plain_text[key]) + offset )%26]
    elif plain_text[key].islower():
        cipher_text += alphabets[( alphabets.find(plain_text[key]) + offset )%26]
    else:
        cipher_text += plain_text[key]

print("密文：  "+cipher_text)