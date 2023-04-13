from app import db

class Article(db.Model):
    __tablename__ = 'articles'
    plataform = db.Column(db.String)
    title = db.Column(db.String)
    url = db.Column(db.String, primary_key=True)
    thumbnail = db.Column(db.String)
    published_date = db.Column(db.DateTime)
    sentiment_score = db.Column(db.Float)
    sentiment_explanation = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return f"<Article(title='{self.title}', url='{self.url}')>"
    
    def to_dict(self):
        return {
            'plataform': self.plataform,
            'title': self.title,
            'url': self.url,
            'thumbnail' : self.thumbnail,
            'published_date' : self.published_date,
            'sentiment_score': self.sentiment_score,
            'sentiment_explanation': self.sentiment_explanation,
            'text': self.text
        }