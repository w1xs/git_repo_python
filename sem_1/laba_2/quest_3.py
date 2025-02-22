def check_for_correct_input(string: str):
    for char in string:
        if char not in '.-0123456789':
            return False
    return True

def get_sum_of_cifr(number):
    if number < 0:
        number = number * -1
    sum_cifr_of_number = 0
    while number > 0:
        sum_cifr_of_number += number % 10
        number = number // 10
    return sum_cifr_of_number

input_data = input("Введите необходимую сумму цифр: ")
count = 0

if check_for_correct_input(input_data):
    necessary_sum = int(input_data)
    if necessary_sum >= 0:
        for i in range(-999,-99):
            if get_sum_of_cifr(i) == necessary_sum:
                print(i)
        for i in range(100,1000):
            if get_sum_of_cifr(i) == necessary_sum:
                print(i)
    else:
        print("Введено отрицательное число")
else:
    print("Введены не верные данные")