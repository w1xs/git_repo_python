import os


def get_file_names(root_path, tag):
    result = []
    empty = True
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith(tag):
                result.append(os.path.join(root, file))
                empty = False
    if empty:
        return None
    else:
        return result


def main():
    print("Введите полный путь до директории: ")
    directory_path = input()
    if not os.path.exists(directory_path):
        print("Такого пути не существует, попробуйте еще раз")
        return
    if not os.path.isdir(directory_path):
        print("Не сущестует папки с таким путем")
        return

    print("Введите расширение в формате *.расширение*")
    tag = input()
    if tag.count(".") != 1:
        print("Неверное расширение")
        return

    file_names = get_file_names(directory_path, tag)
    if file_names:
        for file in file_names:
            print(file)
    else:
        print("Не найдено файлов с таким расширением")
        return


if __name__ == "__main__":
    main()
