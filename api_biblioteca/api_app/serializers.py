from rest_framework import serializers
from .models import Autor, Editorial, Libro, Prestamo, Miembro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)          # muestra datos del autor
    editorial = EditorialSerializer(read_only=True)

    class Meta:
        model = Libro
        fields = '__all__'

class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    libro = LibroSerializer(read_only=True)      # anida la info del libro
    miembro = MiembroSerializer(read_only=True)  # anida la info del miembro

    class Meta:
        model = Prestamo
        fields = '__all__'


        