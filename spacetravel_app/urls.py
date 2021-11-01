from django.urls import path

from spacetravel_app import views

urlpatterns = [
    path('', views.index)
]
