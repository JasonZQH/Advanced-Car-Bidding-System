# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

def get_current_date():
    return timezone.now().date()


class Admin(models.Model):
    admin_id = models.IntegerField(db_column='Admin_ID', primary_key=True)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', unique=True, max_length=11)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    birthdate = models.DateField(db_column='Birthdate')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Admin'


class Auction(models.Model):
    auction_id = models.IntegerField(db_column='Auction_ID', primary_key=True)  # Field name made lowercase.
    auction_status = models.CharField(db_column='Auction_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='Start_Time', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='End_Time', blank=True, null=True)  # Field name made lowercase.
    auction_period = models.IntegerField(db_column='Auction_Period', blank=True, null=True)  # Field name made lowercase.
    attend_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='Attend_User_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Auction'


class Auctioncar(models.Model):
    auction = models.ForeignKey(Auction, models.DO_NOTHING, db_column='Auction_id', blank=True, null=True)  # Field name made lowercase.
    vin = models.ForeignKey('Car', models.DO_NOTHING, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    unsold = models.IntegerField(db_column='Unsold', blank=True, null=True)  # Field name made lowercase.
    reserve_price = models.DecimalField(db_column='Reserve_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    start_bid = models.DecimalField(db_column='Start_Bid', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soldprice = models.DecimalField(db_column='SoldPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'AuctionCar'


class Bid(models.Model):
    bid_id = models.IntegerField(db_column='Bid_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    auction = models.ForeignKey(Auction, models.DO_NOTHING, db_column='Auction_ID', blank=True, null=True)  # Field name made lowercase.
    bid_amount = models.DecimalField(db_column='Bid_Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bid_time = models.DateTimeField(db_column='Bid_Time', blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=17, blank=True, null=True)  # Field name made lowercase.
    bidwin = models.IntegerField(db_column='BIDWIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Bid'


class Car(models.Model):
    vin = models.CharField(db_column='VIN', primary_key=True, max_length=17)
    exterior_color = models.CharField(db_column='Exterior_Color', max_length=255, blank=True, null=True)
    interior_color = models.CharField(db_column='Interior_Color', max_length=255, blank=True, null=True)
    make = models.CharField(db_column='Make', max_length=255, blank=True, null=True)
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)
    fuel = models.CharField(db_column='Fuel', max_length=255, blank=True, null=True)
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    list_time = models.DateTimeField(db_column='List_Time', blank=True, null=True)
    list_price = models.DecimalField(db_column='List_Price', max_digits=10, decimal_places=2, blank=True, null=True)
    current_mileage = models.IntegerField(db_column='Current_Mileage', blank=True, null=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    class Meta:
        managed = True  # Change this to True if you want Django to manage the table schema.
        db_table = 'Car'


class Convertible(models.Model):
    vin = models.OneToOneField(Car, models.DO_NOTHING, db_column='VIN', primary_key=True)  # Field name made lowercase.
    canopymaterial = models.CharField(db_column='CanopyMaterial', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Convertible'


class Electric(models.Model):
    vin = models.OneToOneField(Car, models.DO_NOTHING, db_column='VIN', primary_key=True)  # Field name made lowercase.
    electric_range = models.IntegerField(db_column='Electric_Range', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Electric'
 

class Hybrid(models.Model):
    vin = models.OneToOneField(Car, models.DO_NOTHING, db_column='VIN', primary_key=True)  # Field name made lowercase.
    fuel_range = models.IntegerField(db_column='Fuel_Range', blank=True, null=True)  # Field name made lowercase.
    electric_range = models.IntegerField(db_column='Electric_Range', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Hybrid'


class Manage(models.Model):
    admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='Admin_ID', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Manage'


class Orders(models.Model):
    order_id = models.IntegerField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    bidder = models.ForeignKey('Users', models.DO_NOTHING, db_column='Bidder', blank=True, null=True)  # Field name made lowercase.
    seller = models.ForeignKey('Users', models.DO_NOTHING, db_column='Seller', related_name='orders_seller_set', blank=True, null=True)  # Field name made lowercase.
    o_price = models.DecimalField(db_column='O_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_Method', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=17, blank=True, null=True)  # Field name made lowercase.
    auction = models.ForeignKey(Auction, models.DO_NOTHING, db_column='Auction_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Orders'


class Payment(models.Model):
    payment_id = models.IntegerField(db_column='Payment_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_Method', max_length=255, blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='Payment_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Payment'


class Report(models.Model):
    report_id = models.IntegerField(db_column='Report_ID', primary_key=True)  # Field name made lowercase.
    vin = models.ForeignKey(Car, models.DO_NOTHING, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    detail_history = models.TextField(db_column='Detail_History', blank=True, null=True)  # Field name made lowercase.
    owner_history = models.TextField(db_column='Owner_History', blank=True, null=True)  # Field name made lowercase.
    title_history = models.TextField(db_column='Title_History', blank=True, null=True)  # Field name made lowercase.
    additional_history = models.TextField(db_column='Additional_History', blank=True, null=True)  # Field name made lowercase.
    history_mileage = models.IntegerField(db_column='History_Mileage', blank=True, null=True)  # Field name made lowercase.
    owner_count = models.IntegerField(db_column='Owner_Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Report'


class Suv(models.Model):
    vin = models.OneToOneField(Car, models.DO_NOTHING, db_column='VIN', primary_key=True)  # Field name made lowercase.
    seatnumber = models.IntegerField(db_column='SeatNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SUV'


class Sedan(models.Model):
    vin = models.OneToOneField(Car, models.DO_NOTHING, db_column='VIN', primary_key=True)  # Field name made lowercase.
    seatnumber = models.IntegerField(db_column='SeatNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Sedan'


class Shipping(models.Model):
    tracking_number = models.CharField(db_column='Tracking_Number', primary_key=True, max_length=255)  # Field name made lowercase.
    shipping_method = models.CharField(db_column='Shipping_Method', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipping_status = models.CharField(db_column='Shipping_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    car_vin = models.ForeignKey(Car, models.DO_NOTHING, db_column='Car_VIN', blank=True, null=True)  # Field name made lowercase.
    user_id_track = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID_Track', blank=True, null=True)  # Field name made lowercase.
    approved_payment = models.ForeignKey(Payment, models.DO_NOTHING, db_column='Approved_Payment_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Shipping'


class Transaction(models.Model):
    payment = models.ForeignKey(Payment, models.DO_NOTHING, db_column='Payment_ID', blank=True, null=True)  # Field name made lowercase.
    order = models.ForeignKey(Orders, models.DO_NOTHING, db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    transaction_id = models.IntegerField(db_column='Transaction_ID', primary_key=True)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_Method', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    transaction_amount = models.DecimalField(db_column='Transaction_Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Transaction'


class Truck(models.Model):
    vin = models.OneToOneField(Car, models.DO_NOTHING, db_column='VIN', primary_key=True)  # Field name made lowercase.
    boatload = models.IntegerField(db_column='BoatLoad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Truck'


class Userfeedback(models.Model):
    case_id = models.IntegerField(db_column='Case_ID', primary_key=True)  # Field name made lowercase.
    feedback = models.CharField(db_column='Feedback', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    providefb_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='ProvideFB_User_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserFeedback'


class Userpreference(models.Model):
    preferenceid = models.IntegerField(db_column='PreferenceID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    allowed_sharing_info = models.IntegerField(db_column='Allowed_Sharing_Info', blank=True, null=True)  # Field name made lowercase.
    allowed_reciving_adv = models.IntegerField(db_column='Allowed_Reciving_ADV', blank=True, null=True)  # Field name made lowercase.
    allowed_sending_email = models.IntegerField(db_column='Allowed_Sending_Email', blank=True, null=True)  # Field name made lowercase.
    allowed_sending_text = models.IntegerField(db_column='Allowed_Sending_text', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserPreference'


class Users(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Auto-generated primary key
    email = models.CharField(db_column='Email', unique=True, max_length=255, blank=True, null=True)
    phone_number = models.CharField(db_column='Phone_Number', max_length=20, blank=True, null=True)
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    lastn = models.CharField(db_column='LastN', max_length=255, blank=True, null=True)
    firstn = models.CharField(db_column='FirstN', max_length=255, blank=True, null=True)
    seller = models.BooleanField(db_column='Seller', default=False)  # Boolean field with default False
    bidder = models.BooleanField(db_column='Bidder', default=False)  # Boolean field with default False
    active_date = models.DateField(db_column='Active_Date', default=get_current_date)  # Default to current date
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)
    zip = models.CharField(db_column='ZIP', max_length=20, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Users'