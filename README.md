# Financial News Scraper from WSJ

## Project Overview

This project aims to scrape the latest earnings-related news about Apple (AAPL), Microsoft (MSFT) and Google (GOOGL) from the Wall Street Journal (WSJ), and store the results in a structured format for further processing.

---

## Source and Target Companies

- **Source Website**: Wall Street Journal (WSJ)
- **Target Companies**:
  - Apple Inc. (Ticker: AAPL)
  - Microsoft Corporation (Ticker: MSFT)
  - Alphabet Inc. (Ticker: GOOGL)

---

## Methodology

- Manually construct request headers and cookies to simulate real browser visits and bypass basic anti-crawling detections: Capture a real cURL request from WSJ and manually rewrite it into a Python `requests` format.
- Use the `requests` library to send HTTP requests, including necessary headers and cookies.
- Parse the HTML page with `BeautifulSoup` to extract the hidden `<script>` tag (id=`__NEXT_DATA__`): Use `BeautifulSoup` to locate the hidden `<script id="__NEXT_DATA__">` tag, extract the standard JSON data, and parse it into a Python object using `json.loads`, making it easier to retrieve useful information such as headlines, timestamps, and summaries..
- Parse the embedded JSON data to extract article information such as headline, timestamp, and summary.
- Handle pagination by looping through multiple pages until no more search results are available.
- Store structured data in a list (which can later be exported to JSON or CSV files).


---

## Keywords List

| Company | Keyword | Description |
|:--------|:--------|:------------|
| AAPL | apple | Company name |
| AAPL | iphone | Flagship smartphone product |
| AAPL | aapl | Stock ticker |
| AAPL | macbook | Laptop product line |
| AAPL | ipad | Tablet product line |
| AAPL | ios | Mobile operating system |
| AAPL | apple inc | Full company name |
| AAPL | apple earnings | Earnings-related news |
| AAPL | apple revenue | Revenue-related news |
| AAPL | tim cook | CEO of Apple |
| MSFT | microsoft | Company name |
| MSFT | msft | Stock ticker |
| MSFT | windows | Operating system product |
| MSFT | office | Office software suite |
| MSFT | azure | Cloud computing platform |
| MSFT | xbox | Gaming console product |
| MSFT | microsoft corp | Full company name |
| MSFT | satya nadella | CEO of Microsoft |
| MSFT | microsoft earnings | Earnings-related news |
| MSFT | microsoft cloud | Cloud services news |
| GOOGL | alphabet | Parent company name |
| GOOGL | google | Subsidiary company name |
| GOOGL | googl | Stock ticker |
| GOOGL | android | Mobile operating system |
| GOOGL | youtube | Video sharing platform |
| GOOGL | chrome | Web browser product |
| GOOGL | google cloud | Cloud computing services |
| GOOGL | google earnings | Earnings-related news |
| GOOGL | alphabet inc | Full parent company name |
| GOOGL | sundar pichai | CEO of Google |
| GOOGL | waymo | Alphabet's autonomous driving subsidiary |

---

## Data Format

The scraped news articles are stored in a JSON format as a list of objects, where each object represents one article with four fields:

Example:
```json
[
  {
    "company": "AAPL",
    "title": "Apple Q2 earnings beat expectations",
    "date": "2025-04-23",
    "summary": "Apple reports strong second-quarter earnings driven by iPhone sales."
  },
  {
    "company": "MSFT",
    "title": "Microsoft sees cloud revenue jump",
    "date": "2025-04-22",
    "summary": "Microsoft's Azure cloud revenue increases by 28% year-over-year."
  }
]
```
| Field    | Description |
|:---------|:------------|
| company  | Company ticker symbol (e.g., AAPL, MSFT, GOOGL) |
| title    | News headline |
| date     | News publication date (format: YYYY-MM-DD) |
| summary  | Short summary of the article |

---

## reCAPTCHA Strategy

No explicit reCAPTCHA challenges were encountered during the WSJ news scraping process.  
This project utilizes a cURL-based request construction approach with browser fingerprinting and manual cookie management to bypass basic anti-bot detections.

If actual reCAPTCHA protection is encountered, the following strategies can be considered:
- Simulating real user behavior using Selenium browser automation.
- Using third-party CAPTCHA-solving services (e.g., 2captcha, AntiCaptcha).
- Rotating proxy IPs combined with request throttling.
- Employing stealth plugins for headless browsers (e.g., puppeteer-extra-plugin-stealth).

---

## Files and Directory Structure


- `wsj.py` scrapes the earnings news articles from WSJ.
- Each company folder stores individual keyword-based JSON files.
- `company.json` aggregates all articles into a single file.
