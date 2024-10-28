from django.urls import path
from reserv_service.apps import ReservServiceConfig
from reserv_service.views import index, about_us, contacts, feedback, reservation_blank, OrderCreateView, \
    OrderDeleteView, OrderUpdateView, OrderDetailView, OrderListView, TableListView, our_service

app_name = ReservServiceConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('reservation_blank/', TableListView.as_view(), name='reservation_blank'),
    path('our_service', our_service, name='our_service'),

    path('order/list/', OrderListView.as_view(), name='order_list'),
    path('order/create/<int:pk>', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('order/detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/delete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),

]