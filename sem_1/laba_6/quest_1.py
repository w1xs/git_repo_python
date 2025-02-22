# для построения реугярных выражений, используй https://regex101.com/
import re


def check_for_correct_input(string: str):
    if len(string) > 3:
        return True
    return False


def check_for_filenames(string: str):
    if string.count('.') == 1 and len(re.findall("[\\!?/|*<>=]", string)) == 0:
        if string[-4:] in ['.txt', '.doc', '.docx', '.odt', '.rtf']:
            return True
        return False
    return False


print("Введие строки для анализа по одной.\nПосле ввода всех строк, нажмите N + ENTER для получаения результата:")

nice_str = []
wrong_str = []
working = True

while working:
    input_str = input()
    if input_str == 'N' or input_str == 'n':
        working = False
    else:
        if check_for_correct_input(input_str) and check_for_filenames(input_str):
            nice_str.append(input_str)
        else:
            wrong_str.append(input_str)

print(f"Именами файлов являются: {nice_str}")
print(f"Именами файлов не являются: {wrong_str}")
