import math


def check_for_correct_input(number: str):
    if number.count('.') <= 1:
        for char in number:
            if char not in ".-0123456789":
                return False
        return True
    return False


input_data = input("Введите градусную меру угла: ")

if check_for_correct_input(input_data):
    sin = math.sin(math.radians(float(input_data)))
    cos = math.cos(math.radians(float(input_data)))
    tan = math.tan(math.radians(float(input_data)))
    print(f"синус: {sin}, косинус: {cos}, тангенс: {tan}")
else:
    print("Введите корректные данные")
