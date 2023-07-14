#!/usr/bin
#Copyright 2022 fthV2.3

#Github: 

# Installer fthv2

# Colors
red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

# Location
path=$(pwd)

# Check root 
if [ "$(id -u)" != "0" ] > /dev/null 2>&1; then
echo -e '\n$red[x] Este script necesita permisos root.' 1>&2
exit
fi

echo -e "\n      Derechos de autor:   N | Copyright (c) 2022\n"
sleep 1
echo -e '      Derechos reservados: S | Licensia para: (c) fth\n\n'
sleep 1

# IMGFONT
echo -e "
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
"

# Check dependencies
echo -e $yellow
echo -n [*] Checando dependencias...= ;
sleep 3 & while [ "$(ps a | awk '{print $1}' | grep $!)" ] ; do for X in '-' '\' '|' '/'; do echo -en "\b$X"; sleep 0.1; done; done 
echo ""


# Check if xterm exists
which xterm > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo ""
echo -e "$green[✔][Xterm]------------------------->[ OK ]"
sleep 1.5
else
echo ""
echo -e "$red[x][Xterm]---------------------->[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Xterm...]"
sudo apt-get install -y xterm > /dev/null
fi

# Check if postgresql exists
which /etc/init.d/postgresql > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[✔][Postgresql].....................[ OK ]"
sleep 1.5
else
echo -e "$red[x][Postgresql]..................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Postgresql...]"
xterm -T "INSTALLER POSTGRESQL" -geometry 100x30 -e "sudo apt-get install -y postgresql"
fi 

# Check if metasploit framework exists 
which msfconsole > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[✔][Metasploit Framework]...........[ OK ]"
sleep 1.5
else
echo -e "$red[x][Metasploit Framework]........[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Metasploit-Framework...]"
xterm -T "INSTALLER METASPLOIT FRAMEWORK" -geometry 100x30 -e "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall && sudo apt-get update && apt-get upgrade"
fi

# Check if apktool exists 
which apktool > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[✔][Apktool]........................[ OK ]"
sleep 1.5
else
echo -e "$red[x][Apktool].....................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Apktool...]"
xterm -T "INSTALLER APKTOOL" -geometry 100x30 -e "wget -O apktool.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.4.0.jar && wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool && mv apktool* /usr/local/bin && chmod +x /usr/local/bin/apktool*"
fi

# Check if jarsigner exists
which jarsigner > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[✔][Jarsigner]......................[ OK ]"
sleep 1.5
else
echo -e "$red[x][Jarsigner]...................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Jarsigner...]"
xterm -T "INSTALLER JARSIGNER" -geometry 100x30 -e "sudo apt-get install default-jdk"
fi

# Check if zipalign exists
which zipalign > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[✔][Zipalign].......................[ OK ]"
sleep 1.5
else
echo -e "$red[x][Zipalign]....................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Installing Zipalign...]"
xterm -T "INSTALLER ZIPALIGN" -geometry 100x30 -e "sudo apt-get install -y zipalign"
fi


# Check if ngrok exists
arch=`arch`
if [ -f "ngrok" ]; then
echo -e "$green[✔][Ngrok]..........................[ OK ]"
sleep 1.5
else
echo -e "$red[x][Ngrok]........................[ NOT FOUND ]"
sleep 1.5
echo -e "$yellow[!][Downloading ngrok...]"
if [ "$arch" ==  "x86_64" ]; then
xterm -T "DOWNLOAD NGROK" -geometry 100x30 -e "wget https://bin.equinox.io/a/kpRGfBMYeTx/ngrok-2.2.8-linux-amd64.zip && unzip ngrok-2.2.8-linux-amd64.zip"
rm ngrok-2.2.8-linux-amd64.zip
else
xterm -T "DOWNLOAD NGROK" -geometry 100x30 -e "wget https://bin.equinox.io/a/4hREUYJSmzd/ngrok-2.2.8-linux-386.zip && unzip ngrok-2.2.8-linux-386.zip"
rm ngrok-2.2.8-linux-386.zip
fi
fi




# Installing requirements
echo -e $yellow
echo -n [*] Instalando requerimientos de python...= ;
sleep 3 & while [ "$(ps a | awk '{print $1}' | grep $!)" ] ; do for X in '-' '\' '|' '/'; do echo -en "\b$X"; sleep 0.1; done; done
echo ""
echo -e $green
apt-get install python3-tk
apt-get install libatk-adaptor libgail-common
sudo apt-get purge fcitx-module-dbus


# Shortcut for FTHV2.3
echo -e $yellow
echo -n [*] Configurando el acceso directo...= ;
sleep 3 & while [ "$(ps a | awk '{print $1}' | grep $!)" ] ; do for X in '-' '\' '|' '/'; do echo -en "\b$X"; sleep 0.1; done; done
echo ""
echo ""
echo -e "$green[!] ¿Desea poder ejecutar fthV2 desde el menu? {y/n}"
echo -e "$default"
echo -ne "fth >> $red"
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
echo -e $green
echo -e "╔──────────────────────────────────────────────────────────╗"
echo -e "|[✔] Installation complete. write 'fth' para correr fthV2.3|"
echo -e "┖──────────────────────────────────────────────────────────┙"
fi
;;

n|N)
sleep 2
echo -e $green
echo -e "╔──────────────────────────╗"
echo -e "|[✔] Instalacion completa..|"
echo -e "┖──────────────────────────┙"
;;
esac
exit