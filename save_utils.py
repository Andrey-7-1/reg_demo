import csv
import json


def save_to_csv(filename, data):
    """
    Save data to a csv file.
    Append at the end of the file
    """
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(data)


def update_orgs(filename, full, short):
    data = json.load(open(filename))

    new_short = set(data['5']['short'])
    new_short.add(short.strip())

    new_full = set(data['5']['full'])
    new_full.add(full.strip())

    data['5'] = {"short": list(new_short), "full": list(new_full)}

    # Save dict to json
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def update_division_type_name(filename, dt):
    data = json.load(open(filename))

    new_dt = set(data['10'])
    new_dt.add(dt.strip())
    data['10'] = list(new_dt)

    # Save dict to json
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
