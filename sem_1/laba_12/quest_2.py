import os

data_file_name = "quest_2_data.txt"

if data_file_name in os.listdir(os.getcwd()):

    with open(data_file_name, 'r', encoding="utf-8") as file:
        arr_of_words = []
        for line in file:
            line = line.strip()
            count_a = line.count('а')
            arr_of_words.append([line, count_a])

    arr_of_words.sort(key=lambda x: -x[1])

    for word in arr_of_words:
        print(word[0])

else:
    print("Не найден нужный файл")
