from requests import get
from datetime import datetime
from csv import DictWriter
from bs4 import BeautifulSoup
import re

new = "/feed/?q=flask"

with open("base.csv", mode="w", encoding="utf8") as f:
    dict_base = DictWriter(f, fieldnames=["data", "title", "link", "text"], delimiter=";")
    while new:
        row = {}
        res = get(f"https://pythondigest.ru{new}")
        soup = BeautifulSoup(res.text, "html.parser")
        for tag in soup.find_all("div", class_="items-container"):
            title = tag.find(rel=["nofollow"])
            row["title"] = title.get_text()
            row["title"] = title.get("href")
            dat = tag.find("small")
            d1 = re.search(r"\d{2}\.\d{2}\.d{4}", dat.get_text())[0]
            d2 = datetime.strptime(d1, "%d.%m.%y").date()
            row["date"] = d2
            row["text"] = ''.join([x.get_text() for x in tag.find_all("p")])
            dict_base.writerow(row)
        ss = soup.find("ul", class_="pagination pagination-sm")
        p = ss.find_all("li")[-1]
        url = p.a.get("href")
