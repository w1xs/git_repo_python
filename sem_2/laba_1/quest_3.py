def input_data(path: str):
    data = []
    element = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            element = line.strip().split()
            if element[1].isdigit():
                element[1] = int(element[1])
            else:
                return None
            data.append(element)
    return data


def main():
    print("Введите полный путь к файлу: ")
    path = input()
    data = input_data(path)
    if data is not None:
        print(sorted(data, key=lambda x: x[0]))
        print(sorted(data, key=lambda x: x[1]))
        print("Введите минимально количество баллов: ")
        n = input()
        if n.isdigit():
            with open("quest_3_res.txt", "w", encoding='utf-8') as res:
                for i in range(len(data)):
                    if data[i][1] >= int(n):
                        res.write(data[i][0])
                        res.write("\n")
        else:
            print("Введены не верные данные, повторите попытку")
    else:
        print("Введены не верные данные, повторите попытку")
    return


if __name__ == "__main__":
    main()
