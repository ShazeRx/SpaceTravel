from django.contrib.auth import views as generic_auth_views
from django.urls import path

from authentication.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', generic_auth_views.LogoutView.as_view(next_page='login'))
]
