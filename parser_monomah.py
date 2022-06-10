import requests
from bs4 import BeautifulSoup
import json

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en;q=0.9",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.160 YaBrowser/22.5.1.985 Yowser/2.5 Safari/537.36 "
}

data = []

def get_data(url):
    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    shops = soup.find_all("div", class_="shop")
    for shop in shops:
        print(shop)
        try:
            address = shop.find("p", class_="name").text
        except Exception:
            address = "Адресс не указан."

        try:
            phones = shop.find("p", class_="phone").find("a").get("href")
        except Exception:
            phones = "Телефон не указан."

        data.append(
            {
                "address": address,
                "phones": phones
            }
        )

        with open("MONOMAHpars.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    get_data(url='https://monomax.by/map')


if __name__ == "__main__":
    main()
