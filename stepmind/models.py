from django.db import models

class TeamMember(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class ProjectInfo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50, help_text="Font Awesome icon class")
    
    def __str__(self):
        return self.titulo

class FutureUpdate(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    version = models.CharField(max_length=20)
    fecha_estimada = models.DateField()
    
    def __str__(self):
        return f"{self.titulo} - v{self.version}"

class AppScreenshot(models.Model):
    titulo = models.CharField(max_length=100, default="Captura de App StepMind")
    descripcion = models.TextField(blank=True, help_text="Descripción opcional de la captura")
    imagen = models.ImageField(upload_to='app_screenshots/')
    activa = models.BooleanField(default=True, help_text="Mostrar esta captura en la página principal")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Captura de App"
        verbose_name_plural = "Capturas de App"
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha_creacion.strftime('%d/%m/%Y')}"

class AppGallery(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre de esta galería (ej: 'Tour Principal')")
    descripcion = models.TextField(blank=True, help_text="Descripción de la galería")
    activa = models.BooleanField(default=True, help_text="Mostrar esta galería en la página principal")
    auto_play = models.BooleanField(default=False, help_text="Reproducción automática")
    intervalo_segundos = models.PositiveIntegerField(default=3, help_text="Segundos entre imágenes (auto-play)")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Galería de App"
        verbose_name_plural = "Galerías de App"
    
    def __str__(self):
        return f"{self.nombre} ({self.imagenes.count()} imágenes)"
    
    def get_imagenes_ordenadas(self):
        return self.imagenes.filter(activa=True).order_by('orden')

class AppGalleryImage(models.Model):
    galeria = models.ForeignKey(AppGallery, on_delete=models.CASCADE, related_name='imagenes')
    titulo = models.CharField(max_length=100, help_text="Título de esta imagen")
    descripcion = models.TextField(blank=True, help_text="Descripción de lo que muestra esta imagen")
    imagen = models.ImageField(upload_to='app_gallery/')
    orden = models.PositiveIntegerField(default=0, help_text="Orden en la secuencia (0 = primera)")
    activa = models.BooleanField(default=True, help_text="Mostrar esta imagen en la galería")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Imagen de Galería"
        verbose_name_plural = "Imágenes de Galería"
        ordering = ['orden', 'fecha_creacion']
    
    def __str__(self):
        return f"{self.galeria.nombre} - {self.titulo}"

class AppDownload(models.Model):
    nombre = models.CharField(max_length=100, default="StepMind APK")
    version = models.CharField(max_length=20, help_text="Versión de la app (ej: 1.0.0)")
    descripcion = models.TextField(blank=True, help_text="Descripción de esta versión")
    archivo_apk = models.FileField(upload_to='apks/', help_text="Archivo APK para descargar")
    activa = models.BooleanField(default=True, help_text="Mostrar esta versión para descarga")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descargas = models.PositiveIntegerField(default=0, help_text="Número de descargas")
    
    class Meta:
        verbose_name = "APK de StepMind"
        verbose_name_plural = "APKs de StepMind"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} v{self.version}"
    
    def incrementar_descargas(self):
        self.descargas += 1
        self.save()
