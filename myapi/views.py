from rest_framework import viewsets
import django_filters
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import(ListCreateAPIView)

# Consulta 0: dame los datos de la app
class DatappViewSet(viewsets.ModelViewSet):
	#queryset = Datapp.objects.all()
	serializer_class = DatappSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		return Datapp.objects.filter(keyapp = kap)

# Consulta 1: dame todos los Artistas
class ArtistasViewSet(viewsets.ModelViewSet):
	#queryset = Artista.objects.all().order_by('nombre_a')
	serializer_class = ArtistaSerializer
	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			return Artista.objects.all().order_by('nombre_a')

# Consulta 2: dame todos las Canciones de un Artista
class CancionesSerializer(ListCreateAPIView):
	serializer_class = CancionesSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_a = self.request.GET.get('id')
			canciones = Cancion.objects.filter(id_a__id_a = id_a)
			return canciones

# Consulta 2: dame todos los Wallpapers de un Artista
#class WallpaperSerializer(ListCreateAPIView):
#	serializer_class = WallpaperSerializer
#
#	def get_queryset(self):
#		kap = self.request.GET.get('kap')
#		if(Datapp.objects.filter(keyapp = kap)):
#			id_a = self.request.GET.get('id')
#			wallpapers = Wallpaper.objects.filter(id_a__id_a = id_a)
#			return wallpapers

# Consulta 3: dame los datos de un Artista
class ArtistaViewSet(viewsets.ModelViewSet):
	serializer_class = ArtistaSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_a = self.request.GET.get('id')
			return Artista.objects.filter(id_a = id_a)

# Consulta 4: dame las Redes de un Artista
class RedsocialSerializer(ListCreateAPIView):
	serializer_class = RedsocialSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_a = self.request.GET.get('id')
			redesociales = Redsocial.objects.filter(id_a__id_a = id_a)
			return redesociales

# Consulta 5: dame los datos de una Cancion
class CancionSerializer(ListCreateAPIView):
	serializer_class = CancionSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_c = self.request.GET.get('id')
			cancion = Cancion.objects.filter(id_c = id_c)
			return cancion

############ LANDING
def index(request):
# Home index (lista de artistas)
	artistas = Artista.objects.all().order_by('?')
	#videos = Video.objects.all()
	context = {
		'artistas':artistas,
        #'videos':videos,
        }
	return render(request, "landing/index.html", context)

# Artista perfil (datos del artista y lista de videos)
def artista(request):
	id_a = request.GET.get('id')
	artista = Artista.objects.filter(id_a = id_a).first
	#logger.error("artista: "+str(artista))
	canciones = Cancion.objects.filter(id_a = id_a)
	context = {
		'artista':artista,
        'canciones':canciones,
        }
	return render(request, "landing/artista.html", context)
