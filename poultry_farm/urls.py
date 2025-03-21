"""
URL configuration for poultry_farm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from farm import views


router = DefaultRouter()
router.register(r'vendors', views.VendorViewSet)
router.register(r'batches', views.BatchViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'rewards', views.RewardViewSet)
router.register(r'sales', views.SaleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Template views
    path('vendors/', views.vendors_list, name='vendors_list'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('batches/<int:pk>/', views.batch_detail, name='batch_detail'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('rewards/', views.reward_list, name='reward_list'),
    path('rewards/<int:pk>/', views.reward_detail, name='reward_detail'),
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/<int:pk>/', views.sale_detail, name='sale_detail'),
]
