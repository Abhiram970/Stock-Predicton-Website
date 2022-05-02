from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/login/')
def home2(request):
    url = f'https://gnews.io/api/v4/search?q=example&token=522813761f2a6540308e793ba2ecddfd'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    desc = []
    news = []
    img = []
    date = []
    author = []
    source = []
    url = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['image'])
        date.append(article['publishedAt'])
        # author.append(article['author'])
        source.append(article['source']['name'])
        url.append(article['url'])
    mylist = zip(news, desc, img,date,source,url)

    return render(request, "news/news.html", context={"mylist": mylist})