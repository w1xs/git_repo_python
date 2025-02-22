import os

data_file_name = "quest_3_data.txt"

if data_file_name in os.listdir(os.getcwd()):
    last_name_year_of_birth = ()
    data_of_line = []
    all_data = []
    with open(data_file_name, 'r', encoding='utf-8') as file:
        for line in file:
            data_of_line = line.strip().split(' ')
            last_name_year_of_birth = (data_of_line[0], data_of_line[1])
            all_data.append(last_name_year_of_birth)
    all_data.sort(key=lambda x: (x[0], x[1]))
    print(all_data)

else:
    print("Не найден нужный файл")
