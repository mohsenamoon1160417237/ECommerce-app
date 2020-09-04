from django.contrib import admin
from .models import Product , ProductDetail , ProductAttribute , Catalog , Category





class CategoryAdmin(admin.TabularInline):

	model = Category
	list_display = ['catalog' , 'parent' , 'name']



@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):

	list_diaply = ['name' , 'publisher' , 'pub_date']
	inlines = [CategoryAdmin]



class ProductDetailAdmin(admin.TabularInline):

	model = ProductDetail
	raw_id_fields = ['attribute']
	list_display = ['product' , 'attribute' , 'value' , 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

	list_display = ['category' , 'name' , 'slug' , 'image' , 'manufacturer' , 'price' , 'available' , 'created' , 'updated']
	list_editable = ['available']
	inlines = [ProductDetailAdmin]


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):

	list_display = ['name' , 'description']


admin.site.register(Category)