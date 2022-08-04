import socket
from tqdm import tqdm
import struct

client = socket.socket()
client.connect(("192.168.0.11", 2000))
print ("Есть контакт!")
f_name = client.recv(1024).decode()
f = open(f_name, 'wb')
client.send("1".encode())
size = int(client.recv(1024).decode())
client.send("2".encode())
print(size)
data = client.recv(1024)
with tqdm(total=size, desc="Получение", unit=" Bytes") as pbar:
    while data:
        pbar.update(1024)
        f.write(data)
        data = client.recv(1024)
    f.close()
    client.close()
    print(f"Файл {f_name} успешно получен!")