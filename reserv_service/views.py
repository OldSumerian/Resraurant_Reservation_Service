from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from reserv_service.forms import OrderForm
from reserv_service.models import Order, Table


def index(request):
    return render(request,'reserv_service/index.html')


def about_us(request):
    return render(request,'reserv_service/about_us.html')


def contacts(request):
    return render(request,'reserv_service/contacts.html')


def feedback(request):
    return render(request,'reserv_service/feedback_form.html')


def reservation_blank(request):
    return render(request,'reserv_service/reservation_blank.html')


def our_service(request):
    return render(request,'reserv_service/our_service.html')

class TableListView(ListView):
    model = Table
    template_name = 'reserv_service/reservation_blank.html'
    paginate_by = 4


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('reserv_service:reservation_blank')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'table_pk': self.kwargs.get('pk')})
        return kwargs

    def form_valid(self, form): # доработать
        order = form.save()
        order.user = self.request.user
        times_used = order.order_time.all()
        used_table = Table.objects.get(pk=self.kwargs.get('pk'))
        times_table = used_table.times.all()
        used_table.times.set(times_table.difference(times_used))
        used_table.save()
        order.save()
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('reserv_service:order_list') ####


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['user', 'table', 'order_time']
    success_url = reverse_lazy('reserv_service:order_list') ####


class OrderListView(ListView):
    model = Order
    paginate_by = 3
    template_name = 'users:my_cabinet'


class OrderDetailView(DetailView):
    model = Order


