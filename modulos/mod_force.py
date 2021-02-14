import time
import os
import random

def colores ():
    listas = ['\033[1;36m','\033[1;31m','\033[1;34m','\033[1;30m','\033[1;37m','\033[1;35m','\033[1;32m','\033[1;33m']
    indice=random.randrange(len(listas))
    lista=listas[indice]
    print(lista)

# ----=cls,clear=---
def clear_cleanner():
    os.system('clear')
#-----KeyboardInterrupt----
#     -----not_start-----

#banner
print ('''\033[1;31m\033[1;3m   
         _______  _______  __   __ 
        |       ||       ||  | |  |
        |    ___||_     _||  |_|  |
        |   |___   |   |  |       |
        |    ___|  |   |  |       |
        |   |      |   |  |   _   |
        |___|      |___|  |__| |__|
\033[1;34m                    _______  _______  ______    _______  _______ 
                    |       ||       ||    _ |  |       ||       |
                    |    ___||   _   ||   | ||  |____   ||    ___|
                    |   |___ |  | |  ||   |_||_  ____|  ||   |___ 
                    |    ___||  |_|  ||    __  || ______||    ___|
                    |   |    |       ||   |  | || |_____ |   |___ 
                    |___|    |_______||___|  |_||_______||_______|
''')
print('''
                       \033[1;32m|------------------------------------------|\033[1;0m
                       \033[1;32m| \033[1;34m[*]\033[1;0m     \033[1;36mBrute_Forze__ftp_Forze \033[1;0m          \033[1;32m|\033[1;0m
                       \033[1;32m|__________________________________________|\033[1;0m''')
def menu():
    colores()
    time.sleep(0.50)
    salir = (os.system('exit'))
    colores()
    opciones = (''' 
    [ -01- ] Scann_Puertos
    [ -02- ] Brute_ftp
    [ -03- ] Brute_ssh
    [ -04- ] mysql_force
    [ -00- ] volver al menu
    [ -99- ] salir \n\n\n''')
    print(opciones)
#>----ffor opcion---<

def link():
    colores()
    menu()
    opcion = int(input('\033[1;31m💀\033[1;45m==>\033[1;0m\033[1;41m \033[1;44m$\033[1;0m '))
    colores()
    if opcion == 1 :
        scan_nmap = input('Ingresa ip a scanear $ ')
        os.system('nmap ' + scan_nmap)
        menu()
        link()
    elif opcion == 2 :
        print(' Espere ingresando al systema ftp modulo\n')
        print('\n\n Espere Ejecutando la herramienta \n\n')
        print('\n                  Brute_Forze__ftp_Forze\n\n')
        time.sleep(0.50)

        print('\n Quiere hacer el Brute_Forze__ftp_Forze [y/n]\n\n')
        nameif = input('$ ')
        if nameif == 'y' :
            print('\n En breve se ejecutara Brute_Forze__ftp_Forze \n')
            time.sleep(2)
            os.system('bash modulos/modsh/ftp_brute.sh')
        elif nameif == n :
            print (' Perfecto vuelve pronto ... ')
            link()
    elif opcion == 3 :
	    print ('Creando orden ... \n' )
	    time.sleep(2)
	    os.system('bash modulos/modsh/ssh_brute.sh')
    elif opcion == 4 :
        os.system('clear')
        os.system('bash modulos/modsh/mysql_force.sh')
    elif opcion == 99 :
        os.system ('exit')
    elif opcion == 00 :
        os.system('clear')
        os.system('python3 fth.py')
    elif opcion != opcion :
        print('error')
        link()
    else :
        print('error')
        os.system('clear')
        link()
link()
