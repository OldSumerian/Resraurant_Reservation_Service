from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reserve_service/', include('reserve_service.urls', namespace='reserve_service')),
    path('users/', include('users.urls', namespace='users')),
]
