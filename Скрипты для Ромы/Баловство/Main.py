import subprocess
import sys
import os
import getpass
import webbrowser

path = 'C:\Logopass\logopass.txt'
pathToNotepad = 'C:\\Windows\\System32\\notepad.exe'
a = 0
flag = 0

def GetLogoPass():
    f = open(path, 'r')
    logo = f.readline(20).rstrip()
    pess = f.readline(20)
    f.close()
    return logo, pess

def DrawAndInput():
    DrawMenu()
    a = input ("Введите число: ")
    checkInput(a)

def GetUserLogoPass():
    login = input("Введите логин: ")
    if login == "exit":
        sys.exit()
    password = getpass.getpass('Введите пароль: ')
    Comparison(login, password)

def Comparison(ulogin, upassword):
    login = GetLogoPass()[0]
    password = GetLogoPass()[1]
    if login == ulogin and password == upassword:
        DrawAndInput()
    else:
        print ("Неверный логин или пароль!\n")
        GetUserLogoPass()

def checkInput(a):
    path = 'C:\Logopass\logopass.txt'
    pathToNotepad = 'C:\\Windows\\System32\\notepad.exe'
    if a == "1":
        f = open(path, 'w')
        login_change = input ("\nВведите новый логин: ")
        print ("Новый логин: " + login_change)
        password_change = getpass.getpass("Введите пароль новый: ")
        print ("Новый пароль: Ты сам знаешь, запоминать надо!")
        if login_change != "" and password_change != "":
            f.write (login_change + '\n')
            f.write (password_change)
            f.close()
            print ("Логин и пароль успешно изменены!\n")
        else:
            print ("Ты чё, ебанутый? Напиши хоть что-нибудь!")
            checkInput(a)
    elif a == "2":
        subprocess.Popen([pathToNotepad, path])
        print ("Файл " + path + " успешно запущен" + "\n")
        DrawAndInput()
    elif a == "5":
        print ("Производится завершение приложения...")
        print ("Приложение завершено")
        sys.exit()
    elif a == "3":
        webbrowser.open_new('https://crm.rus-telecom.ru/')
        print ("CRM открыт")
        DrawAndInput()
    elif a == "4":
        print ("Выход из учётной записи\n")
        GetUserLogoPass()
    else:
        print ("Ты чё, ебанутый? Нормальную циферку напиши!")
        DrawAndInput()
    GetUserLogoPass()

def DrawMenu():
    print ("\nДобро пожаловать, " + GetLogoPass()[0] + "!")
    print ("Доступные действия:")
    print ("1. Изменить логин и пароль")
    print ("2. Запустить файл")
    print ("3. Открыть CRM")
    print ("4. Выйти")
    print ("5. Завершить приложение")

def Start():
    GetLogoPass()
    GetUserLogoPass()

Start()

