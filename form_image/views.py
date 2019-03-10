from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import View
from .forms import ArticleForm


class IndexView(View):
    # 如果是GET请求，直接渲染到上传文件页面
    def get(self, request):
        return render(request, 'index.html')

    # 如果是POST请求，那么将接收文件的值
    def post(self, request):
        # 获取前台传来的文件，request.POST用来接收title和content，request.FILES用来接收文件
        form = ArticleForm(request.POST, request.FILES)
        # 将数据保存到数据库
        if form.is_valid():
            form.save()
            return HttpResponse("SUCCESS")
        else:
            # 打印错误信息
            print(form.errors.get_json_data())
            return HttpResponse("Fail")

# Create your views here.
