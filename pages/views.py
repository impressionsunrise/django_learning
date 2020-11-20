from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World!</h1>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	my_context = {
	"title": "little title",
	"my_text": "This is contacts page",
	"Address": "Saint-Petersburg Novoizmailovsky",
	"my_list": [122,3212,3213, 'AA']
	}
	return render(request, "contact.html", my_context)
