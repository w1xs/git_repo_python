pervoe = input("Введите певое число: ")
vtoroe = input("Введите второе число: ")

if pervoe.isdigit() and vtoroe.isdigit():
    buffer = vtoroe
    vtoroe = pervoe
    pervoe = buffer
    print(f"Первое число: {pervoe}, Второе числo: {vtoroe}")
else:
    print("Введены не верные данные")