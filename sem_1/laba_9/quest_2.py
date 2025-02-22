author_books_dict = {"Александр Пушкин":["Капитанская Дочка", "Евгений Онегин"],
                     "Стивен Кинг":["Кладбище домашних животных", "ОНО"],
                     "Джон Толкиен":["Хоббит", "Властелин Колец"],
                     "Анджей Сапковский":["Ведьмак"]}

while True:
    print("Введите имя и фамилию автора: ")
    author = input()
    if author == '':
        break
    print("Введите произведение этого автора: ")
    book = input()
    if book == '':
        print("Ошибка ввода данных, попробуйте еще раз")
    else:
        if author in author_books_dict.keys():
            book = input()
            author_books_dict[author].append(book)
        else:
            author_books_dict[author] = [book]

while True:
    print("Введите фамилию автора, для просмотра его произведений: ")
    input_name = input()
    if input_name == '':
        break
    if input_name in author_books_dict.keys():
        print(author_books_dict[input_name])
    else:
        print("Такого автора нет в списке, попробуйте другого")

