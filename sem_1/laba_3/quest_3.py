from datetime import datetime

print("Введите дату и время отправления в соответствии с образцом: Month/Day/Year Hour:Minute ")
input_start_datetime = input()
print("Введите дату и время прибытия в соответствии с образцом: Month/Day/Year Hour:Minute")
input_finish_datetime = input()

try:
    datetime_of_start = datetime.strptime(input_start_datetime, '%m/%d/%Y %H:%M')
    datetime_of_finish = datetime.strptime(input_finish_datetime, '%m/%d/%Y %H:%M')
    time_in_way = datetime_of_finish - datetime_of_start
    print(f"Время в пути составит: {time_in_way}")
except:
    print("Введены не верные данные")


# ds1 = 'Friday, November 17, 2020'
# ds2 = '11/17/20'
# ds3 = '11-17-2020'
#
# # Конвертируем строки в объекты datetime и сохраним
# dt1 = datetime.strptime(ds1, '%A, %B %d, %Y')
# dt2 = datetime.strptime(ds2, '%m/%d/%y')
# dt3 = datetime.strptime(ds3, '%m-%d-%Y')
#
# print(dt1)
# print(dt2)
# print(dt3)



# def check_for_correct_input(number: str):
#     if (number.count('.') <= 2) and (number.count(':') <= 1):
#         for char in number:
#             if char not in ".:0123456789":
#                 return False
#         return True
#     return False
#
#
# def check_for_correct_date(date_of_start, date_of_finish, time_of_start, time_of_finish: str):
#     year_of_start = int(date_of_start[:4])
#     month_of_start = int(date_of_start[5:7])
#     day_of_start = int(date_of_start[8:])
#     hour_of_start = int(time_of_start[:2])
#     minute_of_start = int(time_of_start[3:])
#
#     year_of_finish = int(date_of_finish[:4])
#     month_of_finish = int(date_of_finish[5:7])
#     day_of_finish = int(date_of_finish[8:])
#     hour_of_finish = int(time_of_finish[:2])
#     minute_of_finish = int(time_of_finish[3:])
#
#     if (12 < month_of_start) or (12 < month_of_finish):
#         return False
#
#     if (31 < day_of_start) or (31 < day_of_finish):
#         return False
#
#     if (24 < hour_of_start) or (24 < hour_of_finish):
#         return False
#
#     if (60 < minute_of_start) or (60 < minute_of_finish):
#         return False
#
#     if year_of_finish < year_of_start:
#         return False
#
#     return True
#
#
# print("Введите дату отправления в соотетствии с образцом")
# input_date_of_start = input("YYYY.MM.DD ")
# print("Введите время отправления в соответствии с образцом")
# input_time_of_start = input("HH:MM ")
# print("Введите дату прибытия в соответствии с образцом")
# input_date_of_finish = input("YYYY.MM.DD ")
# print("Введите время прибытия в соответствии с образцом")
# input_time_of_finish = input("HH:MM ")
#
# if check_for_correct_input(input_date_of_start) and check_for_correct_input(
#         input_time_of_start) and check_for_correct_input(input_date_of_finish) and check_for_correct_input(
#     input_time_of_finish):
#     if check_for_correct_date(input_date_of_start, input_date_of_finish, input_time_of_start, input_time_of_finish):
#         year_of_start = int(input_date_of_start[:4])
#         month_of_start = int(input_date_of_start[5:7])
#         day_of_start = int(input_date_of_start[8:])
#         hour_of_start = int(input_time_of_start[:2])
#         minute_of_start = int(input_time_of_start[3:])
#
#         year_of_finish = int(input_date_of_finish[:4])
#         month_of_finish = int(input_date_of_finish[5:7])
#         day_of_finish = int(input_date_of_finish[8:])
#         hour_of_finish = int(input_time_of_finish[:2])
#         minute_of_finish = int(input_time_of_finish[3:])
#
#         time_in_move_sec = (year_of_finish * 63261216000 + month_of_finish * 2592000 +
#                             day_of_finish * 86400 + hour_of_finish * 3600 + minute_of_finish * 60) - (
#                                    year_of_start * 63261216000 + month_of_start * 2592000 +
#                                    day_of_start * 86400 + hour_of_start * 3600 + minute_of_start * 60)
#
#         day_in_move = time_in_move_sec // 3600 // 24
#         time_in_move_sec = time_in_move_sec - day_in_move * 3600 * 24
#         hour_in_move = time_in_move_sec // 3600
#         time_in_move_sec = (time_in_move_sec - hour_in_move * 3600)
#         minute_in_move = time_in_move_sec // 60
#
#         print(f"Время в пути составит: {day_in_move} д. {hour_in_move} ч. {minute_in_move} м.")
#     else:
#         print("Введена неверная дата или неверное время")
# else:
#     print("Введены не верные данные")
#
# print("Введите дату рождения в соответствии с образцом")
# date_of_birth = input("YYYY.MM.DD ")
