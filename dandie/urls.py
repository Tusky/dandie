from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.home', name='home'),
    url(r'news/(?P<news_id>\w+)', 'news.views.specific_new', name="specific_news"),
    url(r'^admin/', include(admin.site.urls)),
)
