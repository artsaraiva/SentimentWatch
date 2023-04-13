import openai
import os
from app.models import Article
from app import db, app
from flask import jsonify


def get_openai_secret():
    return os.environ.get("OPENAI_KEY")


def get_sentiment(text):
    openai.api_key = get_openai_secret()

    model_engine = "gpt-3.5-turbo"
    messages = []
    messages.append(
        {
            "role": "system",
            "content": "Please score the sentiment of this article on a scale of -1 (negative) to 1 (positive). Format the analysis in this way:\n"
            "SCORE: the number between -1 (negative) to 1 (positive). Only the number and nothing else\n"
            "EXPLANATION: the reasoning for the scoring\n\n"
            f"{text}",
        }
    )

    response = openai.ChatCompletion.create(model=model_engine, messages=messages)

    response_string = response.choices[0].message.content

    score = float(response_string.split(":")[1].split("\n")[0].strip())
    explanation = response_string.split(":")[2].strip()

    return (float(score), explanation)


def update_sentiment_scores():
    try:
        with app.app_context():
            with db.session() as session:
                articles = session.query(Article).all()

                for article in articles:
                    score, explanation = get_sentiment(article.text)

                    article.sentiment_score = score
                    article.sentiment_explanation = explanation

                    session.add(article)

                session.commit()
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()
