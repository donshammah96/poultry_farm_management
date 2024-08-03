from django.contrib import admin
from .models import Vendor, Batch, Inventory, Customer, Order, Reward, Sale

admin.site.register(Vendor)
admin.site.register(Batch)
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Reward)
admin.site.register(Sale)
