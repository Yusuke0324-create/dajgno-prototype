from django.shortcuts import render
from django.views import generic  
from django.views import View  
from .models import Shop

class SampleView(View):  #一覧表示、検索機能のトップページ
	def get(self, request, *args, **kwargs): 
		shops = Shop.objects.all()
		context = {
            'object_list': shops,
        }
		return render(request, 'app_folder/page01.html', context=context)

	def post(self, request, *args, **kwargs):  
		input_data = request.POST['input_data']
		result = Shop.objects.filter(name=input_data)

		if result.exists():
			result_name = result[0].name
			result_address = result[0].address
		else:
			result_name = '該当する項目はありませんでした'
			result_address = ''

		context = {
    		'result_name': result_name,
    		'result_address': result_address,
		}
		return render(request, 'app_folder/page02.html', context=context)

top_page = SampleView.as_view()

class DetailView(generic.DetailView):
	def get(self, request, *args, **kwargs): 
		shops = Shop.objects.all()
		context = {
			'object_list': shops,
		}
		return render(request, 'app_folder/detail_base.html', context = context)

detail_page = DetailView.as_view()
