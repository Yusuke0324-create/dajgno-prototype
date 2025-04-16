from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django .views import View
from .models import Category, Shop


class SampleView(View):  
	def get(self, request, *args, **kwargs):  
		return render(request, 'app_folder/top_page.html')
top_page = SampleView.as_view()

    