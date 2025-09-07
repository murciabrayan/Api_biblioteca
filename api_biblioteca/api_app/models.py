from django.db import models

class Autor(models.Model):
    id_autor= models.AutoField(primary_key=True, editable=False, db_column='T001IdAutor')
    nombre = models.CharField(max_length=100, db_column='T001Nombre')
    apellido = models.CharField(max_length=100, db_column='T001Apellido')
    biografia = models.TextField(db_column='T001Biografia', blank=True, null=True)



    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T001Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'autores'

class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True, editable=False, db_column='T002IdEditorial')
    nombre_editorial = models.CharField(max_length=200, db_column='T002Editorial')
    direccion = models.CharField(max_length=200, db_column='T002Direccion')
    telefono = models.CharField(max_length=20, db_column='T002Telefono', blank=True, null=True)


    def __str__(self):
        return self.nombre_editorial

    class Meta:
        db_table = 'T002Editorial'
        verbose_name = 'Editorial'
        verbose_name_plural = 'editoriales'   


          
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True, editable=False, db_column='T004IdLibro')
    titulo = models.CharField(max_length=200, db_column='T004Titulo')
    resumen = models.TextField(db_column='T004Resumen', blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True, db_column='T004ISBN')
    anio_publicacion = models.IntegerField(db_column='T004AnioPublicacion')

    # Relaciones
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, db_column='T001IdAutor')
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE, db_column='T002IdEditorial')

    def __str__(self):
        return f"{self.titulo} ({self.anio_publicacion})"

    class Meta:
        db_table = 'T004Libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'libros'




class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True, editable=False, db_column='T005IdPrestamo')
    fecha_prestamo = models.DateField(db_column='T005FechaPrestamo')
    fecha_devolucion = models.DateField(null=True, blank=True, db_column='T005FechaDevolucion')
    
    
    
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE, db_column='T004IdLibro')
    miembro = models.ForeignKey('Miembro', on_delete=models.CASCADE, db_column='T003IdMiembro')


    def __str__(self):
        return f"{self.fecha_prestamo} ({self.fecha_devolucion})"

    class Meta:
        db_table = 'T005Prestamo'
        verbose_name = 'Prestamo'
        verbose_name_plural = 'prestamos'



class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True, editable=False, db_column='T003IdMiembro')
    nombre_miembro = models.CharField(max_length=100, db_column='T003NombreMiembro')
    apellido_miembro = models.CharField(max_length=100, db_column='T003ApellidoMiembro')
    email_miembro = models.EmailField(max_length=40, db_column='T003EmailMiembro')
    fecha_membresia = models.DateField(db_column='T003FechaMembresia')

    def __str__(self):
        return f"{self.nombre_miembro} {self.apellido_miembro}"

    class Meta:
        db_table = 'T003Miembro'
        verbose_name = 'Miembro'
        verbose_name_plural = 'miembros'






        