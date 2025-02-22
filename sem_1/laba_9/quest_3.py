rus_end_dict = {"привет": "Hello",
                "как":"how",
                "твои": "yours",
                "дела":"deals",
                }

print("Введите строку для перевода на английский: ")
input_str = input()
data_for_convert = input_str.lower().strip().split(' ')
data_for_convert : list
res_str = ""

for word in data_for_convert:
    if word in rus_end_dict.keys():
        res_str += (rus_end_dict[word])
        res_str += " "
    else:
        res_str += word
        res_str += " "

print(res_str)

