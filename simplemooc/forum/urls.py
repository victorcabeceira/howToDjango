from django.conf.urls import url, include
from simplemooc.forum import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  
]
