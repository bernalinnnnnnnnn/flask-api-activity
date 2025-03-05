import feedparser
from flask import Flask, render_template

app = Flask(__name__)

#bbc_feed = "http://feeds.bbci.co.uk/news/rss.xml"
rss_feeds = {'bbc': "http://feeds.bbci.co.uk/news/rss.xml",
             'cnn': "http://rss.cnn.com/rss/edition.rss",
             'fox': "http://feeds.foxnews.com/foxnews/latest"}


@app.route("/")
@app.route("/bbcnews")
def bbc():
    return get_news('bbc')


@app.route("/cnnnews")
def cnn():
    return get_news('cnn')


@app.route("/foxnews")
def fox():
    return get_news('fox')


def get_news(publication):
    feed = feedparser.parse(rss_feeds[publication])
    print(feed)
    article = feed['entries']
    print(article)
    return render_template("home.html", Article = feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
