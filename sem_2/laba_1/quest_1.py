import datetime as dt

def import_data():
    user_birth = input()
    try:
        res = dt.datetime.strptime(user_birth, "%d/%m/%y")
    except:
        return None
    return res

def main():
    print("Введите дату вашего рождения в формате d/m/y. Пример: 01/01/01")
    user_data = import_data()
    if user_data is not None:
        now = dt.datetime.now().date()
        count_days_birth = dt.datetime.toordinal(user_data)
        count_days_now = dt.datetime.toordinal(now)
        res = count_days_now - count_days_birth
        print(f"С вашего рождения прошло {res} дней")
        return
    else:
        print("Введенные данные не корректны, повторите попытку")
    return

if __name__ == "__main__":
    main()