# --------ქვიზი 4 (Web Scraping/Parsing)--------
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open("Top-Sites.csv", "w", encoding="utf-8_sig", newline="\n")

file_obj = csv.writer(file)
file_obj.writerow(
    ["საიტი", "საიტის აღწერა", "ჰიტები (გუშინ)", "უნიკალური (გუშინ)", "საშუალოდ 1 დღეში", "უნიკალური თვეში"])

ind = 1

while ind <= 5:
    url = f"https://top.ge/page/{ind}"
    r = requests.get(url)
    print(r.status_code)

    content = r.text
    soup = BeautifulSoup(content, "html.parser")

    tbody = soup.find("tbody")
    all_sites = tbody.find_all("tr")

    for i in all_sites:
        title = i.find("a", class_="stie_title").text.strip()
        about = i.find("td", class_="tr_paddings desc_pd hidden-xs ipad_hidden").text.strip()
        hits = i.find("span", class_="stat_now_big").text.strip()
        unique = i.find_all("span", class_="stat_now_big")[1].text.strip()
        average_day = i.find_all("span", class_="stat_now_big")[2].text.strip()
        unique_month = i.find_all("span", class_="stat_now_big")[3].text.strip()
        file_obj.writerow([title, about, hits, unique, average_day, unique_month])

    ind += 1
    sleep(randint(1, 5))
    print(ind)
