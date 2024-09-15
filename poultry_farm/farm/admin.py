from django.contrib.admin import AdminSite, ModelAdmin
from .models import Vendor, Batch, Inventory, Customer, Order, Reward, Sale

class MyAdminSite(AdminSite):
    site_header = 'Poultry Farm Management Admin'
    site_title = 'Poultry Farm Management'
    index_title = 'Admin Dashboard'

admin_site = MyAdminSite(name='myadmin')

class VendorAdmin(ModelAdmin):
    list_display = ('name', 'contact_info', 'email', 'average_hatch_rate')
    search_fields = ('name', 'email')
    list_filter = ('name',)

class BatchAdmin(ModelAdmin):
    list_display = ('batch_number', 'vendor', 'date_received', 'quantity', 'hatch_date')
    search_fields = ('batch_number', 'vendor')
    list_filter = ('date_received',)

class InventoryAdmin(ModelAdmin):
    list_display = ('day_old', 'week_old', 'twenty_one_day_old', 'last_updated')
    search_fields = ('day_old', 'week_old', 'twenty_one_day_old')
    list_filter = ('last_updated',)

class CustomerAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_info', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name',)

class OrderAdmin(ModelAdmin):
    list_display = ('order_number', 'customer', 'order_date', 'quantity')
    search_fields = ('order_number', 'customer')
    list_filter = ('order_date',)

class RewardAdmin(ModelAdmin):
    list_display = ('customer', 'reward_points', 'reward_date', 'expiry_date', 'remaining_reward_points')
    search_fields = ('customer', 'reward_points')
    list_filter = ('reward_date',)

class SaleAdmin(ModelAdmin):
    list_display = ('sale_number', 'customer', 'sale_date', 'quantity')
    search_fields = ('sale_number', 'customer')
    list_filter = ('sale_date',)

# Register the models with the custom admin site
admin_site.register(Vendor, VendorAdmin)
admin_site.register(Batch, BatchAdmin)
admin_site.register(Inventory, InventoryAdmin)
admin_site.register(Customer, CustomerAdmin)
admin_site.register(Order, OrderAdmin)
admin_site.register(Reward, RewardAdmin)
admin_site.register(Sale, SaleAdmin)