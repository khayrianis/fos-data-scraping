import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def parse_js(
    url="https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas",
):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    driver.get(url)
    time.sleep(30)
    elements = driver.find_elements(By.CSS_SELECTOR, ".primary")
    with open("parse_js.txt", "w") as file:
        for elt in elements:
            file.write(elt.text)
            print(elt.text)

    driver.quit()


if __name__ == "__main__":
    parse_js()
