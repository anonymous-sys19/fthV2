#!/usr/bin

echo -e '   
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

'


path=$(pwd)
printf '
		|******************************************************|
		| [ * ]          Instalacion fth-linux          [ * ]  |
		|******************************************************|
'
#xterm
which xterm > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e " [ y ] [Xterm]..........................[ yes ] ✔"
sleep 1.5
else
echo ""
echo -e " [ n ] [Xterm]...........................[ NOT ] x"
sleep 1.5
echo -e " [ 💀 ] [Installing Xterm...] 💀"
sudo apt-get install -y xterm > /dev/null
fi

#zipalign
which /etc/init.d/zipalign > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e " [ y ] [zipalign]........................[ yes ] ✔"
sleep 1.5
else
echo -e " [ n ] [zipalign]........................[ NOT ] x"
sleep 1.5
echo -e " [ 💀 ] [Installing zipalign.....] 💀"
xterm -T " INSTALLER ZIPALIGN" -geometry 100x30 -e "sudo apt-get install -y zipalign"
fi 


#postgresql
which /etc/init.d/postgresql > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e " [ y ] [Postgresql].....................[ yes ] ✔"
sleep 1.5
else
echo -e " [ n ] [Postgresql]........................[ NOT ] x"
sleep 1.5
echo -e " [ 💀 ] [Installing Postgresql...] 💀"
xterm -T " INSTALLER POSTGRESQL" -geometry 100x30 -e "sudo apt-get install -y postgresql"
fi 

#metasploit framework 
which msfconsole > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e " [ y ] [Metasploit Framework]...........[ yes ] ✔"
sleep 1.5
else
echo -e " [ n ] [Metasploit Framework]...........[ NOT ] x"
sleep 1.5
echo -e " [ 💀 ][Installing Metasploit-Framework...] 💀"
xterm -T "INSTALLER METASPLOIT FRAMEWORK" -geometry 100x30 -e "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall && sudo apt-get update && apt-get upgrade"
fi

# apktool
which apktool > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e " [ y ] [Apktool]........................[ yes ] ✔"
sleep 1.5
else
echo -e " [ n ] [Apktool]........................[ NOT ] x"
sleep 1.5
echo -e " [ 💀 ][Installing Apktool...] 💀"
xterm -T "INSTALLER APKTOOL" -geometry 100x30 -e "wget -O apktool.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.4.0.jar && wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool && mv apktool* /usr/local/bin && chmod +x /usr/local/bin/apktool*"
fi


# Check if ngrok exists
arch=`arch`
if [ -f "ngrok" ]; then
echo -e " [ y ] [Ngrok]..........................[ yes ] ✔"
sleep 1.5
else
echo -e " [ n ] [Ngrok]..........................[ NOT ] x"
sleep 1.5
echo -e " [ 💀 ] [Downloading ngrok----] 💀"
if [ "$arch" ==  "x86_64" ]; then
xterm -T " DOWNLOAD NGROK" -geometry 100x30 -e "wget https://bin.equinox.io/a/kpRGfBMYeTx/ngrok-2.2.8-linux-amd64.zip && unzip ngrok-2.2.8-linux-amd64.zip"
rm ngrok-2.2.8-linux-amd64.zip
else
xterm -T " DOWNLOAD NGROK" -geometry 100x30 -e "wget https://bin.equinox.io/a/4hREUYJSmzd/ngrok-2.2.8-linux-386.zip && unzip ngrok-2.2.8-linux-386.zip"
rm ngrok-2.2.8-linux-386.zip
fi
fi

echo -e '\n\n[ * ] [ Espere .....]\n\n'
echo -n   [ 0 ] Instalando requerimientos pip3...= ;
sleep 3 & while [ "$(ps a | awk '{print $1}' | grep $!)" ] ; do for X in '-' '\' '\' '/'; do echo -en "\b$X"; sleep 0.1; done; done
echo ""
pip install re
pip install random
pip install time
pip install requests
pip install py-getch
apt-get install python3-tk
apt-get install libatk-adaptor libgail-common
sudo apt-get purge fcitx-module-dbus


printf "\n      Derechos de autor:   N | Copyright (c) 2021\n"
sleep 1
printf '      Derechos reservados: S | Licensia para: (c) fth\n\n'
sleep 1
printf 'Creando orden dependencia: | 01 \n'
sleep 0.70
printf 'Creando acceso directo:    | 02 \n'
sleep 1
printf 'Creando Icono en el menu:  | 03 \n'
sleep 0.50
printf 'Escribiendo acceso directo:| 04 \n\n'
sleep 1
echo -e "$green[!] ¿Press ? (y) para continuar"
echo -ne "fth >> $default"
read -r option
case "$option" in

y|Y)
lnk=$?
if [ "$lnk" ==  "0" ];then
run="cd $path && sudo python3 fth.py"
touch /usr/local/bin/fth
echo "#!/bin/bash" > /usr/local/bin/fth
echo "$run" >> /usr/local/bin/fth
chmod +x /usr/local/bin/fth
cp images/fth.desktop /usr/share/applications/fth.desktop
cp images/fth.png /usr/share/icons/fth.png
sleep 2
echo -e 
echo -e "       ╔───────────────────────────────────────────────╗"
echo -e "       |[@] Instalacion completa [write [fth] to open  |"
echo -e "       ┖───────────────────────────────────────────────┙"
fi
;;
esac
exit
