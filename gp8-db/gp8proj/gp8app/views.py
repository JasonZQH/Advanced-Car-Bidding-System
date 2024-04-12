<<<<<<< Updated upstream
# Create your views here.
from django.shortcuts import render
from .models import User
=======
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
from django.utils import timezone
from django.db.models import Max
import logging
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
>>>>>>> Stashed changes

#Templete View
class ReactAppView(TemplateView):
    template_name = 'CarBiddingReact/index.html'

<<<<<<< Updated upstream
def testmysql(request):
    search_query = request.GET.get('search_query')  # Retrieve the search term from the GET request
=======
# Views' logging info
logger = logging.getLogger(__name__)
>>>>>>> Stashed changes

    if search_query:
        users = User.objects.filter(userid__icontains=search_query)
    else:
        users = User.objects.all()

    if users:
        context = {
            'user_id': users[0].userid,
            'user_gender': users[0].gender,
            'user_age': users[0].age,
            'user_phone': users[0].phone,
            'user_email': users[0].email,

        }
    else:
        context = {
            'user_id': 'Not found',
            'user_gender': 'Not found',
            'user_age': 'Not found',
            'user_phone': 'Not found',
            'user_email': 'Not found',

        }
        
<<<<<<< Updated upstream
    return render(request, 'home.html', context)
=======
#         vins = auction_cars.values_list('vin', flat=True)
        
#         cars = Car.objects.filter(vin__in=vins)


#         serializer = CarSerializer(cars, many=True)
#         response_data = {
#             'auction_id': auction_id,
#             'cars': serializer.data
#         }
#         return Response(response_data)
#     except Auctioncar.DoesNotExist:
#         return Response({'error': 'Car with the specified VIN does not exist or is not associated with any auction.'}, status=404)
#     except Car.DoesNotExist:
#         return Response({'error': 'No cars found in the specified auction.'}, status=404)



# Auction Car info extract (recive the vin from a car, get back to django, find where the car in which auction)
@api_view(['GET'])
def auction_cars(request, vin):
    # Find the auction car using the provided VIN
    auction_car = get_object_or_404(Auctioncar, vin__vin=vin)
    auction_id = auction_car.auction.auction_id

    # Fetch all cars associated with the auction
    auction_cars = Auctioncar.objects.filter(auction__auction_id=auction_id)

    # Serialize the auction cars with their auction-specific details
    auction_cars_serializer = AuctioncarSerializer(auction_cars, many=True)

    # Fetch and serialize the related car details
    car_vins = [ac.vin.vin for ac in auction_cars]
    cars = Car.objects.filter(vin__in=car_vins)
    car_serializer = CarSerializer(cars, many=True)

    response_data = {
        'auction_id': auction_id,
        'auction_cars': auction_cars_serializer.data,
        'car_details': car_serializer.data
    }
    return Response(response_data)


# Submit a bid
@api_view(['POST'])
def submit_bid(request):
    if request.method == 'POST':
        max_bid_id = Bid.objects.aggregate(max_id=Max('bid_id'))['max_id']
        new_bid_id = 1 if max_bid_id is None else max_bid_id + 1

        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            bid_data = serializer.validated_data
            bid_instance = Bid(**bid_data)
            bid_instance.bid_id = new_bid_id
            bid_instance.bid_time = timezone.now()
            bid_instance.bidwin = False
            bid_instance.save()

            return Response({'message': 'Bid submitted successfully', 'bid_id': new_bid_id})
        else:
            return Response(serializer.errors, status=400)

# Receive a bid  
@api_view(['GET'])
def receive_bid(request):
    vin = request.query_params.get('vin')
    if vin:
        bids = Bid.objects.filter(vin=vin)
    else:
        bids = Bid.objects.all()
    serializer = BidSerializer(bids, many=True)
    return Response(serializer.data)
>>>>>>> Stashed changes



