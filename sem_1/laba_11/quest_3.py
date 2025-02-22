import random
import os


def check_for_correct_input(number: str):
    if number.count('.') <= 1:
        for char in number:
            if char not in "0123456789":
                return False
        return True
    return False


def get_n_sentence_from_file(file_name: str, n: int):
    all_phrases = []
    with open(file_name) as file:
        for line in file:
            phrases_in_line = line.strip().split("; ")
            all_phrases.append(phrases_in_line)

    res_sentences = [[] for k in range(0, n)]
    i = 0

    while i < n:
        for j in range(len(all_phrases)):
            phrase_number = random.randint(0, len(all_phrases[j]) - 1)
            res_sentences[i].append(all_phrases[j][phrase_number])
        i += 1

    return res_sentences


def write_sentences_to_file(file_name: str, arr_for_write: []):
    with open(file_name, 'w') as f:
        str_for_write = ''
        for i in range(len(arr_for_write)):
            str_for_write += str(arr_for_write[i])
            str_for_write = str_for_write.replace('[', '').replace(']', '').replace(', ', ' ')
            str_for_write = str_for_write.replace("\'", '')
            str_for_write += '\n'
        f.write(str_for_write)


def add_sentences_to_file(file_name: str, arr_for_write: []):
    with open(file_name, 'a') as f:
        str_for_write = ''
        for i in range(len(arr_for_write)):
            str_for_write += str(arr_for_write[i])
            str_for_write = str_for_write.replace('[', '').replace(']', '').replace(', ', ' ')
            str_for_write = str_for_write.replace("\'", '')
            str_for_write += '\n'
        f.write(str_for_write)


data_file_name = "quest_3_data.txt"
res_file_name = "quest_3_res.txt"

if data_file_name in os.listdir(os.getcwd()):
    print("Введите число предложений, которые нужно сгенерировать: ")
    input_str = input()
    if check_for_correct_input(input_str):
        arr_of_sentences = get_n_sentence_from_file(data_file_name, int(input_str))
        write_sentences_to_file(res_file_name, arr_of_sentences)

        print("Желаете добавить еще предложений?")
        input_answer = input()
        if input_answer == "Да":
            print("Введите число предложений, которые нужно сгенерировать: ")
            input_str = input()
            if check_for_correct_input(input_str):
                arr_of_sentences = get_n_sentence_from_file(data_file_name, int(input_str))
                add_sentences_to_file(res_file_name, arr_of_sentences)
            else:
                print("Неверное колличество предлжений")
    else:
        print("Неверное колличество предложений")
else:
    print("Нужный файл не найден")
