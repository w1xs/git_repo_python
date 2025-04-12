import json


def main():
    count = 0
    with open(".\\animals.json", "r") as file:
        data = json.load(file)
    print("Информация о птицах: ")
    for animal in data["animals"]:
        if animal["animal_type"] == "Bird":
            for key in animal.keys():
                if key != "id" and key != "image_link":
                    print(f"{key}: {animal[key]}")
            print()
        if animal["active_time"] == "Diurnal":
            count += 1
    min_weight_animal_data = min(data["animals"], key=lambda x: float(x["weight_min"]))
    min_weight_animal = min_weight_animal_data["name"]
    print(f"Число дневных животных: {count}")
    print(f"Животное с наименьшим весом: {min_weight_animal}")


if __name__ == "__main__":
    main()
