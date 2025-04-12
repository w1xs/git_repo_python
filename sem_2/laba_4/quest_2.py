import json
from docxtpl import DocxTemplate
import csv

def main():
    doc = DocxTemplate("template.docx")
    with open(".\\data_marathon.csv", "r") as file:
        row_data = list(csv.DictReader(file))

    print(row_data)

    data = {}

    for item in row_data:
        if item["year"] not in data.keys():
            data[item["year"]] = {}
        if item["marathon_city"] not in data[item["year"]].keys():
            data[item["year"]][item["marathon_city"]] = []

        buffer = {
            "name":item["name"],
            "sex":item["sex"],
            "time":item["time"],
        }
        data[item["year"]][item["marathon_city"]].append(buffer)

    print(json.dumps(data, indent=4))

    context = {
        "data": data
    }

    doc.render(context)
    doc.save("result.docx")

if __name__ == "__main__":
    main()