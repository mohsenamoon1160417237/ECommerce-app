from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth.models import User



class Coupon(models.Model):


	code 		 = models.CharField(max_length=25 , unique=True)
	active_from  = models.DateField()
	active_to    = models.DateField()
	discount     = models.PositiveIntegerField(validators=[MinValueValidator(0) , MaxValueValidator(100)])
	user         = models.ManyToManyField(User , related_name='coupons' , blank=True)
	number       = models.IntegerField(default=0)
	valid        = models.BooleanField(default=True)
	max_discount = models.DecimalField(default=100 , max_digits=6 , decimal_places=2) 


	def __str__(self):

		return self.code

