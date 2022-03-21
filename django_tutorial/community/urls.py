from django.urls import path
from .views import write, articlelist, viewdetail

app_name = 'community'
urlpatterns = [
 
    path('write/',write, name='write'),

    path('list/',articlelist, name='article_list'),

    path('view_detail/<int:num>/', viewdetail, name='view_detail'),
    
]
