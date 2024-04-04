from rest_framework import generics
from .models import (Admin, Auction, Auctioncar, Bid, Car, Convertible, Electric, Hybrid, Manage, Orders, Payment, Report, Suv, Sedan, Shipping, Transaction, Truck, Userfeedback, Userpreference, Users)
from .serializers import (AdminSerializer, AuctionSerializer, AuctioncarSerializer, BidSerializer, CarSerializer, ConvertibleSerializer, ElectricSerializer, HybridSerializer, ManageSerializer, OrdersSerializer, PaymentSerializer, ReportSerializer, SuvSerializer, SedanSerializer, ShippingSerializer, TransactionSerializer, TruckSerializer, UserfeedbackSerializer, UserpreferenceSerializer, UsersSerializer)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users



# show all cars
class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


#create acc
@api_view(['POST'])
def create_account(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# user login
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
    
# admin login
@api_view(['POST'])
def admin_login(request):
    admin_id = request.data.get('admin_id')
    password = request.data.get('password')
    if admin_id and password:
        admin = Manage.objects.filter(admin_id=admin_id, password=password).first()
        if admin:
            return Response({'message': 'Login successful', 'admin_id': admin.admin_id})
        else:
            return Response({'message': 'Invalid Admin ID or password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Missing Admin ID or password'}, status=status.HTTP_400_BAD_REQUEST)
    

# car upload
@api_view(['POST'])
def add_car(request):
    car_data = request.data.copy()
    car_type = car_data.pop('car_type', None)
    image = request.FILES.get('image', None)

    try:
        car = Car.objects.create(**car_data)
        if image:
            car.image.save(image.name, image, save=True)  # Save the image field
        if car_type == 'Convertible':
            Convertible.objects.create(vin=car)
        elif car_type == 'Electric':
            Electric.objects.create(vin=car)
        elif car_type == 'Hybrid':
            Hybrid.objects.create(vin=car)
        elif car_type == 'SUV':
            Suv.objects.create(vin=car)
        elif car_type == 'Sedan':
            Sedan.objects.create(vin=car)
        elif car_type == 'Truck':
            Truck.objects.create(vin=car)
        return Response({'message': 'Car added successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


