import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    productPK       = models.AutoField('Product PK', primary_key=True)
    product         = models.CharField('Product', null=False, blank=False, unique=True, max_length=20)
    image           = models.ImageField(upload_to='%y%m%d', height_field=None, width_field=None, max_length=100)
    
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
    
    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True
    
    def __str__(self):
        return self.product

class publicCode(models.Model):
    publicCodePK    = models.AutoField('Public Code PK', primary_key=True)
    publicCode      = models.BigIntegerField('Public Code', null=False, blank=False, unique=True)
    active          = models.BooleanField('Active', default=False, null=False, blank=False)
    product         = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.publicCode

class UserCode(models.Model):
    userCodePK      = models.AutoField('User Code PK', primary_key=True)
    userCode        = models.BigIntegerField('User Code', null=False, blank=False, unique=True)
    active          = models.BooleanField('Active', default=False, null=False, blank=False)
    product         = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.userCode

class State (models.Model):
    statePK         = models.AutoField('State PK', primary_key=True)
    state           = models.CharField('State', null=False, blank=False, unique=True, max_length=20)
    
    def __str__(self):
        return self.state

class City(models.Model):
    cityPK          = models.AutoField('City PK', primary_key=True)
    city            = models.CharField('City', null=False, blank=False, unique=True, max_length=30)
    state           = models.ForeignKey(State, null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.city
    
    class Meta:
        unique_together=(("city", "state"),)
    
class Pharmacy(models.Model):
    pharmacyPK      = models.AutoField('Pharmacy PK', primary_key=True)
    pharmacy        = models.CharField('Pharmacy', null=False, blank=False, unique=True, max_length=30)
    city            = models.ForeignKey(City, null=False, blank=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.pharmacy
    
    class Meta:
        unique_together=(("pharmacy", "city"),)
        
class Doctor(models.Model):
    doctorPK        = models.AutoField('Doctor PK', primary_key=True)
    doctor          = models.CharField('Doctor', null=False, blank=False, unique=True, max_length=30)
    city            = models.ForeignKey(City, null=False, blank=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.doctor
    
    class Meta:
        unique_together=(("doctor", "city"),)