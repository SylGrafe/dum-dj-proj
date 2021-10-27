# this file is  /home/syl1/private/Pgm/djo1/top/polls/urls.py
# for more "gettings started with django "detailed  comments see 
#   /home/syl1/private/Pgm/djo1/top/polls/urls_tut3.py
# https://docs.djangoproject.com/en/3.1/intro/tutorial04/


from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


