from django.shortcuts import get_object_or_404, render
from django.views import generic  
from django.views import View  
from .models import Shop, Blog # Blogモデルをインポート
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


class DetailView(generic.DetailView):
    def get(self, request, *args, **kwargs): 
        shop = get_object_or_404(Shop, id=kwargs['pk']) # URLからIDを取得して対象の店を検索

        # 関連するブログ投稿を取得
        # Blogモデルのshopフィールドが現在のshopオブジェクトを参照しているものをフィルタリング
        blogs = Blog.objects.filter(shop=shop).order_by('-created_at') # 新しい順に並べ替え

        context = {
            'shop': shop, # Shopオブジェクト自体を渡すと、テンプレートでよりアクセスしやすくなります
            'result_detail_name': shop.name,
            'result_detail_address': shop.address,
            'result_detail_author': shop.author,
            'result_detail_category': shop.category,
            'blogs': blogs, # 取得したブログ一覧をコンテキストに追加
        }

        return render(request, 'app_folder/detail_base.html', context=context)

detail_page = DetailView.as_view()

class BlogPostDetailView(generic.DetailView):
    model = Blog  # 対象とするモデルはBlog
    template_name = 'app_folder/blog_post_detail.html'  # 使用するテンプレート
    context_object_name = 'blog_post'  # テンプレート内で記事を参照する際の変数名

blog_post_detail_view = BlogPostDetailView.as_view()