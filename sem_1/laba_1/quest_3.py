input_first_side_length = input("Ввелите первую сторону треугольника: ")
input_second_side_length = input("Ввелите вторую сторону треугольника: ")
input_third_side_length = input("Ввелите третью сторону треугольника: ")


if input_first_side_length.isdigit() and input_second_side_length.isdigit() and input_third_side_length.isdigit():
    biggest_side = max(int(input_first_side_length), int(input_second_side_length), int(input_third_side_length))
    sum_of_other_sides = int(input_first_side_length) + int(input_second_side_length) + int(input_third_side_length) - biggest_side
    if biggest_side < sum_of_other_sides:
        square_biggest_side = biggest_side**2
        sum_of_squares_of_other_sides = int(input_first_side_length) ** 2 + int(input_second_side_length) ** 2 + int(input_third_side_length) ** 2 - square_biggest_side
        if square_biggest_side == sum_of_squares_of_other_sides:
            print("Треугольник прямоугольный")
        elif square_biggest_side > sum_of_squares_of_other_sides:
            print("Треугольник тупоугольный")
        elif square_biggest_side < sum_of_squares_of_other_sides:
            print("Треугольник остроугольный")
    else:
        print("Такого треугольника не существует")
else:
    print("Введены не верные данные")