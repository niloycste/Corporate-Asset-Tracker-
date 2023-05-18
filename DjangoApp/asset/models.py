from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(Employee, related_name='companies')

    def __str__(self):
        return self.name

    
    
class Device(models.Model):
      name = models.CharField(max_length=255)
      condition = models.CharField(max_length=255)
      asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
      checked_out_at = models.DateTimeField(null=True, blank=True)
      checked_in_at = models.DateTimeField(null=True, blank=True)

      def __str__(self):
        return self.name
      

class Asset(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='assets')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_assets')
    checked_out_at = models.DateTimeField(null=True, blank=True)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class DelegateDevice(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    delegation_date = models.DateTimeField(auto_now_add=True)

    

