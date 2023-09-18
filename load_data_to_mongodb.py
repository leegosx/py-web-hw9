import json
from models import Author, Quotes
from connect_to_mongodb import connect_url

connect_url()

with open('output/quotes.json', 'r', encoding='utf-8') as f:
    quotes_data = json.load(f)
    
with open('output/authors.json', 'r', encoding='utf-8') as f:
    authors_data = json.load(f)

quotes_map = {}    
for quote in quotes_data:
    qotes_doc = Quotes(**quote).save()
    quotes_map[quote['tags']] = qotes_doc
    quotes_map[quote['author']] = qotes_doc
    quotes_map[quote['text']] = qotes_doc

authors_map = {}
for author in authors_data:
    author_doc = Author(**author).save()
    authors_map[author['fullname']] = author_doc
    authors_map[author['born']] = author_doc
    authors_map[author['bio']] = author_doc

if __name__ == "__main__":     
    print("All data loaded successfully!")