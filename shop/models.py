from django.db import models
from .slugify import slugify  # For persian slugs
from django.urls import reverse
'''from whoosh.fields import Schema , TEXT
from whoosh.analysis import StemmingAnalyzer
from whoosh.index import create_index_in'''


class Catalog(models.Model):

	name 		= models.CharField(max_length=255 , unique=True)
	slug 		= models.SlugField(max_length=255 , unique=True , blank=True)
	publisher 	= models.CharField(max_length=255)
	description = models.TextField(blank=True)
	pub_date    = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return self.name

	def save(self , *args , **kwargs):

		self.slug = slugify(self.name)
		return super(Catalog,self).save()

	def get_absolute_url(self):

		return reverse('shop:product_list_by_catalog' , args=[self.slug , self.id])



class Category(models.Model):

	catalog 	= models.ForeignKey(Catalog , related_name='catalog_categories' , on_delete=models.CASCADE)
	parent  	= models.ForeignKey('self' , blank=True , null=True , related_name='children',
																	  on_delete=models.DO_NOTHING)
	name    	= models.CharField(max_length=150 , unique=True)
	slug    	= models.SlugField(max_length=150 , blank=True, unique=True)
	description = models.TextField(blank=True)

	def save(self , *args , **kwargs):

		self.slug = slugify(self.name)
		return super(Category,self).save()

	def __str__(self):

		if self.parent:

			return '{}:{}-{}'.format(self.catalog.name, 
								     self.parent.name,
								     self.name)

		return '{}:{}'.format(self.catalog , self.name)

	def get_absolute_url(self):

		return reverse('shop:product_list_by_category' , args=[self.slug , self.id])

	class Meta:

		verbose_name_plural = 'categories'




class Product(models.Model):


	category     = models.ForeignKey(Category , related_name='category_products' , on_delete=models.CASCADE)
	name 		 = models.CharField(max_length=40 , unique=True)
	slug 		 = models.SlugField(max_length=300 , unique=True , blank=True)
	description  = models.TextField()
	image        = models.ImageField(upload_to='products' , blank=True)
	manufacturer = models.CharField(max_length=200 , blank=True)
	price        = models.DecimalField(max_digits=6 , decimal_places=2)
	created      = models.DateTimeField(auto_now_add=True)
	updated      = models.DateTimeField(auto_now=True)
	available    = models.BooleanField(default=True)
	
	class Meta:

		ordering = ['-created']

	def __str__(self):

		return self.name


	def save(self , *args , **kwargs):

		self.slug = slugify(self.name)
		return super(Product,self).save()

	def get_absolute_url(self):

		return reverse('shop:product_detail' , args=[self.slug , self.id])
	
	
class ProductAttribute(models.Model):


	name 		= models.CharField(max_length=300)
	description = models.TextField(blank=True)

	def __str__(self):

		return self.name


class ProductDetail(models.Model):

	product   	= models.ForeignKey(Product , related_name='details' , on_delete=models.CASCADE)
	attribute 	= models.ForeignKey(ProductAttribute , on_delete=models.CASCADE)
	value     	= models.CharField(max_length=500)
	description = models.TextField(blank=True)

	def __str__(self):

		return '{}:{}-{}'.format(self.product,
								 self.attribute,
								 self.value)


