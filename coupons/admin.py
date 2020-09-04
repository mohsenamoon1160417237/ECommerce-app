from django.contrib import admin

# Register your models here.
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):

	list_display = ['code','max_discount', 'valid' , 'active_from' , 'active_to', 'number']
	list_editable = ['valid' , 'max_discount']
	list_filter = ['active_from' , 'active_to' , 'number' , 'max_discount']
	
