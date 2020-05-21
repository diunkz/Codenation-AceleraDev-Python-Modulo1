from datetime import datetime, timedelta


# global variables

MINUTE_FEE = 0.09
FIX_FEE = 0.36


# pep8

records = [
    {'source': '48-996355555',
     'destination': '48-666666666',
     'end': 1564610974,
     'start': 1564610674},

    {'source': '41-885633788',
     'destination': '41-886383097',
     'end': 1564506121,
     'start': 1564504821},

    {'source': '48-996383697',
     'destination': '41-886383097',
     'end': 1564630198,
     'start': 1564629838},

    {'source': '48-999999999',
     'destination': '41-885633788',
     'end': 1564697158,
     'start': 1564696258},

    {'source': '41-833333333',
     'destination': '41-885633788',
     'end': 1564707276,
     'start': 1564704317},

    {'source': '41-886383097',
     'destination': '48-996384099',
     'end': 1564505621,
     'start': 1564504821},

    {'source': '48-999999999',
     'destination': '48-996383697',
     'end': 1564505721,
     'start': 1564504821},

    {'source': '41-885633788',
     'destination': '48-996384099',
     'end': 1564505721,
     'start': 1564504821},

    {'source': '48-996355555',
     'destination': '48-996383697',
     'end': 1564505821,
     'start': 1564504821},

    {'source': '48-999999999',
     'destination': '41-886383097',
     'end': 1564610750,
     'start': 1564610150},

    {'source': '48-996383697',
     'destination': '41-885633788',
     'end': 1564505021,
     'start': 1564504821},

    {'source': '48-996383697',
     'destination': '41-885633788',
     'end': 1564627800,
     'start': 1564626000}
]


# creating a night time list

def night_time():
    night_hour_list = []
    hour = 0
    while (hour < 24):
        if hour < 6 or hour >= 22:
            for y in range(60):
                night_hour_list.append(str(timedelta(hours=hour, minutes=y)))
            hour += 1
            if hour == 6:
                hour = 22
    return night_hour_list


# calculating fees

def call_fee(start, end):
    count = timedelta(seconds=end-start)
    start = datetime.fromtimestamp(start)
    total = FIX_FEE
    times = 0.0

    while(count > timedelta(seconds=59)):
        if start.strftime("%H:%M:00") not in night_time():
            times += 1
        start += timedelta(minutes=1)
        count -= timedelta(minutes=1)

    total += times * MINUTE_FEE

    return total


# sorting by phone number and calculating total calls

def classify_by_phone_number(records):
    new_records = []

    for x in records:
        total = call_fee(x["start"], x["end"])
        new_dict = {"source": x["source"], "total": total}
        condition = False

        if len(new_records):
            for i in range(len(new_records)):
                if new_dict["source"] == new_records[i]["source"]:
                    new_records[i]["total"] += total
                    condition = True
                    break

        if condition is False:
            new_records.append(new_dict)

    for x in new_records:
        x["total"] = round(x["total"], 2)

    return sorted(new_records, key=lambda k: k['total'], reverse=True)
