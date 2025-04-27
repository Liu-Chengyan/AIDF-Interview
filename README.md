# LLM Data Engineering Task

## Project Overview

This repository contains the solutions for the LLM Data Engineering internship task, covering web scraping, simple data pipeline automation and LLM-driven visualizations and summarizations.

The work is divided into four parts, each implemented in a separate Git branch.

---

## Branches Overview

- **Financial-News-Scraper**
  - Task 1: Scrape earnings news articles about Apple (AAPL), Microsoft (MSFT) and Google (GOOGL) from the Wall Street Journal (WSJ).
  - Includes handling basic anti-bot mechanisms and organizing scraped data.

- **Data-Pipeline-Automation**
  - Task 2: Build a simple automated pipeline to clean and normalize the scraped data.
  - Load the cleaned data into a local MongoDB database.
  - Set up periodic execution using scheduling tools.

- **Option-A-LLM-Driven-Visualization**
  - Task 3 (Option A): Use OpenAI models to assist in generating visualizations.
  - Create a histogram of news articles by company and build an interactive Streamlit dashboard.

- **Option-B-LLM-Driven-Structured-Summarization**
  - Task 3 (Option B): Use OpenAI models to assist in structuring news article headlines into company, sentiment and summary fields.
  - Develop code that enables structured semantic parsing and summarization of news headlines into company, sentiment and summary fields.

---

## How to Explore

To view the detailed implementations:
1. Switch to the corresponding branch.
2. Open the branch-specific `README.md` for a full explanation.
3. Review the uploaded code, results and screenshots.

---

## Technologies Used

- Python 3.9+
- Requests, BeautifulSoup
- MongoDB
- Streamlit
- OpenAI API (`gpt-3.5-turbo`)
- Schedule library

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Liu-Chengyan/AIDF-Interview.git
cd AIDF-Interview
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install all dependencies:

```bash
pip install -r requirements.txt
```

---
## Contact

For any questions or discussions, feel free to open an issue or contact me through GitHub.

