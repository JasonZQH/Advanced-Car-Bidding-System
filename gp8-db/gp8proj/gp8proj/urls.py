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
    path('admin/', views.AdminListView.as_view(), name='admin-list'),
    path('admin/<int:pk>/', views.AdminDetailView.as_view(), name='admin-detail'),
    path('create-account/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    path('auction/', views.AuctionListView.as_view(), name='auction-list'),
    path('auction/<int:pk>/', views.AuctionDetailView.as_view(), name='auction-detail'),

    path('auctioncar/', views.AuctioncarListView.as_view(), name='auctioncar-list'),
    path('auctioncar/<int:pk>/', views.AuctioncarDetailView.as_view(), name='auctioncar-detail'),

    # Add similar patterns for other models...
    path('cars/', views.CarListView.as_view(), name='car-list'),

    path('car/<str:pk>/', views.CarDetailView.as_view(), name='car-detail'),

    # Continue adding paths for other models like Convertible, Electric, etc.
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
