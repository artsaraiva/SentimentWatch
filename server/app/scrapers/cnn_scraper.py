import feedparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from app.models import Article
from app import db, app
from datetime import datetime
from app.util.db_utils import check_if_article_exists
from dateutil.parser import parse
from app.util.openai_api import get_sentiment
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_cnn_articles():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    rss_url = "http://rss.cnn.com/rss/cnn_topstories.rss"
    feed = feedparser.parse(rss_url)

    count = 0
    with app.app_context():
        with db.session() as session:
            for entry in feed.entries:
                if "published" in entry and "media_content" in entry and entry.link.endswith(".html"):
                    if not check_if_article_exists(entry.link):
                        article_url = entry.link
                        article_published_date = entry.published
                        print(">>>" + article_url)
                        media_content = entry.get("media_content", [])
                        if media_content:
                            article_thumbnail_url = media_content[0]["url"]
                        else:
                            article_thumbnail_url = None
                        driver.get(article_url)
                        wait = WebDriverWait(driver, 10)
                        wait.until(
                            EC.presence_of_element_located(
                                (By.CLASS_NAME, "paragraph.inline-placeholder")
                            )
                        )
                        soup = BeautifulSoup(driver.page_source, "html.parser")
                        paragraphs = soup.find_all(
                            "p", {"class": "paragraph inline-placeholder"}
                        )
                        article_text = "\n".join(
                            [
                                p.get_text().strip()
                                for p in paragraphs
                                if p.get_text().strip()
                            ]
                        )
                        article_title = (
                            entry.title.replace("/", "-")
                            .replace("\\", "-")
                            .replace("|", "-")
                        )

                        sentiment_result = get_sentiment(article_text)

                        article_sentiment_score = sentiment_result[0]
                        article_sentiment_explanation = sentiment_result[1]

                        article = Article(
                            plataform="CNN",
                            title=article_title,
                            url=article_url,
                            thumbnail=article_thumbnail_url,
                            published_date=datetime.strptime(
                                article_published_date, "%a, %d %b %Y %H:%M:%S %Z"
                            ),
                            sentiment_score=article_sentiment_score,
                            sentiment_explanation=article_sentiment_explanation,
                            text=article_text,
                        )
                        session.add(article)
                        session.commit()
                    count += 1
                    if count == 5:
                        break
                session.close()
