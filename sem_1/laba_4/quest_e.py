def check_for_correct_data(number: str):
    if number.count('.') <= 1:
        for char in number:
            if char not in "0123456789":
                return False
        return True
    return False


def get_nok(number_1, number_2, rec_progress):
    if number_1 * number_2 < rec_progress:
        return number_1 * number_2
    if (rec_progress % number_1 == 0) and (rec_progress % number_2 == 0):
        return rec_progress
    return get_nok(number_1, number_2, rec_progress + 1)


input_number_1 = input("Введите первое число: ")
input_number_2 = input("Введите первое второе: ")

if check_for_correct_data(input_number_1) and check_for_correct_data(input_number_2):
    ans = get_nok(int(input_number_1), int(input_number_2), max(int(input_number_1), int(input_number_2)))
    print(f"Наименьшее общее кратное введенных чисел: {ans}")
else:
    print("Введены не верные данные")
