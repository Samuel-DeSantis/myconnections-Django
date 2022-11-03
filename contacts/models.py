from django.db import models
from phone_field import PhoneField

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def name(self):
        return self.first_name + ' ' + self.last_name

    def full_address(self):
        return self.address + ', ' + self.city + ', ' + self.state + ' ' + str(self.zip_code)


class Address(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField(max_length=5)
    country  = models.CharField(max_length=50)


class Communications(models.Model):
    email = models.EmailField(max_length=50)
    phone = modelsPhoneField(help_text='Contact phone number.')