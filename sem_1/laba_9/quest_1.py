name_score_dict = {"Иванов": 20, "Сидоров": 68, "Петров": 26, "Смирнов": 68}
name_score_dict["Сидоров"] = 52
name_score_dict["Михайлов"] = 100

sum_score = 0
max_score = -1
min_score = name_score_dict["Иванов"]
middle_score = 0
people_with_big_score = {}
people_with_low_score = {}
people_with_middle_score = []
res_with_highest_scores = {}
res_with_lowest_scores = {}

for key in name_score_dict.keys():
    sum_score += name_score_dict[key]
    if name_score_dict[key] >= max_score:
        people_with_big_score[key] = name_score_dict[key]
        max_score = name_score_dict[key]

    if name_score_dict[key] <= min_score:
        people_with_low_score[key] = name_score_dict[key]
        min_score = name_score_dict[key]

middle_score = sum_score / len(name_score_dict.keys())

for key in name_score_dict.keys():
    if name_score_dict[key] > middle_score:
        people_with_middle_score.append(key)

for key in people_with_big_score.keys():
    if people_with_big_score[key] == max_score:
        res_with_highest_scores[key] = people_with_big_score[key]

for key in people_with_low_score.keys():
    if people_with_low_score[key] == min_score:
        res_with_lowest_scores[key] = people_with_low_score[key]

print(f"Участники баллы, которых выше среднего: {people_with_middle_score}")
print(f"Участники с макисмальными баллами: {res_with_highest_scores}")
print(f"Участники с минимальными баллами: {res_with_lowest_scores}")
print(f"Средний балл участников: {middle_score}")


