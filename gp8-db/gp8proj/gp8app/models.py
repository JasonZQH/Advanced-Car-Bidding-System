# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    adminid = models.IntegerField(db_column='AdminID', blank=True, null=True)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', max_length=11, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
    #     managed = False
        db_table = 'ADMIN'


class User(models.Model):
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    # userid = models.IntegerField(blank=True, null=True)
    fname = models.CharField(db_column='Fname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.
    # gender = models.CharField(max_length=6, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seller = models.IntegerField(db_column='Seller', blank=True, null=True)  # Field name made lowercase.
    bidder = models.IntegerField(db_column='Bidder', blank=True, null=True)  # Field name made lowercase.
    privacypreference = models.CharField(db_column='PrivacyPreference', max_length=100, blank=True, null=True)  # Field name made lowercase.
    acitivedate = models.DateField(db_column='AcitiveDate', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zip = models.IntegerField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.

    class Meta:
    #     managed = False
        db_table = 'USER'
