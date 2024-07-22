from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Shop

# Create your views here.

@login_required()
def shop_view(request):
    if request.method == 'POST':
        search = request.POST["search"]
        shopp = Shop.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'shopp': shopp})
    shopp = Shop.objects.all()
    return render(request, 'shop.html', {'shopp': shopp})

@login_required()
def detail_view(request, id):
    blog = Shop.objects.get(id=id)
    return render(request, 'detail.html', {'blog': blog})
