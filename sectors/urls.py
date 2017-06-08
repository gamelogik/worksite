from django.conf.urls import url, include
from . import views, forms


urlpatterns = [
    url(r'^$', views.sector_list, name='list'),
    url(r'(?P<sector_pk>\d+)/(?P<job_pk>\d+)/apply/$', views.apply_view, name='apply'),
    url(r'(?P<sector_pk>\d+)/t(?P<job_pk>\d+)/$', views.text_detail, name='text'),
    url(r'(?P<sector_pk>\d+)/q(?P<job_pk>\d+)/$', views.quiz_detail, name='quiz'),
    url(r'(?P<pk>\d+)/$', views.sector_detail, name='detail'),
]