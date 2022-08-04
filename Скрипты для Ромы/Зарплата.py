def main():
    print("Добро пожаловать в средство расчёта ЗП.")
    a = input("Введите количество ЕТК: ")
    b = input("Введите количество ОРД: ")
    zp_full = (int(a)*500)+(int(b)*1000)+35000
    zp_nalog = zp_full * 0.13
    zp_beznalog = zp_full * 0.87
    print(f"Полная зарплата: {zp_full} Руб.")
    print(f"Зарплата с вычитом налога: {int(zp_beznalog)} Руб.")
    print(f"Зарплата с вычитом налога и аванса: {int(zp_beznalog-10000)} Руб.")
    input()

if __name__ == "__main__":
    main()
