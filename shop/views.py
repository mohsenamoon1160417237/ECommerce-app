from django.shortcuts import render , get_object_or_404
from .models import Product , ProductDetail , Category , Catalog
from cart.forms import CartForm
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from cart.forms import CartForm
from django.contrib.postgres.search import TrigramSimilarity , SearchVector , SearchQuery
from .forms import SearchForm
#from haystack.query import SearchQuerySet


def product_list_all(request):

	products = Product.objects.filter(available=True)
	catalogs = Catalog.objects.all()

	s_form = SearchForm()
	query = None

	if 'query' in request.GET:

		form = SearchForm(data=request.GET)

		if form.is_valid():

			query = form.cleaned_data['query']
			search_vector = SearchVector('name' , weight='A') + SearchVector('description' , weight='B')
			search_query = SearchQuery(query)
			products = Product.objects.annotate(similarity=TrigramSimilarity('name',query)).filter(similarity__gte=0.3
																								  ,available=True).order_by('-similarity')

	page = request.GET.get('page')
	paginator = Paginator(products,9)

	try:
		products = paginator.page(page)

	except PageNotAnInteger:

		products = paginator.page(1)

	except EmptyPage:

		products = paginator.page(paginator.num_pages)

	form = CartForm()


	return render(request , 'list_all.html' , {'products':products,
										       'catalogs':catalogs,
										       'page':page,
										       'form':form,
										       's_form':s_form,
										       'query':query})



def product_list_by_catalog(request , catalog_slug , catalog_id):

	catalog = get_object_or_404(Catalog , slug=catalog_slug , id=catalog_id)
	categories = Category.objects.filter(catalog=catalog)
	products = Product.objects.filter(category__catalog=catalog , available=True)
	s_form = SearchForm()
	query = None

	if 'query' in request.GET:

		form = SearchForm(data=request.GET)

		if form.is_valid():

			query = form.cleaned_data['query']
			search_vector = SearchVector('name' , weight='A') + SearchVector('description' , weight='B')
			search_query = SearchQuery(query)
			products = Product.objects.annotate(similarity=TrigramSimilarity('name',query)).filter(similarity__gte=0.3
																								  ,available=True).order_by('-similarity')


	page = request.GET.get('page')
	paginator = Paginator(products,9)

	try:
		products = paginator.page(page)

	except PageNotAnInteger:

		products = paginator.page(1)

	except EmptyPage:

		products = paginator.page(paginator.num_pages)

	form = CartForm()

	return render(request , 'list_by_catalog.html' , {'catalog':catalog,
													  'categories':categories,
													  'products':products,
													  'page':page,
													  'form':form,
													  's_form':s_form,
													  'query':query})




def product_list_by_category(request , category_slug , category_id):

	category = get_object_or_404(Category , slug=category_slug , id=category_id)
	catalog = category.catalog
	categories = Category.objects.filter(parent=category)
	products = Product.objects.filter(category=category)

	s_form = SearchForm()
	query = None

	if 'query' in request.GET:

		form = SearchForm(data=request.GET)

		if form.is_valid():

			query = form.cleaned_data['query']
			search_vector = SearchVector('name' , weight='A') + SearchVector('description' , weight='B')
			search_query = SearchQuery(query)
			products = Product.objects.annotate(similarity=TrigramSimilarity('name',query)).filter(similarity__gte=0.3
																								  ,available=True).order_by('-similarity')

	page = request.GET.get('page')
	paginator = Paginator(products,9)

	try:
		products = paginator.page(page)

	except PageNotAnInteger:

		products = paginator.page(1)

	except EmptyPage:

		products = paginator.page(paginator.num_pages)

	form = CartForm()


	return render(request , 'list_by_catg.html' , {'category':category,
												   'categories':categories,
												   'products':products,
												   'catalog':catalog,
												   'page':page,
												   'form':form,
												   's_form':s_form,
												   'query':query})






def product_detail(request , product_slug , product_id):

	product = get_object_or_404(Product , slug=product_slug , id=product_id)
	details = None

	if product.details:

		details = product.details.all()

	form = CartForm()

	return render(request , 'detail.html' , {'product':product,
											 'details':details,
											 'form':form})


	
