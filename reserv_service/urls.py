from django.urls import path
from reserv_service.apps import ReservServiceConfig


app_name = ReservServiceConfig.name

urlpatterns = [
    # path("", LoginView.as_view(template_name='users/login.html'), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    # path("registration/", RegisterView.as_view(), name="registration"),
    # path("profile/", ProfileView.as_view(), name="profile"),
    # path('confirm/<str:code>/', confirm_user, name="confirm"),
    # path('restore_password/', ProfilePasswordRestoreView.as_view(), name="restore_password"),
]