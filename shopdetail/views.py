from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shop.models import Shop

# Create your views here.

@login_required
def shop_detail_view(request):
    return render(request, 'shopdetail.html')
