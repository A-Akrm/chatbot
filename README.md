# chatbot

This repository contains a script to fetch the top 5 bestselling products from Amazon Japan.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script to print the product names:

```bash
python amazon_top5.py
```

The script scrapes Amazon's bestseller page and outputs the first five product titles. A network connection is required for the script to work.
If you see an error or no titles are printed, ensure that the dependencies are installed and that you can access the Amazon Japan website.
