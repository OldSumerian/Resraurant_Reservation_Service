from django.urls import path
from reserv_service.apps import ReservServiceConfig
from reserv_service.views import index, about_us, contacts, feedback, reservation_blank, OrderCreateView, \
    OrderDeleteView, OrderUpdateView, OrderDetailView, OrderListView, TableListView

app_name = ReservServiceConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('reservation_blank/', TableListView.as_view(), name='reservation_blank'),

    path('order/list/', OrderListView.as_view(), name='order_list'),
    path('order/create/<int:pk>', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('order/detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/delete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),


    # path("reservations/", ReservationListView.as_view(), name="reservation_list"),
    # path("reservations/new/", ReservationCreateView.as_view(), name="reservation_create"),
    # path("reservations/<int:pk>/update/", ReservationUpdateView.as_view(), name="reservation_update"),
    # path("reservations/<int:pk>/delete/", ReservationDeleteView.as_view(), name="reservation_delete"),
    # path("", LoginView.as_view(template_name='users/login.html'), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    # path("registration/", RegisterView.as_view(), name="registration"),
    # path("profile/", ProfileView.as_view(), name="profile"),
    # path('confirm/<str:code>/', confirm_user, name="confirm"),
    # path('restore_password/', ProfilePasswordRestoreView.as_view(), name="restore_password"),
]