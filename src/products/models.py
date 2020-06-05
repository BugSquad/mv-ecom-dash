from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('a', 'active'),
    ('ia', 'inactive'),
)


class Product(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    vendor_id = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    badges = models.PositiveIntegerField()
    category_id = models.PositiveIntegerField()
    num_stock = models.PositiveIntegerField()
    num_views = models.PositiveIntegerField()
    num_purchases = models.PositiveIntegerField()
    num_added_cart = models.PositiveIntegerField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
