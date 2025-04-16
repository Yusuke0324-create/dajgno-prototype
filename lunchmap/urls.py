from django.urls import path
from . import views

#top_page.htmlとリンクしている。top_pageでappp_folderとなっている部分をlunchmapに直せばここをapp_name = 'lunchmap'にできるが、まだやっていない
app_name = 'app_folder'

urlpatterns = [
    path('top_page/', views.top_page, name='top_page')
]