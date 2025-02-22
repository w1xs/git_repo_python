def check_for_correct_input(string: str):
    for char in string:
        if char not in '.-0123456789':
            return False
    return True

input_first_number = input("Введите первое число: ")
input_second_number = input("Введите второе число: ")

if check_for_correct_input(input_first_number) and check_for_correct_input(input_second_number):
    if len(input_first_number) > len(input_second_number):
        print("В первом числе больше цифр")
    elif len(input_first_number) < len(input_second_number):
        print("Во втором числе больше цифр")
    elif len(input_first_number) == len(input_second_number):
        print("В числах равное количество цифр")
else:
    print("Введены не верные данные")