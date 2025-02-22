def check_for_correct_input(string: str):
    for char in string:
        if char not in '.-0123456789':
            return False
    return True
input_data = input("Введите число, для которого нужно найти факториал: ")

output = 1

if check_for_correct_input(input_data):
    number_of_factorial = int(input_data)
    if number_of_factorial != 0:
        for i in range(1,number_of_factorial+1):
            output *= i
        print(f"искомый факториал: {output}")
    else:
        print("искомый факториал: 1")
else:
    print("Введены не верные данные")