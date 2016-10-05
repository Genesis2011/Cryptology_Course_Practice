# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:29:08 2016

@author: 李厚峰

仿射密码:
明文中所有字母都由一简单数学方程加密
当加密函数（ax+b） （mod 26）中的a=1时，仿射密码为凯撒密码
"""

# 加密函数 （ax+b） （mod 26）
print("加密函数：（ax+b） （mod 26），请输入参数a、b的值： ")
a = int( input("a： ") )
b = int( input("b： ") )

Alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets = 'abcdefghijklmnopqrstuvwxyz'

plain_text = input("明文（区分大小写及空格）： ")
cipher_text = ''

# 根据是否是字符，以及字符的大小写情况，计算密文
for key in range(len(plain_text)):
    if plain_text[key].isupper():
        cipher_text += Alphabets[( a * Alphabets.find(plain_text[key]) + b )%26]
    elif plain_text[key].islower():
        cipher_text += alphabets[( a * alphabets.find(plain_text[key]) + b )%26]
    else:
        cipher_text += plain_text[key]

print("密文：  "+cipher_text)