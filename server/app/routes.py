from flask import jsonify
from app.models import Article
from app import db, app


@app.route("/api/articles")
def index():
    with db.session() as session:
        try:
            articles = session.query(Article).all()
            sorted_articles = sorted(articles, key=lambda article: article.published_date, reverse=True)
            article_list = [article.to_dict() for article in sorted_articles]
            return jsonify(article_list)

        except Exception as e:
            session.rollback()
            return jsonify({"error": str(e)}), 500

        finally:
            session.close()