#coding=utf-8
import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    from tfa import menu
    menu()
elif bit == '32bit':
    from tfa32 import menu
    menu()
else:
    print ('\033[0;96mYour mobile not supported')
    exit()
