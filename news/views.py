from django.shortcuts import render
from django.views.generic import ListView

from .models import News


class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"

        return context
