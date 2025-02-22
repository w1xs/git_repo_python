import random


def get_bulb_sort(arr: list):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                buff = arr[j]
                arr[j] = arr[i]
                arr[i] = buff
    return arr


data_for_sort = []

for i in range(0, 5000):
    data_for_sort.append(random.randint(-300, 300))

print(data_for_sort)
sorted_data = get_bulb_sort(data_for_sort)
print(sorted_data)
