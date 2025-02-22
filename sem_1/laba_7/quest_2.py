def check_for_correct_input(string: str):
    for char in string:
        if char not in '.-0123456789':
            return False
    return True


def get_matrix_summ(matrix_1: list, matrix_2: list):
    res = [[0 for a in range(len(matrix_1[0]))] for b in range(max(len(matrix_1), len(matrix_2)))]
    for i in range(len(matrix_1)):
        for j in range(max(len(matrix_1[0]), len(matrix_2[0]))):
            res[i][j] = matrix_1[i][j] * matrix_2[i][j]
    return res


first_matrix = []
second_matrix = []

print("Введите строки первой матрицы, разделяйте символы пробелом")
while True:
    input_data = input()
    if input_data == '':
        break
    input_data = input_data.strip()
    input_data_mass = input_data.split(' ')
    input_is_fine = True
    for i in range(len(input_data_mass)):
        if not check_for_correct_input(input_data_mass[i]):
            input_is_fine = False
            break
    if input_is_fine:
        first_matrix.append(list(map(float, input_data_mass)))
    else:
        print("Неверные данные, попробуйте еще раз")

print("Введите строки второй матрицы, разделяйте символы пробелом")
while True:
    input_data = input()
    if input_data == '':
        break
    input_data = input_data.strip()
    input_data_mass = input_data.split(' ')
    input_is_fine = True
    for i in range(len(input_data_mass)):
        if not check_for_correct_input(input_data_mass[i]):
            input_is_fine = False
            break
    if input_is_fine:
        second_matrix.append(list(map(float, input_data_mass)))
    else:
        print("Неверные данные, попробуйте еще раз")

print(get_matrix_summ(first_matrix, second_matrix))
