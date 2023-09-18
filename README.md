# py-web-hw9

This project is designed for web scraping of quotes and author information and subsequently loading the scraped data into MongoDB.

## Directory Structure

- `config.ini`: Configuration file.
- `connect_to_mongodb.py`: Script to establish a connection with MongoDB.
- `load_data_to_mongodb.py`: Script to load scraped data from JSON files into MongoDB.
- `main.py`: Main script for running the project.
- `models.py`: Defines the MongoDB models/schema.
- `poetry.lock` & `pyproject.toml`: Dependency management and packaging files.
- `output/`: Directory containing the scraped data in JSON format.
    - `authors.json`: Contains author information.
    - `quotes.json`: Contains quotes.
- `scrapy_project/`: Main Scrapy project directory.
    - `items.py`: Defines the Scrapy items.
    - `spiders/`: Contains the spiders used for web scraping.
        - `quotes_spider.py`: Spider for scraping quotes.

## How to Run

1. Ensure MongoDB is running locally.
2. Run the main script:
    ```bash
    python main.py
    ```
3. To load the data into MongoDB:
    ```bash
    python load_data_to_mongodb.py
    ```
