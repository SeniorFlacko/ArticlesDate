# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.dates import (
                                        YearArchiveView,
                                        MonthArchiveView,
                                        WeekArchiveView,
                                        DayArchiveView,
                                        TodayArchiveView,
                                        )
from django.shortcuts import render
from models import Article
# Create your views here.
class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    week_format = "%W"
    allow_future = True


class ArticleDayArchiveView(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

class ArticleTodayArchiveView(TodayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True