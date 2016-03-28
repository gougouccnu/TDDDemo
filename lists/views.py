from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
	#return HttpResponse(b'<html><title>To-Do lists</title></html>')
	#if request.method == 'POST':
	#	return HttpResponse(request.POST['item_text'])
	if request.method == 'POST':
		#new_item_text = request.POST['item_text']
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')

	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})

def view_list(request):
	
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})
