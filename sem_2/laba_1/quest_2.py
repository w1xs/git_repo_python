def input_data():
    n = input()
    if n.isdigit():
        return int(n)
    else:
        return None

def duo_simple(a, b : int):
    if a == b and a != 1:
        return False
    for i in range(1, min(a, b)):
        if i != 1 and a % i == 0 and b % i == 0:
            return False
    return True
def main():
    print("Введите натуральное число: ")
    user_data = input_data()
    user_data += 1
    if user_data is not None:
        matrix = [["0" for _ in range(user_data)] for __ in range(user_data)]

        for i in range(user_data):
            matrix[0][i] = str(i)
            matrix[i][0] = str(i)

        for i in range(1, user_data):
            for j in range(1, user_data):
                if duo_simple(i,j):
                    matrix[i][j] = "X"

        for i in range(user_data):
            print(matrix[i])

    else:
        print("Введены не верные данные, повторите попытку")
    return

if __name__ == "__main__":
    main()