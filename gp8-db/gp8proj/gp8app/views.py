from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car, Users
from .serializers import CarSerializer, UsersSerializer, UserLoginSerializer

@api_view(['GET'])
def car_info(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['GET'])
def user_login(request):
    serializer = UserLoginSerializer(data=request.query_params)
    if serializer.is_valid():
        user_id = serializer.validated_data['user_id']
        email = serializer.validated_data['email']
        user = Users.objects.filter(user_id=user_id, email=email).first()
        if user:
            return Response({'message': 'Login successful', 'user_id': user.user_id})
        else:
            return Response({'message': 'Invalid ID number or email'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# @api_view(['POST'])
# def user_login(request):
#     email = request.data.get('email')
#     user_id = request.data.get('user_id')
#     if not email or not user_id:
#         return Response({'message': 'Email and user ID are required'}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         user = Users.objects.get(email=email, user_id=user_id)
#         user_serializer = UsersSerializer(user)
#         return Response(user_serializer.data)
#     except Users.DoesNotExist:
#         return Response({'message': 'Invalid email or user ID'}, status=status.HTTP_404_NOT_FOUND)
