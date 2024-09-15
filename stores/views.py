from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .serializers import PizzasListSerializer, PizzasDetailSerializer # type: ignore
from .models import Pizzas

class PizzasListAPIView(generics.ListAPIView):
    queryset = Pizzas.objects.all()
    serializer_class = PizzasListSerializer # type: ignore
    
    
    
class PizzasRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Pizzas.objects.all()
    serializer_class = PizzasDetailSerializer # type: ignore
  
  
    
class PizzasCreateAPIView(generics.CreateAPIView):
    queryset = Pizzas.objects.all()
    serializer_class = PizzasDetailSerializer # type: ignore
    
    
   
  
    
class PizzasRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id' 
    queryset = Pizzas.objects.all()
    serializer_class = PizzasDetailSerializer # type: ignore
    
    
#This is the Delete API class 
class PizzasDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id' 
    queryset = Pizzas.objects.all()
    
    
    
    
    
         
    
    
    