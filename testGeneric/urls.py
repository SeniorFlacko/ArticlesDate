"""testGeneric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from newapp.models import Article
from django.views.generic.dates import ArchiveIndexView,DateDetailView
from newapp.views import (ArticleYearArchiveView,
                          ArticleMonthArchiveView,
                          ArticleWeekArchiveView,
                          ArticleDayArchiveView,
                          ArticleTodayArchiveView,
                          )
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^archive/$',
        ArchiveIndexView.as_view(model=Article, date_field="pub_date"),
        name="article_archive"),
    url(r'^(?P<year>[0-9]{4})/$',ArticleYearArchiveView.as_view(),name="article_year_archive"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',ArticleMonthArchiveView.as_view(month_format='%m'),name="archive_month_numeric"),
    url(r'^(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$',ArticleWeekArchiveView.as_view(),name="archive_week"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$',ArticleDayArchiveView.as_view(),name="archive_day"),
    url(r'^today/$',ArticleTodayArchiveView.as_view(),name="archive_today"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/(?P<pk>[0-9]+)/$',
    DateDetailView.as_view(model=Article, date_field="pub_date"),
    name="archive_date_detail"),
]
