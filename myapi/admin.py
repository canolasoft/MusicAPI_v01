from django.contrib import admin
from .models import *

class ArtistaAdmin(admin.ModelAdmin):
	list_display = ('id_a', 'nombre_a', 'imagen_a', 'descripcion_a', 'id_tag')
admin.site.register(Artista, ArtistaAdmin)

class RedsocialAdmin(admin.ModelAdmin):
	list_display = ('id_rs', 'id_a', 'nombre_rs', 'imagen_rs', 'url_rs')
admin.site.register(Redsocial, RedsocialAdmin)

class CancionAdmin(admin.ModelAdmin):
	list_display = ('id_c', 'id_a', 'nombre_c', 'imagen_c', 'url_c', 'id_tag')
admin.site.register(Cancion, CancionAdmin)

class TagAdmin(admin.ModelAdmin):
	list_display = ('id_tag', 'genero_tag', 'idioma_tag', 'imagen_tag')
admin.site.register(Tag, TagAdmin)

#class RedsocialArtistaAdmin(admin.ModelAdmin):
#	list_display = ('id_rs', 'id_a', 'url_rsa', 'imagen_rs')
#admin.site.register(RedsocialArtista, RedsocialArtistaAdmin)

#class WallpaperAdmin(admin.ModelAdmin):
#	list_display = ('id_w', 'nombre_w', 'imagen_w', 'id_a')
#admin.site.register(Wallpaper, WallpaperAdmin)

class DatappAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulomapp', 'mensajeapp', 'linkapp', 'keyapp', 'iconapp')
admin.site.register(Datapp, DatappAdmin)