import getpass
import hashlib
import requests
import sys

def ask_for_password():
    password = getpass.getpass(prompt = "\n\nPorfavor introduce tu contraseña: \n\n", stream = None)
    if password == "" or password.isspace():
        print("Please type a password!")
        sys.exit(1)

    password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return password
    

def check_password(password):
    first_characters = password[0:5]
    response = requests.get("https://api.pwnedpasswords.com/range/{}".format(first_characters))
    response = response.text.splitlines()
    for h in response:
        if password[6:] in h:
            return h.split(":")[1]

    return 0

if __name__ == "__main__":
    result = check_password(ask_for_password())
    if result != 0:
        print("Tu contraseña a sido {} veses publicada en la web.".format(result))
        #print("Source: https://haveibeenpwned.com/")
    else:
        print("No aparece la contraseña en la web.")