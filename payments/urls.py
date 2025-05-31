from django.urls import path
from payments.views import buy_item, get_item

app_name = 'payments'

urlpatterns = [
    path('buy/<int:pk>', buy_item, name='buy_item'),
    path('item/<int:pk>', get_item, name='get_item')
]
