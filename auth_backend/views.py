from rest_framework import generics
from .serializers import VendorSerializer, ListingSerializer
from .models import Vendor, Listing

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
