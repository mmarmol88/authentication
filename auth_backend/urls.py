from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('listings/', views.ItemList.as_view(), name = 'item_list'),
    path('listings/<int:pk>', views.ItemDetail.as_view(), name = 'item_detail'),
    # path('listings/<int:pk>/edit/', views.ItemEdit.as_view(), name = 'item_edit'),
    # path('listings/<int:pk>/delete/', views.ItemDelete.as_view(), name = 'item_delete'),
    path('vendors/', views.VendorList.as_view(), name = 'vendor_list'),
    path('vendors/<int:pk>', views.VendorDetail.as_view(), name = 'vendor_detail'),
]