import datetime

print("Введите вашу дату рождения в соответствии с образцом: Month/Day/Year ")
input_date = input()

try:
    date_of_birth = datetime.datetime.strptime(input_date, "%m/%d/%Y")
    date_after_10th_days = date_of_birth + datetime.timedelta(days=10 ** 4)
    date_after_1mill_min = date_of_birth + datetime.timedelta(minutes=10 ** 6)
    date_after_1bill_sec = date_of_birth + datetime.timedelta(seconds=10 ** 9)
    print(f"10 тысяч дней вам исполнится {date_after_10th_days}")
    print(f"1 миллион минут вам исполнится {date_after_1mill_min}")
    print(f"1 миллиард секунд вам исполнится {date_after_1bill_sec}")
except:
    print("Введена не верная дата")

# def check_for_correct_input(number: str):
#     if number.count('.') <= 2:
#         for char in number:
#             if char not in ".0123456789":
#                 return False
#         return True
#     return False
#
#
# def check_for_correct_date(month, day: int):
#     if 13 < month:
#         return False
#     if 31 < day:
#         return False
#     return True
#
#
# def get_life_after_10thousand_day(year, month, day: int):
#     lifetime = year * 365 + month * 30 + day
#     new_life = lifetime + 10000
#     out_year = new_life // 365
#     new_life = new_life - out_year * 365
#     out_month = new_life // 30
#     new_life = new_life - out_month * 30
#     out_day = new_life
#     resp = f"{out_year}.{out_month}.{out_day}"
#     return resp
#
#
# def get_life_after_1mill_min(year, month, day: int):
#     lifetime = year * 365 * 24 * 60 + month * 30 * 24 * 60 + day * 24 * 60
#     new_life = lifetime + 10 ** 6
#     out_year = new_life // 365 // 24 // 60
#     new_life = new_life - out_year * 365 * 24 * 60
#     out_month = new_life // 30 // 24 // 60
#     new_life = new_life - out_month * 30 * 24 * 60
#     out_day = new_life // 24 // 60
#     resp = f"{out_year}.{out_month}.{out_day}"
#     return resp
#
#
# def get_life_after_1bill_sec(year, month, day: int):
#     lifetime = year * 365 * 24 * 3600 + month * 30 * 24 * 3600 + day * 24 * 3600
#     new_life = lifetime + 10 ** 9
#     out_year = new_life // 365 // 24 // 3600
#     new_life = new_life - out_year * 365 * 24 * 3600
#     out_month = new_life // 30 // 24 // 3600
#     new_life = new_life - out_month * 30 * 24 * 3600
#     out_day = new_life // 24 // 3600
#     resp = f"{out_year}.{out_month}.{out_day}"
#     return resp
#
#
# print("Введите дату рождения в соответствии с образцом")
# date_of_birth = input("YYYY.MM.DD ")
#
# year = int(date_of_birth[:4])
# month = int(date_of_birth[5:7])
# day = int(date_of_birth[8:])
#
# if check_for_correct_input(date_of_birth):
#     if check_for_correct_date(month, day):
#         print(f"10 тысяч дней вам исполнится в  {get_life_after_10thousand_day(year, month, day)}")
#         print(f"1 миллион минут вам исполнится в  {get_life_after_1mill_min(year, month, day)}")
#         print(f"1 миллиард секунд вам исполнится в {get_life_after_1bill_sec(year, month, day)}")
#     else:
#         print("Введена не верная дата рождения")
# else:
#     print("Введены не верные данные")
