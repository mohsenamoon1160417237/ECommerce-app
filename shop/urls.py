from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [

	path('' , views.product_list_all , name='product_list_all'),
	path('catalog/<slug:catalog_slug>/<int:catalog_id>/' , views.product_list_by_catalog ,
												   name='product_list_by_catalog'),
	path('category/<slug:category_slug>/<int:category_id>/' , views.product_list_by_category,
													 name='product_list_by_category'),
	path('product/<slug:product_slug>/<int:product_id>/' , views.product_detail , name='product_detail'),

]