import datetime

from django.db import models
from django.utils import timezone
from django.db.models.fields import BigIntegerField

# Create your models here.

class Product(models.Model):
    productPK   = models.AutoField('Product PK', primary_key=True)
    product     = models.CharField('Product', null=False, blank=False, unique=True, max_length=20)        
    
    def __str__(self):
        return self.product

class publicCode(models.Model):
    publicCodePK    = models.AutoField('Public Code PK', primary_key=True)
    publicCode      = models.BigIntegerField('Public Code', null=False, blank=False, unique=True)
    active          = models.BooleanField('Active', default=False, null=False, blank=False)
    productFK       = models.ForeignKey('Product', Product)
    
    def __str__(self):
        return self.publicCode

class UserCode(models.Model):
    userCodePK  = models.AutoField('User Code PK', primary_key=True)
    userCode    = models.BigIntegerField('User Code', null=False, blank=False, unique=True)
    active      = models.BooleanField('Active', default=False, null=False, blank=False)
    productFK   = models.ForeignKey('Product', Product)
    
    def __str__(self):
        return self.userCode

class State (models.Model):
    statePK     = models.AutoField('State PK', primary_key=True)
    state       = models.CharField('State', null=False, blank=False, unique=True, max_length=20)
    
    def __str__(self):
        return self.state

class City(models.Model):
    cityPK      = models.AutoField('City PK', primary_key=True)
    city        = models.CharField('City', null=False, blank=False, unique=True, default='city', max_length=30)
    stateFK     = models.ForeignKey('State', State)

    def __str__(self):
        return self.city
    
    class Meta:
        unique_together=(("city", "stateFK"),)
    
class Pharmacy(models.Model):
    pharmacyPK      = models.AutoField('Pharmacy PK', primary_key=True)
    pharmacy        = models.CharField('Pharmacy', null=False, blank=False, unique=True, max_length=30)
    cityFK          = models.ForeignKey('City', City)
    
    def __str__(self):
        return self.pharmacy
    
    class Meta:
        unique_together=(("pharmacy", "cityFK"),)
        
class Doctor(models.Model):
    doctorPK        = models.AutoField('Doctor PK', primary_key=True)
    doctor          = models.CharField('Doctor', null=False, blank=False, unique=True, max_length=30)
    cityFK          = models.ForeignKey('City', City)
    
    def __str__(self):
        return self.doctor
    
    class Meta:
        unique_together=(("doctor", "cityFK"),)