import platform
from windows import windows as windows_Platform
from linux import linux as linux_Platform

try:

    sistema = platform.system()

    def systema_Operativo(sistema):
        if sistema == "Windows":
            print("[+] {}".format(sistema))
            windows_Platform
            pass
            
        elif sistema == 'Linux':
            print("[+] {}".format(sistema))
            linux_Platform
            pass

except KeyboardInterrupt:
    Exception("{+} File type Eror: Solo admite Linux and Windows")
    exit()
