from rest_framework import generics
from .models import Employee, Company, Asset, Device, DelegateDevice
from .serializers import EmployeeSerializer, CompanySerializer, AssetSerializer, DeviceSerializer, DelegateDeviceSerializer

class EmployeeListAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AssetListAPIView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class DeviceListAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DelegateDeviceListAPIView(generics.ListCreateAPIView):
    queryset = DelegateDevice.objects.all()
    serializer_class = DelegateDeviceSerializer

class DelegateDeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DelegateDevice.objects.all()
    serializer_class = DelegateDeviceSerializer
