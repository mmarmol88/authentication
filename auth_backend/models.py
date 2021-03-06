from django.db import models

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=250,unique=True)
#     password = models.CharField(max_length=40)# min_length=8 in frontEnd
#     street = models.CharField(max_length=200)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=2)
#     zip_code = models.CharField(max_length=5)
#     phone_number = models.CharField(max_length=10)



class Vendor(models.Model):
    name = models.CharField(max_length=50)
    vendor_type = models.CharField(max_length=20)
    email = models.CharField(max_length=250,unique=True)
    password = models.CharField(max_length=40) #min_length=8 in frontEnd
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2) #min_length=2
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    description = models.TextField()
    closing_time = models.CharField(max_length=10)
    

class Listing(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    description = models.TextField()
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='listings')

# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions' )
#     total = models.DecimalField(max_digits=5, decimal_places=2)

# this.state = {
#      bag: {
#          listings: [{ name, price, quantity }, {}],
#          subtotal: num,
#          total: subtotal + subtotal x tax
#      }
# }