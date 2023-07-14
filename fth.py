#!/usr/bin/python
import platform

from partials import windows as windows_Platform
from partials import linux as linux_Platform
 
try:
    
    sistema = platform.system()
    
    if sistema == "Windows":
        print("[+] {}".format(sistema))
        windows_Platform
except:
        print(Exception("{+} File type Eror: Solo admite Linux and Windows"))
        exit()


  # DIVICION DEL SISTEMA OPERATIVO
try:

    if sistema == "Linux":
        print("[+] {}".format(sistema))
        linux_Platform

except:
  Exception("{+} File type Eror: Solo admite Linux and Windows")
  exit()