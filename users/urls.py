from django.urls import path
from .views import login_view, register_view, home_view, logout_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', home_view, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]
