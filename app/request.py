import urllib.request,json
from .models import News


# # Getting api key
# api_key = app.config['NEWS_API_KEY']

# # Getting the news base url
# base_url = app.config["NEWS_API_BASE_URL"]

# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(country,category,):
    get_news_url = base_url.format(country,category,api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        print(get_news_response)
        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        source = news_item.get('source')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if urlToImage:
           news_object = News(source,author,title,description,url,urlToImage,publishedAt)
           news_results.append(news_object)

    return news_results