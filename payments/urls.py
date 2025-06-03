from django.urls import path
from payments import views

app_name = 'payments'

urlpatterns = [
    path('buy/<int:pk>', views.BuyItemView.as_view(), name='buy_item'),
    path('buy-order/<int:pk>', views.BuyOrderView.as_view(), name='buy_order'),
    path('create-order/', views.OrderCreateView.as_view(), name='create_order'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='get_order'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='get_item')
]
