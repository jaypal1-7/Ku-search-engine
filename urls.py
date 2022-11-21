#from django.conf.urls import url, include
from django.urls import path
from views import Home,search_query,relevance_feedback

#this file is related to Django framework

app_name = 'personal'
urlpatterns = [
    path('', Home, name='index'),
    path('<tosearch>/', search_query, name='search'),
    path('<reldoc>/<reldoc1>/', relevance_feedback, name='relevance')    
]
