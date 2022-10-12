from django.db import models

class Tag(models.Model):
	id_tag = models.BigAutoField(primary_key=True)
	imagen_tag = models.ImageField(null=True, blank=True)
	genero_tag = models.CharField(max_length=100)
	idioma_tag = models.CharField(max_length=100)
	def __str__(self):
		return self.genero_tag

	@property
	def imageURL(self):
		try:
			url = self.imagen_c.url
		except:
			url = ''
		return url

class Artista(models.Model):
	id_a = models.BigAutoField(primary_key=True)
	nombre_a = models.CharField(max_length=60)
	imagen_a = models.ImageField(null=True, blank=True)
	descripcion_a = models.CharField(max_length=200)
	id_tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.nombre_a

	@property
	def imageURL(self):
		try:
			url = self.imagen_a.url
		except:
			url = ''
		return url

class Redsocial(models.Model):
	id_rs = models.BigAutoField(primary_key=True)
	id_a = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True)
	nombre_rs = models.CharField(max_length=30)
	imagen_rs = models.ImageField(null=True, blank=True)
	url_rs = models.CharField(max_length=150, null=True)
	def __str__(self):
		return self.nombre_rs

	@property
	def imageURL(self):
		try:
			url = self.imagen_rs.url
		except:
			url = ''
		return url

#class RedsocialArtista(models.Model):
#	id_rs = models.ForeignKey(Redsocial, related_name='Redsocial_id_rs', on_delete=models.SET_NULL, null=True)
#	id_a = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True)
#	imagen_rs = models.ForeignKey(Redsocial, related_name='Redsocial_imagen_rs', on_delete=models.SET_NULL, null=True)
#	url_rsa = models.CharField(max_length=150)
#	def __str__(self):
#		return self.url_rsa
#
#	@property
#	def imageURL(self):
#		try:
#			url = self.imagen_rs.url
#		except:
#			url = ''
#		return url

class Datapp(models.Model):
	titulomapp = models.CharField(max_length=50)
	mensajeapp = models.CharField(max_length=150)
	linkapp = models.CharField(max_length=150)
	keyapp = models.CharField(max_length=200)
	iconapp = models.CharField(max_length=10)
	def __str__(self):
		return self.mensajeapp

class Cancion(models.Model):
	id_c = models.BigAutoField(primary_key=True)
	id_a = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True)
	nombre_c = models.CharField(max_length=100)
	imagen_c = models.ImageField(null=True, blank=True)
	url_c = models.CharField(max_length=200, null=True)
	id_tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.nombre_c

	@property
	def imageURL(self):
		try:
			url = self.imagen_c.url
		except:
			url = ''
		return url




# Eliminar de aca para abajo
#class Wallpaper(models.Model):
#	id_w = models.BigAutoField(primary_key=True)
#	id_a = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True)
#	nombre_w = models.CharField(max_length=100)
#	imagen_w = models.ImageField(null=True, blank=True)
#	def __str__(self):
#		return self.nombre_w
#
#	@property
#	def imageURL(self):
#		try:
#			url = self.imagen_w.url
#		except:
#			url = ''
#		return url

