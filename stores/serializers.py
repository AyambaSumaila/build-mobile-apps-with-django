from rest_framework import serializers
from .models import Pizzas


class PizzasListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzas
        fields =['id',  'name', 'city', 'zip_code']
            



class PizzasDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzas
        fields = [
            'id',
            'name',
            'street',
            'city',
            'state',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active',  # Added this field for filtering active pizzas only.
        ]