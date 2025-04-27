import json
from transformers import pipeline

# Load the dataset
with open('company.json', 'r', encoding = 'utf-8') as file:
    data = json.load(file)
data = data[:10]  # Limit to first 10 articles

# Set up the sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis", model="distilbert-base-uncased", device=-1)

# Prepare the markdown table
markdown_table = "Company | Sentiment | Summary\n--- | --- | ---\n"

# Set up the paraphrasing model
paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws", device=-1)

for article in data:
    company = article['company']
    title = article['title']
    
    # Sentiment analysis
    sentiment_result = sentiment_analysis(title)
    sentiment_label = sentiment_result[0]['label']
    
    # Adjust sentiment assignment
    if sentiment_label.upper() == 'NEGATIVE':
        sentiment = 'Negative'
    elif sentiment_label.upper() == 'NEUTRAL':
        sentiment = 'Neutral'
    else:
        sentiment = 'Positive'
    
    # Paraphrasing the title
    paraphrased_title = paraphraser(f"paraphrase: {title}", max_length=50)[0]['generated_text']
    
    # Append to the markdown table
    markdown_table += f"{company} | {sentiment} | {paraphrased_title}\n"

# Print the final markdown table
print(markdown_table)