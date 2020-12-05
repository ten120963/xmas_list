from django.shortcuts import render, redirect
from .models import address
from .forms import addressForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.db.models import Q 

def home(request):
	all_addresses = address.objects.all
	return render(request, 'home.html', {'all_addresses': all_addresses})

def add_address(request):
	if request.method == "POST":
		form = addressForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Address Has Been Added!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems Like There Was An Error...'))	
			return render(request, 'add_address.html', {})	
	else:
		return render(request, 'add_address.html', {})	

def edit_address(request, list_id):
	if request.method == "POST":
		current_address = address.objects.get(pk=list_id)
		form = addressForm(request.POST or None, instance=current_address)
		if form.is_valid():
			form.save()
			messages.success(request, ('Address Has Been Edited!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems Like There Was An Error...'))	
			return render(request, 'edit_address.html', {})	
	else:
		get_address = address.objects.get(pk=list_id)
		return render(request, 'edit_address.html', {'get_address': get_address})	

def delete_address(request, list_id):
	if request.method == "POST":
		current_address = address.objects.get(pk=list_id)
		current_address.delete()
		messages.success(request, ('Address Has Been Deleted!'))
		return redirect('home')
	else:
		messages.success(request, ('Nothing To See Here...'))	
		return redirect('home')	

def cross_off(request, list_id):	
	item = address.objects.get(pk=list_id)
	item.received = True
	item.save()
	return redirect('home')	

def uncross(request, list_id):	
	item = address.objects.get(pk=list_id)
	item.received = False
	item.save()
	return redirect('home')		

class SearchHomePageView(TemplateView):
    template_name = 'search_home.html'

class SearchResultsView(ListView):
    model = address
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = address.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(zipcode__icontains=query)
        )
        return object_list