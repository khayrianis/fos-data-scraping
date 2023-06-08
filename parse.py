import requests
from bs4 import BeautifulSoup


def parse(url="https://fr.wikipedia.org/wiki/Alger"):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    trs = soup.find_all("tr")
    for tr in trs:
        th = tr.find("th")
        td = tr.find("td")
        if th:
            if th.text.strip() == "Population":
                with open("parse.txt", "w") as file:
                    file.write(td.text.strip())
                return td


if __name__ == "__main__":
    td = parse()
    print(td.text.strip())
