from extract import exctarct
from parse import parse
from parse_js import parse_js

def scrape():
    resp=exctarct()
    print(resp.text)
    td=parse()
    print(td.text.strip())
    elements=parse_js()
    for elt in elements:
        print(elt.text)

scrape()