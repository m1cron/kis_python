def f23(table):
    res = []
    for sublist in table:
        cleaned = [elem for elem in sublist if elem is not None]
        if len(cleaned):
            res.append(cleaned)
    for row in res:
        row[1] = "{:.0f}%".format(float(row[1]) * 100)
        tmp = row[0].split("|")
        row[0] = "{}.".format(tmp[1].replace(',', '').split('.')[0])
        date = tmp[0].split('.')
        row.append("{}.{}.{}".format(date[2], date[1], date[0]))
    return res

print(f23([
            [None, "13.01.2004|Кулянц, Д.А.", "0.9"],
            [None, None, None],
            [None, "10.04.2003|Мевов, П.Б.", "0.8"],
            [None, None, None],
            [None, "01.09.1999|Фекумян, В.А.", "0.4"],
            [None, "07.09.2004|Сусий, В.Б.", "0.4"]
        ]))

print(f23([
            [None, None, None],
            [None, "17.04.2004|Закук, И.В.", "0.7"],
            [None, None, None],
            [None, "15.11.2003|Шутизман, Я.К.", "0.8"],
            [None, "03.09.2004|Мубетов, М.И.", "0.4"]
        ]))
