from rest_framework import serializers
from .models import Autor, Editorial, Libro, Prestamo, Miembro


#   AUTOR

class AutorSerializer(serializers.ModelSerializer):
    id_autor = serializers.IntegerField(read_only=True)  # <-- Esto es la clave

    class Meta:
        model = Autor
        fields = ['id_autor', 'nombre', 'apellido', 'biografia']


#   EDITORIAL

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


#   LIBRO

class LibroSerializer(serializers.ModelSerializer):

    autor = AutorSerializer(read_only=True)
    editorial = EditorialSerializer(read_only=True)

  
    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(),
        source='autor',
        write_only=True
    )
    editorial_id = serializers.PrimaryKeyRelatedField(
        queryset=Editorial.objects.all(),
        source='editorial',
        write_only=True
    )

    class Meta:
        model = Libro
        fields = '__all__'


#   MIEMBRO

class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


#   PRÉSTAMO

class PrestamoSerializer(serializers.ModelSerializer):
    libro = LibroSerializer(read_only=True)
    miembro = MiembroSerializer(read_only=True)

    libro_id = serializers.PrimaryKeyRelatedField(
        queryset=Libro.objects.all(),
        source='libro',
        write_only=True
    )
    miembro_id = serializers.PrimaryKeyRelatedField(
        queryset=Miembro.objects.all(),
        source='miembro',
        write_only=True
    )

    class Meta:
        model = Prestamo
        fields = '__all__'

        