def check_for_correct_data(number: str):
    if number.count('.') <= 1:
        for char in number:
            if char not in ".-0123456789":
                return False
        return True
    return False


def get_sum_of_geom_prog(number, multiplier, member_count, sum_of_prog):
    if member_count <= 0:
        return sum_of_prog
    if member_count > 0:
        return get_sum_of_geom_prog(number * multiplier, multiplier, member_count - 1,
                                    sum_of_prog + number * multiplier)


input_base_of_prog = input("Введите нулевой элемент: ")
input_multiplier = input("Введите множитель прогрессии: ")
input_count = input("Введите номер нужного элемента: ")

if check_for_correct_data(input_base_of_prog) and check_for_correct_data(input_multiplier) and input_count.isdigit():
    ans = get_sum_of_geom_prog(float(input_base_of_prog), float(input_multiplier), int(input_count), 0)
    print(f"Сумма членов прогрессии: {ans}")
else:
    print("Введены не верные данные")
