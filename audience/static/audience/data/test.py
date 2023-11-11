import csv

with open('players.csv', 'r' ,encoding='utf-8') as file:
    _list = []
    rows = csv.DictReader(file)
    for r in rows:
        # print(r)
        _list.append(r)

print(_list)