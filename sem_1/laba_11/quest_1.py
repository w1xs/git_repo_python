import os


def check_for_correct_input(number: str):
    if number.count('.') <= 1:
        for char in number:
            if char not in "0123456789":
                return False
        return True
    return False


def get_my_list_cut(array: list, numbers_for_delete: int):
    array = array[:(len(array) - numbers_for_delete)]
    res_file_name = "quest_1_res.txt"
    with open(res_file_name, "w") as f:
        f.write(str(array))
    return res_file_name


print("Введите название файла для чтения: ")
file_name = input()
print("Введите сколько значений нужно убрать?")
numbers_to_delete = input()

if file_name in os.listdir(os.getcwd()):

    with open(file_name) as file:
        line = file.readline().replace('(', '').replace(')', '').replace(',', '')
        arr_of_number = line.split(" ")

        if check_for_correct_input(numbers_to_delete) and len(arr_of_number) >= int(numbers_to_delete):
            print(f"Данные сохранены в {get_my_list_cut(arr_of_number, int(numbers_to_delete))}")
        else:
            print("Введены не верные данные, попробуйте еще раз")

else:
    print("Указанный вами файл не существует")
