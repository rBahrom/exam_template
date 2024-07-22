from django.urls import path
from .views import chackout_view

urlpatterns = [
    path('chackout/', chackout_view, name='chackout')

]
