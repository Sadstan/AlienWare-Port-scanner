#ecoding:utf-8
import socket
print"""
  /$$$$$$  /$$ /$$
 /$$__  $$| $$|__/
| $$  \ $$| $$ /$$  /$$$$$$  /$$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$
| $$$$$$$$| $$| $$ /$$__  $$| $$__  $$| $$ | $$ | $$ |____  $$ /$$__  $$ /$$__  $$
| $$__  $$| $$| $$| $$$$$$$$| $$  \ $$| $$ | $$ | $$  /$$$$$$$| $$  \__/| $$$$$$$$
| $$  | $$| $$| $$| $$_____/| $$  | $$| $$ | $$ | $$ /$$__  $$| $$      | $$_____/
| $$  | $$| $$| $$|  $$$$$$$| $$  | $$|  $$$$$/$$$$/|  $$$$$$$| $$      |  $$$$$$$
|__/  |__/|__/|__/ \_______/|__/  |__/ \_____/\___/  \_______/|__/       \_______/
-h para instrucoes
"""

help = raw_input("[+] Digite -h [+] : ")

if help == '-h':
    print"""
        Codado by SadStan
        Greetz: Diogo Makaveli
        PortScan 1.0
        AlienWare
    """
else:
    print"Opcao invalida"

ip = raw_input("[+] IP OR ADDRESS [+]: ")
ports = []
count = 0

while count < 10:
    ports.append(int(raw_input("[+] PORT [+]: ")))
    count +=1
print("\n")
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.15)
    code = client.connect_ex((ip, port))

    if code == 0:
        print str(port) +"-> Porta aberta"
    else:
        print str(port) +" -> Porta fechada"
print("\n")
print("FINALIZED")