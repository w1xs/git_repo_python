def check_for_correct_data(number: str):
    if number.count('.') <= 1:
        for char in number:
            if char not in ".-0123456789":
                return False
        return True
    return False


def get_n_member_of_alg_prog(number, additer, member_count):
    if member_count <= 0:
        return number
    if member_count > 0:
        return get_n_member_of_alg_prog(number + additer, additer, member_count - 1)


input_base_of_prog = input("Введите нулевой элемент: ")
input_multiplier = input("Введите множитель прогрессии: ")
input_count = input("Введите номер нужного элемента: ")

if check_for_correct_data(input_base_of_prog) and check_for_correct_data(input_multiplier) and input_count.isdigit():
    ans = get_n_member_of_alg_prog(float(input_base_of_prog), float(input_multiplier), int(input_count))
    print(f"Значение введенного члена прогрессии: {ans}")
else:
    print("Введены не верные данные")
