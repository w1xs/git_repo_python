print("Введите первую строку: ")
first_str = input()
print("Введите вторую строку: ")
second_str = input()

set_of_f_str = set(first_str)
set_of_s_str = set(second_str)

ans = set_of_f_str.difference(set_of_s_str)
ans = list(ans)
print(f"Символы, которых нет во второй строке, но есть первой строке {ans}")
