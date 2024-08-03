from django.test import TestCase
from .models import Vendor, Batch, Inventory, Customer, Order, Reward, Sale

class ModelTests(TestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(name="Test Vendor", contact_info="Contact Info", average_hatch_rate=75.0)
        self.customer = Customer.objects.create(name="Test Customer", contact_info="Customer Contact Info")
        self.batch = Batch.objects.create(vendor=self.vendor, quantity=100, hatch_date="2024-01-01")
        self.inventory = Inventory.objects.create(day_old=70, week_old=50, twenty_one_day_old=30)
        self.order = Order.objects.create(customer=self.customer, order_date="2024-01-01", quantity=100)
        self.reward = Reward.objects.create(customer=self.customer, reward_points=10)
        self.sale = Sale.objects.create(inventory=self.inventory, quantity=70, sale_date="2024-01-01")

    def test_vendor_creation(self):
        self.assertEqual(self.vendor.name, "Test Vendor")

    def test_batch_creation(self):
        self.assertEqual(self.batch.quantity, 100)

    def test_inventory_creation(self):
        self.assertEqual(self.inventory.day_old, 70)

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "Test Customer")

    def test_order_creation(self):
        self.assertEqual(self.order.quantity, 100)

    def test_reward_creation(self):
        self.assertEqual(self.reward.reward_points, 10)

    def test_sale_creation(self):
        self.assertEqual(self.sale.quantity, 70)
