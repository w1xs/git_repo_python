import random
import time
import keyboard


def start_of_the_game():
    print(
        "Добро пожаловать в игру! \n"
        "Правила: В начале игры мы случайным образом определим начальное количество камней в куче.\n"
        "Далее игроки будут по очереди выбирать какое количество камней они хотят убрать из кучи (1 - 3 камня).\n"
        "Победителем считается игрок, после окончания хода которого, в куче остался один камень.\n"
        "Если вы хотите сыграть, нажмите Y. Для выхода, нажмите N.")

    while True:
        if keyboard.is_pressed('Y'):
            return True
        if keyboard.is_pressed('N'):
            return False


def check_for_save_data(input_data):
    for char in input_data:
        if char not in "012345678":
            return False
        if (int(input_data) < 1) or (int(input_data) > 3):
            return False
        return True


def get_ai_step(number_of_stones):
    if number_of_stones <= 4:
        return 1, abs(1 - number_of_stones)
    ai_step = random.randint(1, 3)
    return number_of_stones - ai_step, ai_step


if start_of_the_game():

    number_of_stones = random.randint(4, 30)
    win = "undefind"

    while win == "undefind":
        print(f"\nТекущее значение камней в куче: {number_of_stones}\n")
        print("Ваш ход\n"
              "Введите число камней, которое хотите убрать из кучи (1 - 3 камня): ")

        input_data = input()

        if check_for_save_data(input_data):
            user_stone_choose = int(input_data)
            number_of_stones = number_of_stones - user_stone_choose

            if number_of_stones == 1:
                print("\nВы победили!")
                win = "User_win"
            elif number_of_stones < 1:
                print("Подумайте еще раз")
            elif number_of_stones > 1:
                print(f"\nТекущее значение камней в куче: {number_of_stones}\n")
                print("Ход другого игрока ...")

                time.sleep(2)
                number_of_stones, ai_stone_choose = get_ai_step(number_of_stones)

                if ai_stone_choose == 1:
                    print(f"Другой игрок убрал {ai_stone_choose} камень из кучи")
                else:
                    print(f"Другой игрок убрал {ai_stone_choose} камня из кучи")

                if number_of_stones == 1:
                    print(f"\nТекущее значение камней в куче: {number_of_stones}\n")
                    print("Вы проиграли. Желаем удачи в следующий раз!")
                    win = "ai_win"

        else:
            print("Неверные данные, попробуйте еще раз")
