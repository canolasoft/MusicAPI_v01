# serializers.py
from rest_framework import serializers
from myapi.models import *

class ArtistaSerializer(serializers.HyperlinkedModelSerializer):
	id_tag = serializers.SlugRelatedField(read_only=True, slug_field='genero_tag')
	class Meta:
		model = Artista
		fields = ('id_a', 'nombre_a', 'imagen_a', 'descripcion_a', 'id_tag')

#class WallpaperSerializer(serializers.HyperlinkedModelSerializer):
#	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
#	class Meta:
#		model = Wallpaper
#		fields = ('id_w', 'id_a', 'nombre_w', 'imagen_w')

class RedsocialSerializer(serializers.HyperlinkedModelSerializer):
	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
	#id_rs = serializers.SlugRelatedField(read_only=True, slug_field='nombre_rs')
	class Meta:
		model = Redsocial
		fields = ('id_rs', 'id_a', 'nombre_rs', 'imagen_rs', 'url_rs')

class CancionesSerializer(serializers.HyperlinkedModelSerializer):
	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
	id_tag = serializers.SlugRelatedField(read_only=True, slug_field='id_tag')
	#id_rs = serializers.SlugRelatedField(read_only=True, slug_field='nombre_rs')
	class Meta:
		model = Cancion
		fields = ('id_c', 'id_a', 'nombre_c', 'imagen_c', 'url_c', 'id_tag')

class CancionSerializer(serializers.HyperlinkedModelSerializer):
	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
	id_tag = serializers.SlugRelatedField(read_only=True, slug_field='id_tag')
	class Meta:
		model = Cancion
		fields = ('id_c', 'id_a', 'nombre_c', 'imagen_c', 'url_c', 'id_tag')

#class RedsocialArtistaSerializer(serializers.ModelSerializer):
#	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
#	id_rs = serializers.SlugRelatedField(read_only=True, slug_field='nombre_rs')
#	imagen_rs = serializers.SlugRelatedField(read_only=True, slug_field='imagen_rs')
	#redsocial = serializers.SlugRelatedField(read_only=True, slug_field='nombre_rs')
#
#	class Meta:
#		model = RedsocialArtista
#		fields = ('id_a', 'url_rsa', 'imagen_rs', 'id_rs')

class DatappSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Datapp
		fields = ('id', 'titulomapp', 'mensajeapp', 'linkapp', 'iconapp')