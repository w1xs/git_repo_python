# для построения реугярных выражений, используй https://regex101.com/
import re


def check_for_auto_number(string: str):
    if len(string) == 6 and string.isalnum():
        if len(re.findall('[a-zA-Z]{2}[0-9]{3}[a-zA-Z]{1}', string)) == 1:
            return True
    return False


input_str = input("Введите предположительный номер автомобиля: ")

if check_for_auto_number(input_str):
    print("Может являться номером автомобиля")
else:
    print("Не может являться номером автомобиля")
