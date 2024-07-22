from django.urls import path

from .views import shop_detail_view

urlpatterns = [
    path('shopdetail/', shop_detail_view, name='shopdetail'),
]
