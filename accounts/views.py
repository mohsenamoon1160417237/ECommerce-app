from django.shortcuts import render , get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from orderss.models import Order , OrderItem
#from django.views.generic.edit import DeleteView , UpdateView
from django.views.generic.base import View , TemplateResponseMixin



def register(request):

	if request.method == 'POST':

		form = UserRegistrationForm(data=request.POST)
		if form.is_valid():

			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			return render(request , 'register_done.html' , {'new_user':new_user})


	else:

		form = UserRegistrationForm()


	return render(request , 'register.html' , {'form':form})





class Dashboard(TemplateResponseMixin , View):


	user = None
	username = user.username
	orders = user.orders.all()

	template_name = 'dashboard.html'
	order_item = None
	product = order_item.product


	def dispatch(self , request , order_item_id , username):

		self.order_item = get_object_or_404(OrderItem , id=order_item_id , order__owner=request.user)
		self.user = get_object_or_404(User , username=username)
		return super(Dashboard,self).dispatch(request , order_item_id)



	



def order_detail(request , order_slug):

	order = get_object_or_404(Order , slug=order_slug)
	orderItems = order.orderItems.all()

	return render(request , 'order_detail.html' , {"order":order,
												   "orderItems":orderItems})


