from django.contrib import admin
from .models import TeamMember, ProjectInfo, FutureUpdate, AppScreenshot, AppGallery, AppGalleryImage, AppDownload

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rol', 'linkedin']
    search_fields = ['nombre', 'rol']

@admin.register(ProjectInfo)
class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'icono']
    search_fields = ['titulo']

@admin.register(FutureUpdate)
class FutureUpdateAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'version', 'fecha_estimada']
    search_fields = ['titulo', 'version']
    list_filter = ['fecha_estimada']

@admin.register(AppScreenshot)
class AppScreenshotAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'activa', 'fecha_creacion']
    list_filter = ['activa', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion']
    list_editable = ['activa']
    ordering = ['-fecha_creacion']

class AppGalleryImageInline(admin.TabularInline):
    model = AppGalleryImage
    extra = 1
    fields = ['titulo', 'descripcion', 'imagen', 'orden', 'activa']
    ordering = ['orden']

@admin.register(AppGallery)
class AppGalleryAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'auto_play', 'intervalo_segundos', 'get_imagenes_count']
    list_filter = ['activa', 'auto_play', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['activa', 'auto_play']
    ordering = ['-fecha_creacion']
    inlines = [AppGalleryImageInline]
    
    def get_imagenes_count(self, obj):
        return obj.imagenes.count()
    get_imagenes_count.short_description = 'Imágenes'

@admin.register(AppGalleryImage)
class AppGalleryImageAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'galeria', 'orden', 'activa', 'fecha_creacion']
    list_filter = ['galeria', 'activa', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion', 'galeria__nombre']
    list_editable = ['orden', 'activa']
    ordering = ['galeria', 'orden']

@admin.register(AppDownload)
class AppDownloadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'version', 'activa', 'descargas', 'fecha_creacion']
    list_filter = ['activa', 'fecha_creacion']
    search_fields = ['nombre', 'version', 'descripcion']
    list_editable = ['activa']
    ordering = ['-fecha_creacion']
    readonly_fields = ['descargas']
