from collections import deque


def check_poli(str: str):
    arr_of_words = []
    first_half = deque()
    for char in input_str:
        arr_of_words.append(char)

    if len(arr_of_words) % 2 == 0:
        point_of_break = 0
        for i in range(len(arr_of_words) // 2):
            first_half.append(arr_of_words[i])
            point_of_break += 1
        arr_of_words = arr_of_words[point_of_break:]

        for word in arr_of_words:
            if first_half.pop() != word:
                return False

        return True

    else:
        point_of_break = 0
        for i in range(len(arr_of_words) // 2):
            first_half.append(arr_of_words[i])
            point_of_break += 1
        arr_of_words = arr_of_words[point_of_break + 1:]

        for word in arr_of_words:
            if first_half.pop() != word:
                return False

        return True


print("Введите слово: ")
input_str = input()

if len(input_str) == 0:
    print("Вы не ввели слово, перезапустите программу")
else:
    if check_poli(input_str):
        print("Слово ялвяется полиндромом")
    else:
        print("Слово не является полиндромом")
