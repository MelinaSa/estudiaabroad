from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('favicon.ico/', RedirectView.as_view(url=settings.STATIC_URL + 'web_estudia/assets/img/favicon.ico')),
    path('android-chrome-192x192.png/', RedirectView.as_view(url=settings.STATIC_URL + 'web_estudia/assets/img/android-chrome-192x192.png')),
    path('android-chrome-512x512.png/', RedirectView.as_view(url=settings.STATIC_URL + 'web_estudia/assets/img/android-chrome-512x512.png')),
    path('apple-touch-icon.png/', RedirectView.as_view(url=settings.STATIC_URL + 'apple-touch-icon.png')),
]
