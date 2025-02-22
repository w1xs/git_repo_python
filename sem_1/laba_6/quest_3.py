string_1 = input("Введите первую строку: ")
string_2 = input("Введите вторую строку: ")

number_of_inv = string_1.find(string_2)
if number_of_inv != 0:
    string_1 = string_1.replace(string_2, '', number_of_inv - 1)
    print(string_1)
else:
    print("Вторая строка не встречается в перой ни разу")
