import json

INPUT_FILE = "output.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    data_to_dict = []  # пустой словарь для записи
    with open(filename) as f:
        list_from_csv = f.read().split(new_line)  # разделение строк
        for line in list_from_csv:
            data_to_dict.append(line.split(delimiter))  # заполнение словаря

    return [{data_to_dict[0][i]: data_to_dict[j][i]\
             for i in range(len(data_to_dict[0]))}\
            for j in range(1, len(data_to_dict)-1)]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

with open("json_data.json", 'w') as file:
    json.dump(csv_to_list_dict(INPUT_FILE), file)
