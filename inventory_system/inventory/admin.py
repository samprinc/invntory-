
# Step 2: Admin Registration (inventory/admin.py)
from django.contrib import admin
from .models import Category, Product, Sale, InventoryLog

# Change site header and title
admin.site.site_header = "My Inventory Admin"
admin.site.site_title = "Inventory Admin Portal"
admin.site.index_title = "Welcome to the Inventory Dashboard"
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(InventoryLog)

