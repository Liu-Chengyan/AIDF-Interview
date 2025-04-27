import json
import re
from pymongo import MongoClient


def clean_text(text):
    return re.sub(r"\s+", " ", text.strip()) if text else ""


def run_pipeline(input_file="company.json"):
    # Read input data
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            news_list = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {input_file}")
        return

    # Clean data and handle missing values
    processed_news = []
    for item in news_list:
        try:
            # Skip items missing required fields (company, title, date)
            if not all(key in item for key in ["company", "title", "date"]):
                continue
                
            # Clean text fields
            item["title"] = clean_text(item["title"])
            item["date"] = clean_text(item["date"])
            
            # Handle missing summary - replace with title if empty
            item["summary"] = clean_text(item.get("summary", item["title"]))
            
            processed_news.append(item)
        except Exception as e:
            print(f"Error processing item {item.get('title')}: {str(e)}")
            continue

    if not processed_news:
        print("No valid news records to process")
        return

    # Insert into MongoDB
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["WSJ"]
        collection = db["latest_news"]

        for item in processed_news:
            collection.update_one(
                {"title": item["title"], "date": item["date"]},
                {"$set": item},
                upsert=True
            )

        print(f"Successfully processed {len(processed_news)} news records")
        print(f"MongoDB collection: WSJ.latest_news")
    except Exception as e:
        print(f"Database operation failed: {str(e)}")
    finally:
        client.close()


if __name__ == "__main__":
    run_pipeline()