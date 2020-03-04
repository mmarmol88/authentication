from rest_framework import serializers
from .models import User, Vendor, Listing

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ('id', 'name', 'email', 'street', 'city', 'state', 'zip_code', 'phone_number',)

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    listings = serializers.HyperlinkedRelatedField(
        view_name='listing_detail',
        many=True,
        read_only=True
    )
    class Meta: 
        model = Vendor
        fields = ('id', 'name', 'vendor_type', 'email', 'street', 'city', 'state', 'zip_code', 'phone_number', 'description', 'closing_time',)

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    vendor = serializers.HyperlinkedRelatedField(
        view_name='vendor_detail',
        many=False,
        read_only=True
    )
    class Meta: 
        model = Listing
        fields = ('id', 'name', 'price', 'quantity', 'description', 'vegetarian', 'vegan',)

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=False,
        read_only=True
    )
    class Meta: 
        model = Transaction
        fields = ('id', 'user_id', 'total',)
