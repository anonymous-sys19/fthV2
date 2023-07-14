import os
import random
import sys
import time

# if sistema == "Windows":
#         print("[+] {}".format(sistema))
#

def colores():
    listas = ['\033[1;36m', '\033[1;31m', '\033[1;34m', '\033[1;30m', '\033[1;37m', '\033[1;35m', '\033[1;32m',
              '\033[1;33m']
    indice = random.randrange(len(listas))
    lista = listas[indice]
    print(lista)


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 100)


def fth():
    colores()
    listalinuxs = ['''
                    ████████        ███      █████
                    ███░░███      ░░███     ░░███
                   ░███░░░       ████████    ░████████
                    ███████      ░░░███░     ░███░░███
                 ░░░███░           ░███      ░███ ░███
                   ░███             ███      ░███ ░███
                    ███             ███    ██████ █████
                    ░░░░░     ░░    ░░░░░  ░░ ░░░░ ░░░░░ 
                                                    ''', '''
                '########::::::'########::::::'##::::'##:
                ##.....:::::::... ##..::::::: ##:::: ##:
                ##::::::::::::::: ##::::::::: ##:::: ##:
                ######::::::::::: ##::::::::: #########:
                ##...:::::::::::: ##::::::::: ##.... ##:
                ##:::::::'###:::: ##::::'###: ##:::: ##:
                ##::::::: ###:::: ##:::: ###: ##:::: ##:
                ..::::::::...:::::..:::::...::..:::::..::
                                                    ''', '''
                        ███████╗████████╗ ██╗  ██╗
                        ██╔════╝╚══██╔══╝ ██║  ██║
                        █████╗     ██║    ███████║
                        ██╔══╝     ██║    ██╔══██║
                        ██║██╗     ██║██╗ ██║  ██║
                        ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝ 
                                        ''', '''
                    O))  O))           O))
                O)     O))  O))      O)) O)
                O)O) O)O)O) O)O))      O))   O)) O))  O))  O))O))   O))
                O))    O))  O) O)    O))O)) O))  O))O))  O))  O) O))
                O))    O))  O))  O)) O))O)) O))  O))O))  O))   O)
                O))    O))  O)   O)) O))O)) O))  O))O))  O)) O)  O))
                O))     O)) O))  O))O)))O))O)))  O))  O))O))O))   O))
        ''', '''
            .%%%%%%..%%%%%%..%%..%%..%%......%%%%%%..%%..%%..%%..%%..%%..%%.
            .%%........%%....%%..%%..%%........%%....%%%.%%..%%..%%...%%%%..
            .%%%%......%%....%%%%%%..%%........%%....%%.%%%..%%..%%....%%...
            .%%........%%....%%..%%..%%........%%....%%..%%..%%..%%...%%%%..
            .%%........%%....%%..%%..%%%%%%..%%%%%%..%%..%%...%%%%...%%..%%.
            ................................................................
        ''', '''

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

    indice = random.randrange(len(listalinuxs))
    listalinux = listalinuxs[indice]
    slowprint(listalinux)
fth()


def clear():
    os.system('cls')


def help():
    print('''\n                                   \033[1;1m<------Menu_de ayuda_------>\n
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
    print(ayuda)


def create_new_Pass():
    print('Creando .txt ....')
    time.sleep(2)
    os.system('notepad New_Pass.txt')
    print('Creado con exito ....')


def create_new_user():
    print('Creando .txt ....\n')
    time.sleep(2)
    os.system('notepad New_user.txt')
    print('Creado con exito ....')


def password():
    from modulos import dicccionario
    diccionaripass = open('user_pass.txt', 'a')
    diccionaripass.write(dicccionario.user_pass)


def usuarios():
    from modulos import dicccionario
    diccionariuser = open('user_user.txt', 'a')
    diccionariuser.write(dicccionario.user_user)


def menu():
    colores()
    print('  \033[1;34m           _____________________________________________  ')
    print(
        '  \033[1;34m           ||\033[1;40m_________________\033[1;31m\033[1;31mMenu\033[1;0m\033[1;34m\033[1;40m_____________________\033[1;0m\033[1;34m||\033[1;0m')

    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print('  \033[1;34m           ||                                          ||\033[1;0m')
    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print(
        '  \033[1;34m           ||          \033[1;32mGenerar diccionario\033[1;0m\033[1;34m             ||\033[1;0m')
    print(
        '  \033[1;34m           ||         \033[1;32mCrear nuevo diccionario\033[1;0m\033[1;34m          ||\033[1;0m')
    print(
        '  \033[1;34m           ||         \033[1;32minteracion del systema\033[1;0m\033[1;34m           ||\033[1;0m')
    print('  \033[1;34m           ||  ______________________________________  ||\033[1;0m')
    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print('  \033[1;34m           ||                                          ||\033[1;0m')
    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print(
        '  \033[1;34m           ||  [Escribe [\033[1;36m\033[1;4mhelp\033[1;0m\033[1;34m] para ver modo de uso ]  ||\033[1;0m')
    print('  \033[1;34m           ||  --------------------------------------  ||\033[1;0m')
    print('  \033[1;34m           ||                                          ||\033[1;0m')
    print(
        '  \033[1;34m           ||___________\033[1;44m\033[1;32mby_anonimo_hackerpc\033[1;0m\033[1;34m____________||\033[1;0m')
    colores()
    print(' \n            -------------------welcome---------------------\n')
menu()


def creacion():
    usr_pas = input('\033[1;44m==>menu-->>\033[1;0m\033[1;36m\033[1;4m $ \033[1;0m')

    if usr_pas == 'menu':
        menu()
    elif usr_pas == "open msfconsole":
        import setInstall
        setInstall.msfconsoleInstall()
        creacion()
    elif usr_pas == 'help':
        clear()
        colores()
        help()
        colores()
        creacion()
    elif usr_pas == 'use hacker_git':
        colores()
        print(' Instalando ')
        time.sleep(1)
        print('Instalacion..escribe la ruta a guardar la herramienta .. \n')
        instalacion = input('$rute $ ')
        os.system('git clone https://github.com/anonymous-sys19/Hacker.git')
        os.system("mv Hacker " + instalacion)
        print('\n       listo se instalo con exito\n')
        creacion()
    elif usr_pas == 'set fb-id':
        os.system('python2 modulos/ID-F-BOOK.py')
        creacion()
    elif usr_pas == 'create_new_pass':
        create_new_Pass()
    elif usr_pas == 'create_new_user':
        create_new_user()
    elif usr_pas == 'exit':
        clear()
        colores()
        print('\n--------Saludes un gusto adios-----\n\n')
        os.system('exit')
    elif usr_pas == 'clear':
        clear()
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
        clear()
        os.system('python modulos/mod_force.py')
        colores()
        creacion()
    elif usr_pas == 'create user list':
        usuarios()
        print('Creado con exito ....')
        time.sleep(2)
        clear()
        creacion()
    elif usr_pas == 'create pass list':

        password()
        print('Creado con exito .... ')
        time.sleep(2)
        clear()
        creacion()
    elif usr_pas == 'create automated payload':
        os.system('bash modulos/modsh/modulo_payload.sh')
        colores()
        creacion()
    elif usr_pas == 'sublime text install':
        os.system(
            'wget --no-check-certificate  https://download.sublimetext.com/sublime_text_build_4121_x64_setup.exe')
        print("\n\n Deve contener C: Users etc... \n")
        ruta = input("Ingresa una Ruta a mover tu Archivo.exe")

        if ruta == ruta:
            os.system('move sublime_text_build_4121_x64_setup.exe ' + ruta)
        else:
            print("\nError: No ingresaste Ruta...")
        creacion()
    elif usr_pas == 'tor-desktop install':
        print('''  
                    Nota : Solo descargara el .tar.xz [en la ruta que lo establescas ]\n''')
        os.system(
            'wget --no-check-certificate  https://dist.torproject.org/torbrowser/11.0.2/torbrowser-install-win64-11.0.2_en-US.exe')
        inport = input(' Ruta a guardar tu .tar.xz => ')
        if inport == inport:
            os.system('move torbrowser-install-win64-11.0.2_en-US.exe ' + inport)
        else:
            print("\nError: No ingresaste Ruta...")
        creacion()
    elif usr_pas == 'use check-pass':
        os.system('python modulos/checkpass.py')
        input('\n\nPress enter para coontinuar\n')
        clear()
        creacion()
    elif usr_pas == usr_pas:
        os.system(usr_pas)
        colores()
        creacion()
    elif usr_pas != usr_pas:
        clear()
        print('\n\n error ')
        creacion()


creacion()
