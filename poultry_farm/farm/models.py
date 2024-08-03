from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    average_hatch_rate = models.FloatField()

    def __str__(self):
        return self.name

class Batch(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    hatch_date = models.DateField()

    def __str__(self):
        return f'Batch from {self.vendor.name} on {self.hatch_date}'

class Inventory(models.Model):
    day_old = models.IntegerField()
    week_old = models.IntegerField()
    twenty_one_day_old = models.IntegerField()

    def __str__(self):
        return f'Inventory on {self.id}'

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'Order by {self.customer.name} on {self.order_date}'

class Reward(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reward_points = models.IntegerField()

    def __str__(self):
        return f'Reward for {self.customer.name}'

class Sale(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateField()

    def __str__(self):
        return f'Sale on {self.sale_date}'
