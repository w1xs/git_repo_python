import os


def check_for_correct_input(number: str):
    if number.count('.') <= 1:
        for char in number:
            if char not in "0123456789":
                return False
        return True
    return False


def add_sentences_to_file(file_name: str, arr_for_write: []):
    with open(file_name, 'a') as f:
        str_for_write = ''
        for i in range(len(arr_for_write)):
            str_for_write += str(arr_for_write[i])
            str_for_write += " "
        str_for_write += '\n'
        f.write(str_for_write)


data_file_name = 'quest_2_data.txt'
res_file_name = 'quest_2_res.txt'

if data_file_name in os.listdir(os.getcwd()):
    words_from_all_sentence = []

    print("Введите нужное колличество слов в предложении: ")
    input_str = input()
    if check_for_correct_input(input_str):
        with open(data_file_name) as file:
            string = file.readline()
            all_sentences = string.strip().replace('!', '.').replace('?', '.').split('.')
            for sentence in all_sentences:
                arr_of_words = sentence.strip().split(' ')
                words_from_all_sentence.append(arr_of_words)

        for sentence in words_from_all_sentence:
            if len(sentence) == int(input_str):
                add_sentences_to_file(res_file_name, sentence)
    else:
        print("Введено не верное колличество слов")
else:
    print("Нужный файл не найден")
