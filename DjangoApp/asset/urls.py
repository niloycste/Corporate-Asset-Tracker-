from django.urls import path
from . import views

urlpatterns = [
    path('api/employees/', views.EmployeeListAPIView.as_view(), name='employee-list'),
    path('api/employees/<int:pk>/', views.EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('api/companies/', views.CompanyListAPIView.as_view(), name='company-list'),
    path('api/companies/<int:pk>/', views.CompanyDetailAPIView.as_view(), name='company-detail'),
    path('api/assets/', views.AssetListAPIView.as_view(), name='asset-list'),
    path('api/assets/<int:pk>/', views.AssetDetailAPIView.as_view(), name='asset-detail'),
    path('api/devices/', views.DeviceListAPIView.as_view(), name='device-list'),
    path('api/devices/<int:pk>/', views.DeviceDetailAPIView.as_view(), name='device-detail'),
    path('api/delegates/', views.DelegateDeviceListAPIView.as_view(), name='delegate-device-list'),
    path('api/delegates/<int:pk>/', views.DelegateDeviceDetailAPIView.as_view(), name='delegate-device-detail'),
]
