from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.conf import settings

from payments.models import Item, Order, OrderItem
from payments.mixins import StripeCheckoutMixin
import stripe

stripe.api_key = settings.SECRET_KEY_STRIPE


class OrderCreateView(View):
    template_name = 'order_form.html'

    def get(self, request):
        items = Item.objects.all()
        return render(request, self.template_name, {'items': items})

    def post(self, request):
        selected_items = []
        for item in Item.objects.all():
            try:
                qty = int(request.POST.get(f"{item.id}_qty", 0))
            except ValueError:
                qty = 0
            if qty > 0:
                selected_items.append((item, qty))

        if not selected_items:
            messages.warning(request, "Выберите хотя бы один товар.")
            return redirect('payments:create_order')

        order = Order.objects.create()
        for item, qty in selected_items:
            OrderItem.objects.create(order=order, item=item, quantity=qty)

        order.calc_total()
        order.create_description()
        return redirect('payments:get_order', pk=order.id)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_key_stripe'] = settings.PUBLIC_KEY_STRIPE
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_key_stripe'] = settings.PUBLIC_KEY_STRIPE
        return context


class BuyItemView(View, StripeCheckoutMixin):
    def get(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        session = self.create_session(
            name=item.name,
            description=item.description,
            amount_cents=int(item.price * 100),
            quantity=1,
        )
        return JsonResponse({"session_id": session.id, "id": pk})


class BuyOrderView(View, StripeCheckoutMixin):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        items = order.items.all()
        session = self.create_session(
            name=f"Order {order}",
            description=", ".join(item.name for item in items),
            amount_cents=int(order.total_amount * 100),
            quantity=1,
        )
        return JsonResponse({"session_id": session.id, "id": pk})
