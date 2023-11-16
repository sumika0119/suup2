from django.urls import path #画面遷移を定義
from . import views


app_name = 'form_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('form_page/', views.form_page, name='form_page'),
    path('form_post/', views.form_post, name='form_post')
] # 遷移する画面を２つ定義