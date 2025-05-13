from django.shortcuts import get_object_or_404, render
from django.views import generic  
from django.views import View  
from .models import Shop
from django.shortcuts import render, get_object_or_404





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



# class DetailView(generic.DetailView):
#     model = Shop  # 対象のモデルを指定
#     template_name = 'app_folder/detail_base.html'  # 使用するテンプレートを指定
#     context_object_name = 'shop'  # テンプレート内での変数名

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         shop = self.get_object()  # 自動的にオブジェクトを取得
#         context['result_detail_name'] = shop.name
#         context['result_detail_address'] = shop.address
#         context['result_detail_author'] = shop.author
#         context['result_detail_category'] = shop.category
#         return context

class DetailView(generic.DetailView):
	def get(self, request, *args, **kwargs): 
		shop = get_object_or_404(Shop, id = kwargs['pk'])#urlからIDを取得して対照の店を検索


		detail_name = shop.name
		detail_address = shop.address
		detail_author = shop.author
		detail_category = shop.category
		context = {
			'result_detail_name' : detail_name,
			 'result_detail_address' : detail_address,
			 'result_detail_author' : detail_author,
			 'result_detail_category' : detail_category,

		}



		return render(request, 'app_folder/detail_base.html', context = context)

detail_page = DetailView.as_view()
