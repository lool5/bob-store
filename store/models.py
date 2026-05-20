from django.db import models


class Product(models.Model):

    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        help_text="نسبة التخفيض % (0 = لا يوجد تخفيض)"
    )
    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (100 - self.discount) / 100
        return self.price


    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='products/'
    )

    def __str__(self):

        return self.name


class Order(models.Model):

    SIZE_CHOICES = [

        ('S', 'Small'),

        ('M', 'Medium'),

        ('L', 'Large'),

        ('XL', 'XL'),

        ('2XL', '2XL'),

        ('3XL', '3XL'),
    ]


    STATUS_CHOICES = [

        ('pending', 'Under Review'),

        ('confirmed', 'Confirmed'),

        ('sold', 'Sold'),

        ('cancelled', 'Cancelled'),
    ]


    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    customer_phone = models.CharField(
        max_length=20
    )

    customer_address = models.TextField(
        null=True,
        blank=True
    )

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.customer_phone

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200, blank=True, help_text="نص بديل للصورة")
    order = models.PositiveIntegerField(default=0, help_text="ترتيب الصورة (الأصغر أولاً)")

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"صورة لـ {self.product.name}"