from rest_framework import generics
from .models import (Admin, Auction, Auctioncar, Bid, Car, Convertible, Electric, Hybrid, Manage, Orders, Payment, Report, Suv, Sedan, Shipping, Transaction, Truck, Userfeedback, Userpreference, Users)
from .serializers import (AdminSerializer, AuctionSerializer, AuctioncarSerializer, BidSerializer, CarSerializer, ConvertibleSerializer, ElectricSerializer, HybridSerializer, ManageSerializer, OrdersSerializer, PaymentSerializer, ReportSerializer, SuvSerializer, SedanSerializer, ShippingSerializer, TransactionSerializer, TruckSerializer, UserfeedbackSerializer, UserpreferenceSerializer, UsersSerializer)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users

class UserView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

# For example, Car Views
class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Admin Views
class AdminListView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class AdminDetailView(generics.RetrieveAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

# Auction Views
class AuctionListView(generics.ListAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class AuctionDetailView(generics.RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

# Auctioncar Views
class AuctioncarListView(generics.ListAPIView):
    queryset = Auctioncar.objects.all()
    serializer_class = AuctioncarSerializer

class AuctioncarDetailView(generics.RetrieveAPIView):
    queryset = Auctioncar.objects.all()
    serializer_class = AuctioncarSerializer

# Add similar views for other models...

# Continue with views for Convertible, Electric, etc.

@api_view(['POST'])
def create_account(request):
    # Your logic for creating a user
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    phone_number = request.data.get('phone_number')
    try:
        # Try to get the user by email and phone number
        user = Users.objects.get(email=email, phone_number=phone_number)
        # Serialize the user info to return
        user_info_serializer = UsersSerializer(user)
        return Response(user_info_serializer.data)
    except Users.DoesNotExist:
        # If the user doesn't exist, return an error
        return Response({'message': 'Invalid email or phone number'}, status=status.HTTP_404_NOT_FOUND)