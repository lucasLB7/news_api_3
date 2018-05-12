from app import app
import urllib.request,json
from .models import news_article
from .models import news_source


Source = news_source.Source
Article = news_article.Article

# We get the API key

api_key = app.config['NEWS_API_KEY']

# We get the urllib

base_url = app.config['BASE_URL']


def get_news(category):
    get_news_url = base_url.format(category,api_key)
    print(get_news_url)

    # with urllib.request.urlopen(get_news_url) as url:
    #     get_news_data = url.read()
    #
    #     get_news_response = json.loads(get_news_data)
    #
    #     news_results = None
#     return get_news_response
#
#         if get_news_response['results']:
#             news_result_list = get_news_response['results']
#             news_results = process_results(news_result_list)
#
#     return news_results
#
# def process_results(movie_list):
#     news_source_results = []
#     for article in news_source_results:
#
#         author = movie_item.get('author')
#         title = movie_item.get('title')
#         description = movie_item.get('description')
#         url = movie_item.get('url')
#         urlImage = movie_item.get('urlToImage')
#         published = movie_item.get('publishedAt')
#
#
#
#         if image:
#             movie_object = Movie(id,title,description,image,author)
#             movie_results.append(movie_object)
#
#     return movie_results
