from django.urls import path

from . import views

urlpatterns = [
    path('current_user/', views.current_user),
    path('', views.UserListView.as_view()),
]
