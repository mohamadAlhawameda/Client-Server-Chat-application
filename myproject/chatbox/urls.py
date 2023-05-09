from django.urls import path
#Package to work with routes 

from . import views


#ROUTES 
urlpatterns = [
    path('', views.index, name='index'),
    path('chat_history/', views.chat_history, name='chat_history'),
    path('user_list/', views.user_list, name='user_list'),
    path('response_history/', views.response_history, name='response_history'),
    # path('chat/', views.chat_history, name='chat_history')
]
