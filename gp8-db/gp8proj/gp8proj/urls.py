"""
URL configuration for gp8proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gp8app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/create-account/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    path('cars/', views.CarListView.as_view(), name='car-list'),
    path('admin-login/', views.admin_login, name='admin-login'),
    path('add-car/', views.add_car, name='add-car'),
    path('api/auction/<str:vin>/', views.auction_cars, name='auction_cars'),
    path('api/bid/', views.submit_bid, name='submit_bid'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
