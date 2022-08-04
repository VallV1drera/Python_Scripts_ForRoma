import socket
import asyncio

async def input_message():
    msg = conn.recv(1024).decode()
    print(f"{address} {msg}")

async def send_message():
    answ = input("Сообщение: ")
    conn.send(answ.encode())

async def connect(tasks):
    conn, address = server.accept()
    print("Новое подключение от " + str(address))
    task1 = asyncio.create_task(input_message())
    task2 = asyncio.create_task(send_message())
    tasks.append(task1, task2)
    await asyncio.gather(*tasks)

async def main():
    tasks = []
    task = asyncio.create_task(connect(tasks))
    tasks.append(task)

HOST = "192.168.0.11"
PORT = 2000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("Сервер запущен!")

asyncio.run(main())







