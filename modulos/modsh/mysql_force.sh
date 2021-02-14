#!/usr/bin/bash

echo -e '\n\n                      Bienvenido a la aventura mysql_force \n\n'
function help {
	echo -e """
		algo muy simple una vez encontrado el user y pass
		habres una terminal y escribes [mysql -h [ip] -u [usuario]] 
				ejemplo mysql -h 127.0.0.1 -u google
		si quieres volver atras escribe [menu]
		te guiara al menu force-brute
	"""
}

help
read -p "enter ip objetivo $ " rhosts
if [ $rhosts = help ]; then
	help
elif [ $rhosts = menu ]; then
	python3 fth.py	
fi
read -p "enter user_file $ " user_file
if [ $user_file = help ]; then
	help
elif [ $user_file = menu ]; then
	cd ..
	python3 fth.py
fi
read -p "enter pass_file $ " pass_file
if [ $pass_file = help ]; then
	help
elif [ $pass_file = menu ]; then
	cd ..
	python3 fth.py
fi
echo -e '\n                     pleace wait ...\n'
echo -e '\n\nEjecutando postgresql ...\n\n'
sudo service postgresql start
echo -e '\n                    [listo espere ........]'
msfconsole -x "use auxiliary/scanner/mysql/mysql_login;\
set PASS_FILE $pass_file;\
set USER_FILE $user_file;\
set rhosts $rhosts;\
run"
