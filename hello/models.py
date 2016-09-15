from django.db import models
# Create your models here.
class Caidos(models.Model):
	ema = models.CharField(max_length=50)
	pas = models.CharField(max_length=50)
	reg = models.DateTimeField('fecha de registro', auto_now_add=True)
	def __str__(self):
		return '%s %s %s' % (self.ema, self.pas, self.reg)
