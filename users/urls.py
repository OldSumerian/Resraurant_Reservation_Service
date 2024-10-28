from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from django.views.generic import DeleteView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, confirm_user, ProfilePasswordRestoreView, my_cabinet, AdminView, \
    deactivate_view

app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("user/logout/", LogoutView.as_view(), name="logout"),
    path("user/registration/", RegisterView.as_view(), name="registration"),
    path("user/profile/", ProfileView.as_view(), name="profile"),
    path('user/confirm/<str:code>/', confirm_user, name="confirm"),
    path('user/restore_password/', ProfilePasswordRestoreView.as_view(), name="restore_password"),
    path('user/my_cabinet/', my_cabinet, name='my_cabinet'),
    path('user/<str:pk>/delete/', DeleteView.as_view(), name="delete_user"),
    path('user/admin/', AdminView.as_view(), name="admin"),
    path('user/deactivate/<int:pk>/', deactivate_view, name="deactivate"),
]
