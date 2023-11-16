from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'formapp/index.html')

def form_page(request):
    form = forms.UserInfo()
    if request.method == 'POST':
        # Formで送られたデータを取り出す
        form = forms.UserInfo(request.POST)
        if form.is_valid():# バリデーション（フィールドが正しいかチェック）
            print('バリデーション成功')
            print(
                f"name: {form.cleaned_data['name']}, mail: {form.cleaned_data['mail']}, age: {form.cleaned_data['age']}"
            ) # formからname,mail,ageを取り出す
            print(form.cleaned_data)
    return render(
        request, 'formapp/form_page.html',context={
            'form': form
        } # formをcontextとして値を渡す
    )


def form_post(request):
    form = forms.PostModelForm()
    if request.method == 'POST':
        form = forms.PostModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(
        request, 'formapp/form_post.html', context={'form': form}
    ) # formappのform_post.htmlから画面表示