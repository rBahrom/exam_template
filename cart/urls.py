from django.urls import path
from .views import card_view

urlpatterns = [
    path('cart/', card_view, name='cart')

]
