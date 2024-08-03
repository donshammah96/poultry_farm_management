from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    average_hatch_rate = models.FloatField()

    def __str__(self):
        return self.name

class Batch(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    eggs_received = models.IntegerField()
    hatch_date = models.DateField()
    hatch_rate = models.FloatField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Batch {self.id} from {self.vendor.name}"

class Inventory(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    day_old_chicks = models.IntegerField()
    week_old_chicks = models.IntegerField()
    twenty_one_day_old_chicks = models.IntegerField()
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"Inventory for Batch {self.batch.id}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    total_orders = models.IntegerField(default=0)
    rewards_earned = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    day_old_chicks = models.IntegerField()
    week_old_chicks = models.IntegerField()
    twenty_one_day_old_chicks = models.IntegerField()
    total_chicks = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

class Reward(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reward_date = models.DateField()
    reward_amount = models.IntegerField()

    def __str__(self):
        return f"Reward {self.id} for {self.customer.name}"

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField()
    total_amount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    receipt_number = models.CharField(max_length=100)

    def __str__(self):
        return f"Sale {self.id} by {self.customer.name}"
