from rest_framework import generics
from .models import (Admin, Auction, Auctioncar, Bid, Car, Convertible, Electric, Hybrid, Manage, Orders, Payment, Report, Suv, Sedan, Shipping, Transaction, Truck, Userfeedback, Userpreference, Users)
from .serializers import (AdminSerializer, AuctionSerializer, AuctioncarSerializer, BidSerializer, CarSerializer, ConvertibleSerializer, ElectricSerializer, HybridSerializer, ManageSerializer, OrdersSerializer, PaymentSerializer, ReportSerializer, SuvSerializer, SedanSerializer, ShippingSerializer, TransactionSerializer, TruckSerializer, UserfeedbackSerializer, UserpreferenceSerializer, UsersSerializer)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from django.core.exceptions import ValidationError
import traceback
from django.utils import timezone
from django.db.models import Max



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
    print("Request Data:", request.data)
    print("Request Files:", request.FILES)

    car_data = request.data.copy()
    car_type = car_data.pop('car_type', [None])[0]  # Extract car_type as a string  # Extract car_type and remove it from car_data
    print("Input Car Type:", car_type)
    car_serializer = CarSerializer(data=car_data)

    if car_serializer.is_valid():
        car = car_serializer.save()
        image = request.FILES.get('image', None)
        if image:
            car.image.save(image.name, image, save=True)

        # Save to the appropriate subtable based on car_type
        subtable_data = {}
        if car_type == 'Convertible':
            subtable_data = {'canopymaterial': car_data.get('canopymaterial', '')}
            print("Convertible Data:", subtable_data)
        elif car_type == 'Electric':
            subtable_data = {'electric_range': car_data.get('electric_range', 0)}
        elif car_type == 'Hybrid':
            subtable_data = {
                'fuel_range': car_data.get('fuel_range', 0),
                'electric_range': car_data.get('electric_range', 0),
            }
        elif car_type == 'SUV':
            subtable_data = {'seatnumber': car_data.get('seatnumber', 0)}
        elif car_type == 'Sedan':
            subtable_data = {'seatnumber': car_data.get('seatnumber', 0)}
            print("Sedan Data:", subtable_data)
        elif car_type == 'Truck':
            subtable_data = {'boatload': car_data.get('boatload', 0)}

        if subtable_data:
            subtable_serializer = SUBTABLE_SERIALIZER_MAP[car_type](data={**subtable_data, 'vin': car.vin})
            print("Subtable Data:", subtable_serializer.initial_data)
            if subtable_serializer.is_valid():
                subtable_serializer.save()
            else:
                print("Subtable Serializer Errors:", subtable_serializer.errors)
                return Response(subtable_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Car added successfully'}, status=status.HTTP_201_CREATED)
    else:
        print(car_serializer.errors)
        return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# A mapping of car types to their corresponding serializers
SUBTABLE_SERIALIZER_MAP = {
    'Convertible': ConvertibleSerializer,
    'Electric': ElectricSerializer,
    'Hybrid': HybridSerializer,
    'SUV': SuvSerializer,
    'Sedan': SedanSerializer,
    'Truck': TruckSerializer,
}


# Delete a car (Admin)
@api_view(['DELETE'])
def delete_car(request, vin):
    try:
        car = Car.objects.get(vin=vin)
        car.delete()
        return Response({'message': 'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Car.DoesNotExist:
        return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def auction_cars(request, vin):
    try:
        auction_car = Auctioncar.objects.get(vin__vin=vin)
        auction_id = auction_car.auction.auction_id

        auction_cars = Auctioncar.objects.filter(auction__auction_id=auction_id)
        
        vins = auction_cars.values_list('vin', flat=True)
        
        cars = Car.objects.filter(vin__in=vins)

        serializer = CarSerializer(cars, many=True)
        response_data = {
            'auction_id': auction_id,
            'cars': serializer.data
        }
        return Response(response_data)
    except Auctioncar.DoesNotExist:
        return Response({'error': 'Car with the specified VIN does not exist or is not associated with any auction.'}, status=404)
    except Car.DoesNotExist:
        return Response({'error': 'No cars found in the specified auction.'}, status=404)

@api_view(['POST'])
def submit_bid(request):
    if request.method == 'POST':
        # 查询当前最大的 Bid_id
        max_bid_id = Bid.objects.aggregate(max_id=Max('bid_id'))['max_id']
        
        # 如果数据库为空，则设置 Bid_id 为 1，否则加 1
        new_bid_id = 1 if max_bid_id is None else max_bid_id + 1

        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            # 创建 Bid 实例，但不保存到数据库
            bid_data = serializer.validated_data
            bid_instance = Bid(**bid_data) # 根据具体模型字段调整
            # 手动设置 Bid_id
            bid_instance.bid_id = new_bid_id
            bid_instance.bid_time = timezone.now()
            bid_instance.bidwin = False
            # 保存到数据库
            bid_instance.save()

            return Response({'message': 'Bid submitted successfully', 'bid_id': new_bid_id})
        else:
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=400)

@api_view(['GET'])
def receive_bid(request):
    bids = Bid.objects.all()
    serializer = BidSerializer(bids, many=True)
    return Response(serializer.data)



