from rest_framework import serializers
from .models import Admin, Auction, Auctioncar, Bid, Car, Convertible, Electric, Hybrid, Manage, Orders, Payment, Report, Suv, Sedan, Shipping, Transaction, Truck, Userfeedback, Userpreference, Users

import logging

logger = logging.getLogger(__name__)

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'
'''
class AuctioncarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auctioncar
        fields = '__all__'
'''
class BidSerializer(serializers.ModelSerializer):
    bid_id = serializers.IntegerField(required=False)
    class Meta:
        model = Bid
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Car
        fields = '__all__'

class AuctioncarSerializer(serializers.ModelSerializer):
    vin = CarSerializer(read_only=True)  # Assuming 'vin' is the related name for the Car model
    latest_bid = serializers.SerializerMethodField()
    # highest_bid = serializers.SerializerMethodField()
    class Meta:
        model = Auctioncar
        fields = ('vin','auction', 'unsold', 'reserve_price', 'start_bid', 'soldprice', 'latest_bid')
    
    def get_vin(self, obj):
        return str(obj.vin)  # Convert obj.vin to string

    def get_latest_bid(self, obj):
        print(f"Debug: obj.vin = {obj.vin}")
        latest_bid = Bid.objects.filter(vin=obj.vin).order_by('-bid_time').first()
        return latest_bid.bid_amount if latest_bid else None

    # def get_highest_bid(self, obj):
    #     print(f"Debug: obj.vin = {obj.vin}")
    #     highest_bid = Bid.objects.filter(vin=obj.vin).order_by('-bid_amount').first()
    #     return highest_bid.bid_amount if highest_bid else None

class ConvertibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convertible
        fields = '__all__'

class ElectricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electric
        fields = '__all__'

class HybridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hybrid
        fields = '__all__'

class ManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manage
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

class SedanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sedan
        fields = '__all__'

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class UserfeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userfeedback
        fields = '__all__'

class UserpreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userpreference
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['user_id', 'active_date']
