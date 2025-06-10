import os
import requests
from bs4 import BeautifulSoup


def fetch_top5_products(url="https://www.amazon.co.jp/gp/bestsellers"):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [span.get_text(strip=True) for span in soup.select("div.p13n-sc-truncated")][:5]
    return titles


def main():
    try:
        top5 = fetch_top5_products()
        for i, title in enumerate(top5, 1):
            print(f"{i}. {title}")
    except Exception as e:
        print("Error fetching products:", e)


if __name__ == "__main__":
    main()
