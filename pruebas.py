
import platform
from partials import windows as windows_Platform
from partials import linux as linux_Platform

try:

    sistema = platform.system()

    def systema_Operativo(sistema):
        if sistema == "Windows":
            print("[+] {}".format(sistema))
            windows_Platform
            
        elif sistema == 'Linux':
            print("[+] {}".format(sistema))
            linux_Platform

except:
    Exception("{+} File type Eror: Solo admite Linux and Windows")
    exit()
