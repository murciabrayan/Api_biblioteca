from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.views import AutorViewSet, EditorialViewSet, LibroViewSet, MiembroViewSet, PrestamoViewSet

router = DefaultRouter()

router.register(r'autores', AutorViewSet, basename='autores')          # /api/autores/
router.register(r'editoriales', EditorialViewSet, basename='editoriales')  # /api/editoriales/
router.register(r'libros', LibroViewSet, basename='libros')            # /api/libros/
router.register(r'miembros', MiembroViewSet, basename='miembros')      # /api/miembros/
router.register(r'prestamos', PrestamoViewSet, basename='prestamos')   # /api/prestamos/

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

