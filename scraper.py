from bs4 import BeautifulSoup as bs
from playwright.sync_api import sync_playwright


def get_citations_needed_count(url_string):
    pass


def get_citations_needed_report(url_string):
    pass


if __name__ == "__main__":
    get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    print("\n")
    get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")