from django.urls import path

from . import views
from .views import LoginView

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('history/<str:room_id>/', views.history, name='history'),
    # path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('<str:group_id>/', views.room, name='room'),
    path('login/', LoginView.as_view(), name='login-view'),
]
