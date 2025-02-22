import os

data_file_name = "quest_4_data.txt"
res_file_name = "quest_4_res.txt"

if data_file_name in os.listdir(os.getcwd()):
    absorb_chapters = []

    with open(data_file_name, 'r', encoding='utf-8') as file:
        all_text = file.read()

    devided_text = all_text.split("\n")

    for i in range(len(devided_text) - 1):
        if "Глава" in devided_text[i] or "Chapter" in devided_text[i]:
            absorb_chapters.append([devided_text[i], devided_text[i + 1]])

    with open(res_file_name, 'w', encoding='utf-8') as f:
        f.write("Оглавление\n")
        for chapter in absorb_chapters:
            str_for_write = ''
            str_for_write += chapter[0] + ' : ' + chapter[1]
            str_for_write += '\n'
            f.write(str_for_write)

else:
    print("Нужный файл не найден")
