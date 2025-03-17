def get_data(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            row_data = file.read().strip().split()
            return row_data
    except:
        return None


def main():
    element = []
    result = []
    print("Введите путь к файлу: ")
    path = input()
    row_data = get_data(path)
    if row_data is not None:
        print("Введите натуральное число: ")
        n = input()
        if n.isdigit():
            n = int(n)
            if n > len(row_data):
                print(" ".join(row_data))
            else:
                for i in range(len(row_data) - n + 1):
                    for j in range(i, i + n):
                        element.append(row_data[j])
                    result.append(" ".join(element))
                    element = []
                print(", ".join(result))
        else:
            print("Введены не верные данные, повторите попытку")
    else:
        print("Введены не верные данные, повторите попытку")
    return


if __name__ == "__main__":
    main()
