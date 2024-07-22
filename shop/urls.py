from django.urls import path

from .views import shop_view, detail_view

urlpatterns = [
    path('shop/', shop_view, name='shop'),
    path('shopdetail/<int:id>/', detail_view, name='shopdetail'),

]
