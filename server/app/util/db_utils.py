from app import db, app
from flask import jsonify
from app.models import Article

def create_all_tables():
    print("Creating tables...")
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(jsonify({"error": str(e)}), 500)


def delete_all_tables():
    print("Deleting tables...")
    with app.app_context():
        try:
            db.drop_all()
        except Exception as e:
            print(jsonify({"error": str(e)}), 500)

def check_if_article_exists(url):
    with db.session() as session:
        article = session.query(Article).filter(Article.url == url).first()
        session.close()
        
        if article is not None:
            return True
        else:
            return False