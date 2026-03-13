import requests
from bs4 import BeautifulSoup


def fetch_top5_products(url: str = "https://www.amazon.co.jp/gp/bestsellers") -> list[str]:
    """Return the titles of the first five bestselling products on Amazon Japan."""

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select("#zg-ordered-list > li")[:5]
    titles = []
    selectors = [
        "div.p13n-sc-truncated",
        "div._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y",
        "div._cDEzb_p13n-sc-css-line-clamp-2_EW94u",
        "div._cDEzb_p13n-sc-css-line-clamp-3_g3dy1",
        "span.zg-text-center-align > div:nth-of-type(1)",
    ]

    for item in items:
        title = None
        for sel in selectors:
            elem = item.select_one(sel)
            if elem:
                title = elem.get_text(strip=True)
                break
        if title:
            titles.append(title)

    if not titles:
        raise ValueError("No product titles found. The page layout may have changed.")

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
