def check_for_correct_input(string: str):
    for char in string:
        if char not in '.-0123456789':
            return False
    return True


input_x_coord = input("Введите х координату вектора: ")
input_y_coord = input("Введите y координату вектора: ")
input_z_coord = input("Введите z координату вектора: ")

if check_for_correct_input(input_x_coord) and check_for_correct_input(input_z_coord) and check_for_correct_input(
        input_z_coord):
    vector_length = (float(input_x_coord) ** 2 + float(input_y_coord) ** 2 + float(input_z_coord) ** 2) ** 0.5
    print(f"Длина заданного вектора: {vector_length}")
else:
    print("Введены неверные данные")
