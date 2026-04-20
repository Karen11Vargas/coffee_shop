from decimal import Decimal
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls     import reverse_lazy
from .models import Orders
from .forms import OrderProductForm


class MyOrderView(LoginRequiredMixin,DetailView):
    model = Orders
    template_name = 'orders/my_order.html'
    context_object_name = 'order'

    def get_object(self):
        order = Orders.objects.filter(is_active=True, user = self.request.user).first()
        if not order:
            raise Http404("No hay una orden activa.")
        return order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.object

        subtotal = Decimal("0.00")
        order_items = order.orderproduct_set.all()

        for item in order_items:
            item.subtotal_item = item.product.price * item.quantity
            subtotal += item.subtotal_item

        igv = subtotal * Decimal("0.18")
        total_order = subtotal + igv

        context['order_items'] = order_items
        context['subtotal'] = subtotal
        context['igv'] = igv
        context['total_order'] = total_order

        return context


class CreateOrderProductView(LoginRequiredMixin,CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('my_order')

    def form_valid(self, form):
        order, created = Orders.objects.get_or_create(
            is_active = True,
            user = self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
