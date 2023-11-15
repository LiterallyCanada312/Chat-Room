
from django.contrib import admin
from django.urls import path, include

from Messaging import views

urlpatterns = [
    path("Messaging/", admin.site.urls),
    path('', include("mysite.urls")),
]