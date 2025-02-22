from collections import deque

print("Введите строку: ")
input_str = input()

if len(input_str) != 0:
    que_of_chars = deque()

    for char in input_str:
        que_of_chars.append(char)

    res_str = ""

    while len(que_of_chars) != 0:
        res_str += que_of_chars.pop()

    print(res_str)
else:
    print("Введена пустая строка")
