from django import forms

from reserv_service.models import Order, Table


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_time']

    def __init__(self, *args, **kwargs):
        table_pk = kwargs.pop('table_pk')
        super().__init__(*args, **kwargs)
        self.fields['order_time'].queryset = Table.objects.get(pk=table_pk).times.all()
