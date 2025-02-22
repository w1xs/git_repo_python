def get_nice_string(string: str):
    string = string.capitalize()
    string = string[::-1]
    if string.find('!') == 0:
        string = string.replace('!', '.', 1)
    if string.find('?') == 0:
        string = string.replace('?', '.', 1)
    if string.find('...') == 0:
        string = string.replace('...', '.', 1)
    return string[::-1]


print("Введите строку для обработки: ")

input_str = input()
if input_str != '':
    ans = get_nice_string(input_str.strip())
    print(ans)
else:
    print("")
