def check_for_correct_input(string: str):
    for char in string:
        if char not in '.-0123456789':
            return False
    return True


def get_scalar_vectors_summ(vector_1: list, vector_2: list):
    res = 0
    for i in range(len(vector_1)):
        res += vector_1[i] * vector_2[i]
    return res


first_vector = []
second_vector = []
print("Введите координаты первого вектора:")
while True:
    input_number = input()
    if input_number == '':
        break
    if check_for_correct_input(input_number):
        first_vector.append(float(input_number))
    else:
        print("Введены не верные данные, попробуйте еще раз")

print("Введите координаты второго вектора:")
while True:
    input_number = input()
    if input_number == '':
        break
    if check_for_correct_input(input_number):
        second_vector.append(float(input_number))
    else:
        print("Введены не верные данные, попробуйте еще раз\n")

if len(first_vector) == len(second_vector):
    ans = get_scalar_vectors_summ(first_vector, second_vector)
    print(ans)
else:
    print("Векторы лежат в разных системах координат")
