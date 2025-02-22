def check_for_correct_input(string: str):
    for char in string:
        if char not in '-0123456789':
            return False
    return True


def get_moda_of_mass(dictionary: dict):
    res = -1
    biggest_number = -1
    for key in dictionary.keys():
        if dictionary[key] > biggest_number:
            res = key
            biggest_number = dictionary[key]

    for key in dictionary.keys():
        if (dictionary[key] == biggest_number) and (key != res):
            return -1

    return res


print("Введите массив для поиска моды")
list_for_work = []
simbols_number = {}

while True:
    input_data = input()
    if input_data == '':
        break
    if check_for_correct_input(input_data):
        list_for_work.append(int(input_data))
    else:
        print("Неверные данные, попробуйте еще раз")

for i in range(len(list_for_work)):
    if list_for_work[i] in simbols_number.keys():
        simbols_number[list_for_work[i]] += 1
    else:
        simbols_number[list_for_work[i]] = 1

ans = get_moda_of_mass(simbols_number)

if ans == -1:
    print("Массив не имеет моды")
else:
    print(f"Мода массива: {ans}")
