from django.shortcuts import render

from shop.models import Shop


# Create your views here.

def home(request):
    if request.method == 'POST':
        search = request.POST["search"]
        shopp = Shop.objects.filter(title__icontains=search)
        return render(request, 'home.html', {'shopp': shopp})
    shopp = Shop.objects.all()
    return render(request, 'home.html', {'shopp': shopp})
