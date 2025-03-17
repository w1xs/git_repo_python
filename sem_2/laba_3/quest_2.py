import csv


def check_for_correct(number: str):
    for ch in number:
        if ch not in ".0123456789":
            return None
    return float(number)


def main():
    print("Введите нижнюю границу дохода:")
    low_income = input()
    low_income = check_for_correct(low_income)
    if low_income is None:
        print("Введены не верные данные")
        return

    print("Введите верхнюю границу дохода:")
    high_income = input()
    high_income = check_for_correct(high_income)
    if high_income is None:
        print("Введены не верные данные")
        return

    with open(".\\countries.csv", "r") as file:
        data = list(csv.DictReader(file))
    first_res = []
    second_res = []
    for item in data:
        if float(item["Income"]) >= low_income and float(item["Income"]) <= high_income and low_income <= high_income:
            first_res.append(item)
    second_res = sorted(data, key=lambda x: float(x["Inflation"]))

    with open('res_a.csv', mode='w', newline='') as file:
        fieldnames = ['Country', 'Health Care', 'Income', 'Inflation', 'Life Expectancy']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(first_res)

    with open('res_b.csv', mode='w', newline='') as file:
        fieldnames = ['Country', 'Health Care', 'Income', 'Inflation', 'Life Expectancy']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(second_res)


if __name__ == "__main__":
    main()
