def check_for_correct_input(number: str):
    for char in number:
        if char not in "0123456789":
            return False
    return True


def find_nod(number_1, number_2: int):
    for i in range(min(number_1, number_2), 1, -1):
        if (number_1 % i == 0) and (number_2 % i == 0):
            return i
    return 1


input_num_1 = input("Введите первое натуральное число: ")
input_num_2 = input("Введите второе натуральное число: ")

if check_for_correct_input(input_num_1) and check_for_correct_input(input_num_2):
    ans = find_nod(int(input_num_1), int(input_num_2))
    print(f"Наибольший общий делитель двух чисел: {ans}")
else:
    print("Введены неверные данные")
