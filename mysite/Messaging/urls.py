from django.urls import path

from Messaging import views

urlpatterns = [
    path('', views.index)
]