from django.urls import path

from .views import testimonial_view

urlpatterns = [
    path('testimonial/', testimonial_view, name='testimonial'),

]