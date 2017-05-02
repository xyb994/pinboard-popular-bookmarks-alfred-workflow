import json
import requests


def get_items():
    items = []

    url = 'http://feeds.pinboard.in/json/popular/'
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json()
        for article in articles:
            parsed_article = parse_article(article['d'], article['u'])
            items.append(parsed_article)

    alfred_return_results = json.dumps({'items': items})
    return alfred_return_results


def parse_article(article_title, article_url):
    parsed_article = {
        'title': article_title[:53],
        'subtitle': article_title,
        'arg': article_url,
        'quicklookurl': article_url,
    }
    return parsed_article
