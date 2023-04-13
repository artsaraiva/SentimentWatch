import feedparser
from bs4 import BeautifulSoup
from app.models import Article
from app import db, app
from datetime import datetime
from app.util.db_utils import check_if_article_exists
from dateutil.parser import parse
from app.util.openai_api import get_sentiment


def scrape_foxnews_articles():
    rss_url = "https://moxie.foxnews.com/google-publisher/latest.xml"
    feed = feedparser.parse(rss_url)

    count = 0
    with app.app_context():
        with db.session() as session:
            for entry in feed.entries:
                if "published" in entry and not check_if_article_exists(entry.link):
                    article_url = entry.link
                    article_published_date = entry.published
                    article_published_date = article_published_date.replace('EDT', '-0400')
                    media_content = entry.get("media_content", [])
                    if media_content:
                        article_thumbnail_url = media_content[0]["url"]
                    else:
                        article_thumbnail_url = None
                    soup = BeautifulSoup(entry.description, "html.parser")
                    article_text = soup.get_text()
                    article_title = (
                        entry.title.replace("/", "-")
                        .replace("\\", "-")
                        .replace("|", "-")
                    )

                    sentiment_result = get_sentiment(article_text)

                    article_sentiment_score = sentiment_result[0]
                    article_sentiment_explanation = sentiment_result[1]

                    article = Article(
                        plataform="FOXNEWS",
                        title=article_title,
                        url=article_url,
                        thumbnail=article_thumbnail_url,
                        published_date=datetime.strptime(
                            article_published_date, "%a, %d %b %Y %H:%M:%S %z"
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
