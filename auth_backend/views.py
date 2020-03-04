from rest_framework import generics
from .serializers import UserSerializer, VendorSerializer, VendorSerializer, TransactionSerializer
from .models import User, Vendor, Listing, Transaction

# Create your views here.

# GET all listings
class ItemList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


# Retrieve/Update/Destroy listing
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

# GET all vendors
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


# Retrieve/Update/Destroy vendor
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
