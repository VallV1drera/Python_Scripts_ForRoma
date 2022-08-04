import shutil
import os

dst = "C:\\Users\\rgilin\\Desktop\\Организации\\"


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


while True:
    b = input("Введите название организации: ")
    if b == "help":
        print("Список доступных шаблонов:\n1. 3608 СО\n2. 2458 СО\n3. ИС ЕПТ АЦ")
        continue
    dst2 = dst + b
    a = input("Введите номер сети: ")
    if a == "3608":
        src = "C:\\Users\\rgilin\\Desktop\\Шаблоны\\3608 СО ЦИТиС"
        print("Выбрана сеть: " + a)
        print("Путь к папке с шаблонами: " + src)
        f = input("Подтверждаете? (Д/Н) ")
        if f == 'Д' or f == 'д':
            os.mkdir(dst + b)
            os.mkdir(dst + b + "\\Старый ОРД") 
            print("Копирование файлов...")
            copytree(src, dst2)
            print("Копирование файлов завершено!\n")
        elif f == 'Н' or f == 'н':
            print("Отмена...")
            exit()
        else:
            print("Неверный ввод! Отмена...\n")
            
    if a == "2458":
        src = "C:\\Users\\rgilin\\Desktop\\Шаблоны\\2458 СО ФЦТ"
        print("Выбрана сеть: " + a)
        print("Путь к папке с шаблонами: " + src)
        f = input("Подтверждаете? (Д/Н) ")
        if f == 'Д' or f == 'д':
            os.mkdir(dst + b)
            os.mkdir(dst + b + "\\Старый ОРД")
            print("Копирование файлов...")
            copytree(src, dst2)
            print("Копирование файлов завершено!\n")
        elif f == 'Н' or f == 'н':
            print("Отмена...")
            exit()
        else:
            print("Неверный ввод! Отмена...\n")

    if a == "ИС ЕПТ" or a == "ис епт" or a == "исепт" or a == "ИСЕПТ":
        src = "C:\\Users\\rgilin\\Desktop\\Шаблоны\\ИС ЕПТ"
        print("Выбрана сеть: " + a)
        print("Путь к папке с шаблонами: " + src)
        f = input("Подтверждаете? (Д/Н) ")
        if f == 'Д' or f == 'д':
            os.mkdir(dst + b)
            os.mkdir(dst + b + "\\Старый ОРД")
            print("Копирование файлов...")
            copytree(src, dst2)
            print("Копирование файлов завершено!\n")
        elif f == 'Н' or f == 'н':
            print("Отмена...")
            exit()
        else:
            print("Неверный ввод! Отмена...\n")

    if a == "help":
        print("Список доступных шаблонов:\n1. 3608 СО\n2. 2458 СО\n3. ИС ЕПТ АЦ")
