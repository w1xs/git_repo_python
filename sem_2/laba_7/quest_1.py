import pandas as pd


def load_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")
        return None


def task_a(df):
    print("5 самых высоких зданий:")
    print(df.nlargest(5, 'height_m')[['name', 'height_m']])

    print("5 самых низких зданий:")
    print(df.nsmallest(5, 'height_m')[['name', 'height_m']])


def task_b(df):
    print("Статистика высот зданий:")
    stats = df['height_m'].agg(['min', 'max', 'mean', 'median'])
    print(stats)


def task_c(df):
    countries = df['country'].nunique()
    print(f"Количество стран в файле: {countries}")


def task_d(df):
    oldest = df[df['year_built'] == df['year_built'].min()]
    newest = df[df['year_built'] == df['year_built'].max()]

    print("Самое старое здание:")
    print(oldest[['name', 'year_built']])

    print("Самые новые зднания:")
    print(newest[['name', 'year_built']])


def task_e(df):
    try:
        min_floors = int(input("Введите минимальное суммарное количество этажей: "))
        total_floors = df['floors_above'] + df['floors_below_ground']
        filtered = df[total_floors > min_floors]
        print(f"Здания с общим числом этажей > {min_floors}:")
        print(filtered[['name', 'floors_above', 'floors_below_ground']])
    except ValueError:
        print("Ошибка: введите целое число!")


def task_f(df):
    try:
        year = int(input("Введите год постройки для поиска: "))
        buildings = df[df['year_built'] == year]
        if buildings.empty:
            print(f"Зданий, построенных в {year} году, не найдено.")
        else:
            print(f"Здания, построенные в {year} году:")
            print(buildings['name'])
    except ValueError:
        print("Ошибка: введите корректный год!")


def task_g(df):
    country = input("Введите название страны: ").strip()
    count = df[df['country'].str.lower() == country.lower()].shape[0]
    print(f"Количество зданий в {country}: {count}")


def main():
    df = load_data('data_tallest_buildings.csv')
    if df is None:
        return

    task_a(df)
    print()
    task_b(df)
    print()
    task_c(df)
    print()
    task_d(df)
    print()

    while True:
        try:
            print("Выберите задачу для выполнения:")
            print("e - Здания с суммарным количеством этажей больше заданного")
            print("f - Здания по году постройки")
            print("g - Количество зданий по стране")
            print("q - Выход")

            choice = input("Ваш выбор: ").lower()

            if choice == 'e':
                task_e(df)
            elif choice == 'f':
                task_f(df)
            elif choice == 'g':
                task_g(df)
            elif choice == 'q':
                break
            else:
                print("Неверный выбор! Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()