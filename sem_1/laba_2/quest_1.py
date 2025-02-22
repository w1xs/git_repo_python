def check_for_correct_input(string: str):
    for char in string:
        if char not in '0123456789':
            return False
    return True


def check_for_luck(number: str):
    first_half = number[0:3]
    second_half = number[3:]
    if sum(map(int, first_half)) == sum(map(int, second_half)):
        return True
    else:
        return False


count = 0
input_min_number = input("Введите наименьший номер билета: ")
input_max_number = input("Введите наибольший номер билета: ")

if check_for_correct_input(input_min_number) and check_for_correct_input(input_max_number):
    begin_of_finding = int(input_min_number)
    end_of_finding = int(input_max_number)
    if (0 <= begin_of_finding <= 100000) and (0 <= end_of_finding <= 100000):
        for i in range(begin_of_finding, end_of_finding + 1):
            if check_for_luck(str(i)):
                count += 1
        print(f"Счастливых билетов: {count}")
    else:
        print("Введены не шестизначные числа")
else:
    print("Введены не верные данные")
