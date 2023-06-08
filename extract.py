import requests


def exctarct(
    url: str = "https://www.ouedkniss.com/appartement-vente-f4-chlef-tenes-algerie-d35916540",
):
    resp = requests.get(url)
    with open("extract.txt", "w") as file:
        file.write(resp.text)
    return resp


if __name__ == "__main__":
    resp = exctarct()
    print(resp.text)
