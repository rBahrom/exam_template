from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('users.urls')),
    path('', include('shop.urls')),
    path('', include('shopdetail.urls')),
    path('', include('contact.urls')),
    path('', include('cart.urls')),
    path('', include('chackout.urls')),
    path('', include('testimonial.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
