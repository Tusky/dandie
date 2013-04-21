from django.shortcuts import render
from news.forms import NewForm
from news.models import New

def home(request):
    news_list = New.objects.all().order_by("-created_at")
    return render(request, "index.html", { "news_list": news_list })

def specific_new(request, news_id):
    news = New.objects.get(pk=news_id)
    form = NewForm()
    return render(request, "index_specific.html", { "news": news, "form": form })