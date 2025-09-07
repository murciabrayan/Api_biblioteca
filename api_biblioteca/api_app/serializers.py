from rest_framework import serializers
from .models import Autor, Editorial


class Autorserializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'



class Libroserializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'


class Editorialserializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'



class Prestamoserializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'


class Miembrolserializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'
        