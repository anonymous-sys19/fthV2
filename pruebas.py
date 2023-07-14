import platform

def systema_Operativo(sistema):
    sistema=platform.system()
    if (sistema=="Windows"):
        return "Sistemas operativos Windows"
    elif (sistema=="Linux"):
        return "Sistemas Operativos Linux"
    else:
        print("No se reconose el sistema operativo")

systema_Operativo()