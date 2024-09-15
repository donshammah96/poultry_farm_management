from django.db import models
import datetime
import uuid

def generate_default_batch_number():
    return str(uuid.uuid4())

def generate_default_order_number():
    return str(uuid.uuid4())    

def generate_default_sale_number():
    return str(uuid.uuid4())

def generate_default_expiry_date():
    return datetime.date.today() + datetime.timedelta(days=30)

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField(default='')
    email = models.EmailField(default='')
    average_hatch_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Batch(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=50, default=generate_default_batch_number)  
    date_received = models.DateField(default=datetime.date.today)
    quantity = models.IntegerField(default=0)
    hatch_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'Batch from {self.vendor.name} on {self.hatch_date}'

class Inventory(models.Model):
    day_old = models.IntegerField(default=0)
    week_old = models.IntegerField(default=0)
    twenty_one_day_old = models.IntegerField(default=0)
    last_updated = models.DateField(default=datetime.date.today)   

    def __str__(self):
        return f'Inventory on {self.id}'

class Customer(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    contact_info = models.TextField(default='')
    email = models.EmailField(default='')

    def __str__(self):
        return self.first_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    order_number = models.CharField(max_length=50, default=generate_default_order_number)
    order_date = models.DateField(default=datetime.date.today)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'Order by {self.customer.first_name} on {self.order_date}'

class Reward(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reward_points = models.IntegerField(default=0)
    reward_date = models.DateField(default=datetime.date.today)
    expiry_date = models.DateField(default=generate_default_expiry_date)
    remaining_reward_points = models.IntegerField(default=0)

    def __str__(self):
        return f'Reward for {self.customer.first_name}'

class Sale(models.Model):
    sale_number = models.CharField(max_length=50, default=generate_default_sale_number)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=0)
    sale_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'Sale on {self.sale_date}'
