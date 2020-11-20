from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
from loguru import logger
from django.http import Http404
# Create your views here.

'''def product_create_view(request):
	form = RawProductForm()
	if request.method == "POST":
		form = RawProductForm(request.POST)
		if form.is_valid():
			Product.objects.create(**form.cleaned_data)
			print(form.cleaned_data)
		else:
			print(form.errors)
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)'''
def product_create_view(request):
	logger.debug("logging....")
	initial_data = {
		'title': "My awesome text",
		'email': "alex@mail.ru",
		'description': "test descr"}
	obj = Product.objects.get(id=21)
	form = ProductForm(request.POST or None,instance=obj)
	#form = ProductForm(request.POST or None, initial=initial_data)
	logger.debug("Before save")
	if request.method == "POST":
		if form.is_valid():
			logger.debug("Saving data to DB")
			form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

def product_detail_view(request, id):
	obj = Product.objects.get(id=id)
	context  = {
		'product': obj,
	}		

	return render(request, "products/product_detail.html", context)

def dynamic_lookup_view(request, id):
	try:
		obj = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise Http404
	
	#obj = get_object_or_404(Product, id=id)
	context = { 
		"object": obj
	}
	return render(request, "products/product_detail.html", context)
def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	#POST request
	if request.method == "POST":
		obj.delete()
		return redirect('../')
	context = {
		"object":obj
	}
	return render(request, "products/product_delete.html", context)
def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, "products/product_list.html", context)
