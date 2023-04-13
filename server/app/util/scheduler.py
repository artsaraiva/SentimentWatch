import schedule
import time
from app import db, app
from flask import jsonify
from app.models import Article
from app.scrapers.cnn_scraper import scrape_cnn_articles
from app.scrapers.foxnews_scraper import scrape_foxnews_articles


def schedule_update_articles():
    print("Scheduling daily event to scrape and update openai sentiment...")

    scrape_cnn_articles()
    scrape_foxnews_articles()

    # Schedule the next update in 2 hours
    schedule.every(2).hours.do(schedule_update_articles)

    while True:
        schedule.run_pending()
        time.sleep(10)
