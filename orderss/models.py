from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from decimal import Decimal
from django.urls import reverse
#import uuid


class Order(models.Model):

	CITIES = [

	('I' , 'Isfahan'),
	('S' , 'Shiraz'),
	('T' , 'Tehran'),
	('Y' , 'Yazd'),
	('Q' , 'Qom')
	]

	STATUS = [

	('Sent' , 'Sent'),
	('Awaiting' , 'Awaiting'),
	('Recieved' , 'Recieved'),
	('Closed' , 'Closed')

	]

	owner 		 = models.ForeignKey(User , on_delete=models.CASCADE , related_name='orders')
	first_name 	 = models.CharField(max_length=50)
	last_name 	 = models.CharField(max_length=50)
	email   	 = models.EmailField()
	address 	 = models.TextField()
	city  		 = models.CharField(max_length=1 , choices=CITIES)
	postal_code  = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=12)
	created 	 = models.DateTimeField(auto_now_add=True)
	updated 	 = models.DateTimeField(auto_now=True)
	paid 		 = models.BooleanField(default=False)
	status       = models.CharField(max_length=10 , choices=STATUS , default='Awaiting')
	slug         = models.SlugField(unique=True , blank=True)

	def save(self , *args , **kwargs):

		self.slug = "order_" + str(self.id)
		return super(Order,self).save()

	def get_total_cost(self):

		return sum([Decimal(x.get_cost()) for x in self.orderItems.all()])

	def pretty_created_date(self):

		return self.created.strftime('%d/%m')

	def get_absolute_url(self):

		return reverse('accounts:order_detail' , args=[self.slug])




class OrderItem(models.Model):

	order 	 = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='orderItems')
	product  = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='orderItems')
	quantity = models.PositiveIntegerField(default=1)
	price 	 = models.DecimalField(max_digits=6 , decimal_places=2)

	def get_cost(self):

		return self.quantity * self.price

	def __str__(self):

		return '{}'.format(self.order.id)
	