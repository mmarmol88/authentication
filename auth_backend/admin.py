from django.contrib import admin
from .models import Vendor, Listing
# Register your models here.
# admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Listing)
# admin.site.register(Transaction)