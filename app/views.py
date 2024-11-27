from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
@api_view(["GET"])
def category(request):
    categories = Category.objects.all()
    ser = CategorySerializer(categories, many=True)
    return Response(ser.data)

@api_view(['GET'])
def food(request):
    foods = Food.objects.all()
    ser = FoodSerializer(foods, many=True)
    return Response(ser.data)
    
@api_view(['POST'])
def reservation(request):
    print(request.data)
    name = request.POST.get('name')
    number_of_guests = request.POST.get('number_of_guests')
    date = request.POST.get('date')
    time = request.POST.get('time')
    Reservation.objects.create(
        name = name,
        number_of_guests = number_of_guests,
        date = date,
        time = time
    )
    return Response({'message': "Success"})