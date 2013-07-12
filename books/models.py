from django.db import models

# Create your models here.
class Editor(models.Model):
	name 			= models.CharField(max_length=30)
	address 		= models.CharField(max_length=50)
	city 			= models.CharField(max_length=60)
	state_province	= models.CharField(max_length=30)
	country 		= models.CharField(max_length=50)
	website 		= models.URLField()
	def __unicode__ (self):
		return str(self.name)
	class Meta:
		ordering=["name"]


class Autor(models.Model):
	salutation 	= models.CharField(max_length=10)
	first_name	= models.CharField(max_length=30)
	last_name 	= models.CharField(max_length=40)
	email 		= models.EmailField()
	headshot 	= models.ImageField(upload_to= '/tmp',blank=True, null=True )
	def __unicode__ (self):
		return self.first_name+" "+self.last_name


class Libro(models.Model):
	title 			 = models.CharField(max_length=100)
	autores 		 = models.ManyToManyField(Autor)
	editores 		 = models.ForeignKey(Editor)
	publication_date = models.DateField()
	def __unicode__ (self):
		return self.title
