import os
import random
import socket
import sys
import time
from os import system, name, path
import brutedum as brutedum
from menuFth import fthmain as fth
from helper import help as helper
from menuFth import menu as menu
from modulos import locateip as iplocate

def colores():
    listas = ['\033[1;36m', '\033[1;31m', '\033[1;34m', '\033[1;30m', '\033[1;37m', '\033[1;35m', '\033[1;32m',
              '\033[1;33m']
    indice = random.randrange(len(listas))
    lista = listas[indice]
    print(lista)

def cls():
    os.system('cls')

menu

def fluxion():
    a = ('fluxion')
    print('instalacion de ' + a)
    fluxio = os.system('git clone https://github.com/FluxionNetwork/fluxion.git')
    cls()
    os.system('mv fluxion /root')
    os.system('cd fluxion')
    os.system('bash fluxion.sh')
    os.system('./fluxion.sh -i')
    print("\n\n Instalado con exito [/root] \n")


def create_new_Pass():
    print('Creando .txt ....')
    time.sleep(2)
    os.system('nano New_Pass.txt')
    print('Creado con exito ....')


def create_new_user():
    print('Creando .txt ....\n')
    time.sleep(2)
    os.system('nano New_user.txt')
    print('Creado con exito ....')


fth


def chmod():
    os.system('chmod 777 -R *')


def creacion():
    usr_pas = input('\033[1;44m==>menu-->>\033[1;0m\033[1;36m\033[1;4m $ \033[1;0m')

    if usr_pas == 'menu':
        menu.menu()
    elif usr_pas == 'help':
        colores()
        cls()
        helper()
        colores()
        creacion()
    
    elif usr_pas == 'set fb-id':
        os.system('python2 modulos/ID-F-BOOK.py')
        creacion()
    elif usr_pas == 'clear':
        cls()
        colores()
        creacion()
    elif usr_pas == 'use force_brute':
        colores()
        print('..........')
        time.sleep(0.50)
        print(' ..........')
        time.sleep(0.50)
        print('-----abriendo modulo-----')
        colores()
        time.sleep(0.50)
        print('..........')
        time.sleep(0.50)
        print('..........')
        time.sleep(0.50)
        cls()
        os.system('python3 modulos/mod_force.py')
        colores()
        creacion()
    elif usr_pas == 'install fluxion':
        fluxion()
        creacion()
    elif usr_pas == 'open msfconsole':
        print('pleace wait ... execute msfconsole \n\n')
        os.system('msfconsole')
        creacion()
    elif usr_pas == 'create automated payload':
        os.system('bash modulos/modsh/modulo_payload.sh')
        colores()
        creacion()
    elif usr_pas == usr_pas:

        creacion()
    
    elif usr_pas == 'use Brute':
        brutedum()
        cls()
        creacion()
    elif usr_pas == 'use check-pass':
        os.system('python3 modulos/checkpass.py')
        input('\n\nPress enter para coontinuar\n')
        cls()
        creacion()
    elif usr_pas == 'set locate':
        iplocate()
        creacion()
    elif usr_pas == usr_pas:
        os.system(usr_pas)
        colores()
        creacion()
    elif usr_pas != usr_pas:
        cls()
        print('\n\n error ')
        creacion()

creacion()
