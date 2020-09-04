from django.contrib.sitemaps import Sitemap
from shop.models import Product


class ProductSitemap(Sitemap):

	def items(self):

		return Product.objects.filter(available=True)