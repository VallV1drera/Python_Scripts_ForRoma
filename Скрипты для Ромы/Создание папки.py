import os

src = "C:\\Users\\rgilin\\Desktop\\Организации\\"

while True:
    dirname = input("Введите название организации: ")
    os.mkdir(src + dirname)
    print("Папка создана.")
