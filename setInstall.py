
import os
import platform
import pathlib
import sys
import time







try:

    print ('''   
            _______  _______  __   __ 
            |       ||       ||  | |  |
            |    ___||_     _||  |_|  |
            |   |___   |   |  |       |
            |    ___|  |   |  |       |
            |   |      |   |  |   _   |
            |___|      |___|  |__| |__|
                        ___   __    _  _______  _______  _______  ___      ___     
                        |   | |  |  | ||       ||       ||   _   ||   |    |   |    
                        |   | |   |_| ||  _____||_     _||  |_|  ||   |    |   |    
                        |   | |       || |_____   |   |  |       ||   |    |   |    
                        |   | |  _    ||_____  |  |   |  |       ||   |___ |   |___ 
                        |   | | | |   | _____| |  |   |  |   _   ||       ||       |
                        |___| |_|  |__||_______|  |___|  |__| |__||_______||_______|

    ''')


    print('''
            |******************************************************|
            | [ * ]          Instalacion fth-Windows        [ * ]  |
            |******************************************************|
    ''')







    def slowprint(s):
                for c in s + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(20./100)         



    def Check_Wget():
        slowprint("Ckeck wget: ... ")
        
        if  os.path.exists(r'C:\Program Files (x86)\GnuWin32\bin\wget.exe') == True:
            print("\n\n[+] Wget to Installed")
        else:
            slowprint("No Instalado_Intentando instalar ... Wget ")
            
            os.system('python -m webbrowser -t "https://iweb.dl.sourceforge.net/project/gnuwin32/wget/1.11.4-1/wget-1.11.4-1-setup.exe"')
            
            print('\n\nPreciona Cuando Termines de  Instalar Wget\n')
            os.system("pause")
            os.system(r'setx path "%path%;C:\Program Files (x86)\GnuWin32\bin"')
            


    Check_Wget()
    
    def DIR_User():
        Directorio = os.getcwd()
        usere = ('{}'.format(Directorio))
        user = open('user.txt', 'w')
        user.write(usere)

    DIR_User()
    def msfconsoleInstall():

        Nombre =(' Metasploit_Framework ')
        slowprint(' Check.. if '+ Nombre+' Is Installed ... ')

        if  os.path.exists(r'C:\metasploit-framework\bin') == True:
            print('[+]'+Nombre+' Ya Fue Instalado.. \n\n')
            
        else:

            NOTA = ("""
                MsfConsole Para windows es la version Free, el cual podras usar
                por medio de Comandos como si fuese Linux. pero la instalacion requiere
                su propia configuracion manual para instalar en el Path// y usar desde CMD
                Instala y no cambies su ubicacion por defecto..
            
            """)

            
            Information = ('''

                Nota: Una vez descargado el archivo no continues y dirijete ala ruta  
                Donde se Descargo''' +Nombre+''' y procede a instalarlo  
                Se abrira una ventana donde cuando tu Finalicez la instalacion  
                Aceptaras con /Y/ sete agregara al Path y podras hacer uso de '''+Nombre+''' desde CMD  
                
                ''')
            print(NOTA)
            install = input("Seguir instalando y/n.. : ")
            
            if install == 'y' or install== 'Y':
                slowprint('\n Instalando...'+Nombre)
                os.system("wget --no-check-certificate https://windows.metasploit.com/metasploitframework-latest.msi")
                

                print(Information)

                Aceptacion = input("Press Y/y cundo instales"+Nombre+": ")
                if Aceptacion == 'y' or Aceptacion == 'Y':
                    os.system(r'setx path "%path%;C:\metasploit-framework\bin"')
                else:
                    print("Gracias por usar FthV2_Win32")
            else:
                os.system('pause')

    msfconsoleInstall()


    
        
except KeyboardInterrupt:
    print(KeyboardInterrupt(" {Error: }Programa Detenido"))
else:
    print('False: Programa_Finalizado... ')