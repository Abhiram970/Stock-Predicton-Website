from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from datetime import date
today = date.today()
# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/login/')
def home2(request):
    url = f'https://newsapi.org/v2/everything?q=business&from={today}&sortBy=publishedAt&lang=en&apiKey=ab33356e87d442da83f47ee4856970a2'
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
        img.append(article['urlToImage'])
        date.append(article['publishedAt'])
        author.append(article['author'])
        source.append(article['source']['name'])
        url.append(article['url'])
    mylist = zip(news, desc, img,date,author,source,url)

    return render(request, "news/news.html", context={"mylist": mylist})