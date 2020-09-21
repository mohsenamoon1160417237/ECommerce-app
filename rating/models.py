from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Rating(models.Model):

	rating         = models.IntegerField()
	content_type   = models.ForeignKey(ContentType , on_delete=models.CASCADE)
	object_id      = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type' , 'object_id') 


	def __str__(self):

		return str(self.rating)



