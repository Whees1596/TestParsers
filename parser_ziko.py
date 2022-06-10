import requests
import json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
}

data = []


def get_data(url):
    req = requests.get(url, headers=headers)
    json_data = json.loads(req.text)
    for i, value in json_data.items():
        try:
            address = value['address']
        except Exception:
            address = 'Адрес не указан.'

        try:
            name = value['title']
        except Exception:
            name = 'Название не указано.'

        try:
            working_hours = value['mp_pharmacy_hours'].replace('<br>', ', ')
        except Exception:
            working_hours = 'Режим работы не указан.'

        try:
            lat = value['lat']
            lon = value['lng']
            latlon = lat, lon
        except Exception:
            latlon = 'Координаты не указаны.'

        data.append(
            {
                "address": address,
                "latlon": latlon,
                "name": name,
                "working_hours": working_hours
            }
        )

        with open("ZIKOpars.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    get_data(url='https://www.ziko.pl/wp-admin/admin-ajax.php?action=get_pharmacies')


if __name__ == "__main__":
    main()