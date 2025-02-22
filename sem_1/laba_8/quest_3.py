def check_for_correct_input(string: str):
    for char in string:
        if char not in '.-0123456789':
            return False
    return True


first_amount = []
second_amount = []

print("Введите первый набор чисел: ")
while True:
    input_number = input()
    if input_number == '':
        break
    if check_for_correct_input(input_number):
        first_amount.append(float(input_number))
    else:
        print("Введены не верные данные, попробуйте еще раз")

print("Введите второй набор чисел: ")
while True:
    input_number = input()
    if input_number == '':
        break
    if check_for_correct_input(input_number):
        second_amount.append(float(input_number))
    else:
        print("Введены не верные данные, попробуйте еще раз")

first_set = set(first_amount)
second_set = set(second_amount)

ans = first_set.intersection(second_set)

print(f"Числа, которые встерчаются в обоих наборах: {ans}")
