from django.contrib import admin

from .models import Order , OrderItem



class OrderItemAdmin(admin.TabularInline):

	model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

	inlines = [OrderItemAdmin]
	list_display = ['owner','status','paid','first_name' , 'last_name' , 'address' , 'city' , 'created' , 'updated' ,
				    'phone_number' , 'postal_code']
				    
	list_editable = ['status']

	list_filter = ['paid' , 'owner' , 'created' , 'updated']


admin.site.register(OrderItem)
