from django.urls import path
from . import views


#top_page.htmlとリンクしている。top_pageでappp_folderとなっている部分をlunchmapに直せばここをapp_name = 'lunchmap'にできるが、まだやっていない
app_name = 'lunchmap'

urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),
    path('detail/<int:pk>/', views.detail_page, name='detail_page'),

]