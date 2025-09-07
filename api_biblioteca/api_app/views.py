from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import AutorSerializer, EditorialSerializer, LibroSerializer, MiembroSerializer, PrestamoSerializer


# ---------------------- AUTOR ----------------------
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# ---------------------- EDITORIAL ----------------------
class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


# ---------------------- LIBRO ----------------------
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'autor__nombre', 'autor__apellido', 'editorial__nombre']

    @action(detail=False, methods=['get'])
    def buscar_por_autor(self, request):
        """Filtra libros por nombre o apellido del autor."""
        nombre_autor = request.query_params.get('autor', None)
        if nombre_autor:
            libros = Libro.objects.filter(autor__nombre__icontains=nombre_autor) | Libro.objects.filter(autor__apellido__icontains=nombre_autor)
            serializer = self.get_serializer(libros, many=True)
            return Response(serializer.data)
        return Response({"error": "Debes proporcionar el parámetro 'autor'."}, status=400)

    @action(detail=False, methods=['get'])
    def buscar_por_editorial(self, request):
        """Filtra libros por nombre de la editorial."""
        nombre_editorial = request.query_params.get('editorial', None)
        if nombre_editorial:
            libros = Libro.objects.filter(editorial__nombre__icontains=nombre_editorial)
            serializer = self.get_serializer(libros, many=True)
            return Response(serializer.data)
        return Response({"error": "Debes proporcionar el parámetro 'editorial'."}, status=400)


# ---------------------- MIEMBRO ----------------------
class MiembroViewSet(viewsets.ModelViewSet):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer


# ---------------------- PRÉSTAMO ----------------------
class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    @action(detail=True, methods=['post'])
    def devolver(self, request, pk=None):
        """Marca un préstamo como devuelto asignando la fecha de devolución."""
        prestamo = get_object_or_404(Prestamo, pk=pk)
        prestamo.fecha_devolucion = request.data.get('fecha_devolucion')
        prestamo.save()
        serializer = self.get_serializer(prestamo)
        return Response(serializer.data)
