import keyboard
import time
import test_progress

input_delay = 0.05
prog = test_progress.progress_bar_ilin

def PredORD():
    it = 9
    pr = 0
    prog.Progress(it, pr)
    keyboard.write("Мат", input_delay)
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.write("Прошу предоставить старый ОРД", input_delay)
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.write("Прошу предоставить старый ОРД", input_delay)
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("ctrl+v")
    pr += 1
    prog.Progress(it, pr)
    print("\nСкрипт закончил свою работу")
    time.sleep(2)

def CheckETK():
    it = 10
    pr = 0
    prog.Progress(it, pr)
    keyboard.write("Мат", input_delay)
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.write("Прошу проверить ЕТК", input_delay)
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.write("Прошу проверить ЕТК", input_delay)
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("ctrl+v")
    pr += 1
    prog.Progress(it, pr)
    print("\nСкрипт закончил свою работу")
    time.sleep(2)

def CheckOE(a):
    it = 10
    pr = 0
    prog.Progress(it, pr)
    keyboard.write("Мат", input_delay)
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.write("Прошу проверить ОЭ", input_delay)
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("tab")
    pr += 1
    prog.Progress(it, pr)
    keyboard.write("Прошу проверить ОЭ. ИНН: " + str(a), input_delay)
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("enter")
    pr += 1
    prog.Progress(it, pr)
    keyboard.send("ctrl+v")
    pr += 1
    prog.Progress(it, pr)
    print("\nСкрипт закончил свою работу")
    time.sleep(2)

def Otchet():
    time.sleep(1)
    for i in range(3, 0, -1):
        print("До запуска осталось: "+ str(i))
        time.sleep(1)
    print("Запуск...")

def main():
    print("Добро пожаловать в автоматизированный скрипт написания запросов к Матюхиной.")
    print("Предварительно ОБЯЗАТЕЛЬНО скопируй вырезку из CRM.")
    print("Выбери интересующий пункт:")
    print("1. Запросить ОРД")
    print("2. Проверить ЕТК")
    print("3. Проверить ОЭ")
    print("4. Выдать флешку")
    a = input("Выбор: ")
    if a == "1":
        print("Был выбран запрос ОРД. Программа ждёт 3 секунды. За это время ты должен переключиться на окно отправки сообщения в Outlook в поле ввода получателя.")
        Otchet()
        PredORD()
    if a == "2":
        print("Была выбрана проверка ЕТК. Программа ждёт 3 секунды. За это время ты должен переключиться на окно отправки сообщения в Outlook в поле ввода получателя.")
        Otchet()
        CheckETK()
    if a == "3":
        print("Была выбрана проверка ОЭ. Программа ждёт 3 секунды после ввода ИНН. За это время ты должен переключиться на окно отправки сообщения в Outlook в поле ввода получателя.")
        a = input ("Введите ИНН: ")
        Otchet()
        CheckOE(a)
    if a == "4":
        inn = input ("Введите ИНН: ")
        Otchet()
        keyboard.write("Прошу выдать флеш-накопитель для записи ОЭ. ИНН: " + inn, input_delay)
if __name__ == "__main__":
    main()
