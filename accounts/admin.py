from django.contrib import admin

from .models import Customer, Tag
from .models import Order
from .models import Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
