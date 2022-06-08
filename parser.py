import requests
import json

url = "https://api.kfc.com/api/store/v2/store.get_restaurants"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en;q=0.9",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.160 YaBrowser/22.5.1.985 Yowser/2.5 Safari/537.36 "
}
data = []
req = requests.get(url, headers=headers)
json_data = json.loads(req.text)
results = json_data['searchResults']
for res in results:
    try:
        address = res['storePublic']['contacts']['streetAddress']['ru']
    except Exception:
        address = "Адрес не указан."

    try:
        latlon = res['storePublic']['contacts']['coordinates']['geometry']['coordinates']
    except Exception:
        latlon = "Координаты не указаны."

    try:
        name = res['storePublic']['title']['ru']
    except Exception:
        name = "Название не указано."

    try:
        phones = res['storePublic']['contacts']['phoneNumber']
    except Exception:
        phones = "Номер не указан."

    try:
        start_time = res['storePublic']['openingHours']['regular']['startTimeLocal'].replace(':00', '', 1)
        end_time = res['storePublic']['openingHours']['regular']['endTimeLocal'].replace(':00', '', 1)
        start_time_daily = res['storePublic']['openingHours']['regularDaily'][5]['timeFrom'].replace(':00', '', 1)
        end_time_daily = res['storePublic']['openingHours']['regularDaily'][5]['timeTill'].replace(':00', '', 1)
        working_hours = f'пн - пт   c {start_time} до {end_time}, сб - вс   с {start_time_daily} до {end_time_daily}'
    except Exception:
        working_hours = "Режим работы не указан."

    data.append(
        {
            "address": address,
            "latlon": latlon,
            "name": name,
            "phones": phones,
            "working_hours": working_hours
        }
    )

    with open("KFCpars.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
