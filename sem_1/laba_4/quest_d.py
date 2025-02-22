def check_for_correct_data(number: str):
    if number.count('.') <= 1:
        for char in number:
            if char not in "0123456789":
                return False
        return True
    return False


def get_bin_from_dec(number, bin):
    if number == 0:
        return bin
    else:
        return get_bin_from_dec(number // 2, bin + str(number % 2))


input_number = input("Введите число для перевода в двоичную систему счисления: ")

if check_for_correct_data(input_number):
    if int(input_number) == 0:
        print("Двоичное представление введенного числа: 0")
    else:
        ans = get_bin_from_dec(int(input_number), '')
        ans = ans[::-1]
        print(f"Двоичное представление введенного числа: {ans}")
else:
    print("Введены не верные данные")
