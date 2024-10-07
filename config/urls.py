from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reserv_service/', include('reserv_service.urls', namespace='reserv_service')),
    path('users/', include('users.urls', namespace='users')),
]
