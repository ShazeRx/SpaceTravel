from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^health/', include('health_check.urls')),
    path('', include('spacetravel_app.urls'))
]
