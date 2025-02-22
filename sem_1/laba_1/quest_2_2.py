input_pervoe = input("Введите певое число: ")
input_vtoroe_ = input("Введите второе число: ")

if input_pervoe.isdigit() and input_vtoroe_.isdigit():
    pervoe = int(input_pervoe)
    vtoroe = int(input_vtoroe_)
    pervoe = pervoe + vtoroe
    vtoroe = pervoe - vtoroe
    pervoe = pervoe - vtoroe
    print(f"Первое число: {pervoe}, Второе числo: {vtoroe}")
else:
    print("Введены не верные данные")