import stripe
from django.conf import settings

stripe.api_key = settings.SECRET_KEY_STRIPE

class StripeCheckoutMixin:
    def create_session(self, *, name, description, amount_cents, quantity=1):
        return stripe.checkout.Session.create(
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": name,
                        "description": description,
                    },
                    "unit_amount": amount_cents,
                },
                "quantity": quantity,
            }],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
