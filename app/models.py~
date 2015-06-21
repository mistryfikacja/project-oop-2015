from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class wpis(models.Model):
	data = models.DateTimeField(auto_now_add = True)
	tresc = models.TextField()
	tytul = models.CharField(max_length = 60)
	
	def __unicode__(self):
		return self.tytul[0:20] + ": " + self.tresc[0:40]
		
class wpis_pro(models.Model):
	data = models.DateTimeField(auto_now_add = True)
	tresc = models.TextField()
	tytul = models.CharField(max_length = 60)
	dodal = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.tytul[0:20] + ": " + self.tresc[0:40]
	
