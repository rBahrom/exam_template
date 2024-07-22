from django.shortcuts import render

# Create your views here.


def testimonial_view(request):
    return render(request, 'testimonial.html')
