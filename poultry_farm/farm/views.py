from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Vendor, Batch, Inventory, Customer, Order, Reward, Sale
from .serializers import VendorSerializer, BatchSerializer, InventorySerializer, CustomerSerializer, OrderSerializer, RewardSerializer, SaleSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def custom_api_root(request, format=None):
    return render(request, 'farm/api_root.html')

def vendors_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'farm/vendors_list.html', {'vendors': vendors})

def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'farm/vendor_detail.html', {'vendor': vendor})

def batch_detail(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    return render(request, 'farm/batch_detail.html', {'batch': batch})

def inventory_list(request):
    inventory = Inventory.objects.all()
    return render(request, 'farm/inventory_list.html', {'inventory': inventory})

def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    return render(request, 'farm/inventory_detail.html', {'inventory': inventory})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'farm/customers_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'farm/customer_detail.html', {'customer': customer})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'farm/orders_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'farm/order_detail.html', {'order': order})

def reward_list(request):
    rewards = Reward.objects.all()
    return render(request, 'farm/rewards_list.html', {'rewards': rewards})

def reward_detail(request, pk):
    reward = get_object_or_404(Reward, pk=pk)
    return render(request, 'farm/reward_detail.html', {'reward': reward})

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'farm/sales_list.html', {'sales': sales})

def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'farm/sale_detail.html', {'sale': sale})

# Django REST Framework viewsets

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
