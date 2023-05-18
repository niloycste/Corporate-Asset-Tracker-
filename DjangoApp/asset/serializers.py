from rest_framework import serializers
from .models import Employee, Company, Asset, Device, DelegateDevice

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'name', 'asset_type', 'company', 'employee', 'checked_in_at','checked_out_at', )


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'condition', 'asset_type','checked_in_at', 'checked_out_at', )


class DelegateDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelegateDevice
        fields = ('id', 'asset', 'device', 'employee', 'delegation_date')

