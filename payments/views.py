from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from payments.models import Item
import stripe
from django.conf import settings

stripe.api_key = settings.SECRET_KEY_STRIPE

def get_item(request, pk):
    item = get_object_or_404(Item, id=pk)
    context = {
        'item': item,
        'public_key_stripe': settings.PUBLIC_KEY_STRIPE
    }
    return render(request, 'item.html', context=context)

def buy_item(request, pk):
    item = get_object_or_404(Item, id=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
            }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel'
    )
    return JsonResponse({'session_id': session.id, 'id': pk})    