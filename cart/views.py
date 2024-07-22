from django.shortcuts import render

# Create your views here.


def card_view(request):
    return render(request, 'cart.html')
