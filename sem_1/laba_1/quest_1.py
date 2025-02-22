input_data = input("Введите оклад сотрудника: ")
if input_data.isdigit():
    oklad = int(input_data)
    premium = (oklad * 2)/3
    member_money = oklad * 0.87
    print(f"Премия сотрудника: {premium}, сумма которую сотрудник получит на руки: {member_money}")
else:
    print("Введен не верный оклад сотрудника")