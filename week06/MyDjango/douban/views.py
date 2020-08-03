from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
from .models import Shorts 

# 返回templates内的html网页
def movies_short(request):
    return render(request, 'result.html')

# 返回数据库内所有评分大于3的数据（JSON格式）
def short_list(request):
    queryset = Shorts.objects.all()
    conditions = {'star__gt': 3}
    tableData = serializers.serialize("json", queryset.filter(**conditions), ensure_ascii=False) 

    return JsonResponse(tableData, safe=False)

# 根据url后的key参数筛选评论返回（JSON格式）
def filted_list(request, key):
    queryset = Shorts.objects.all()
    conditions = {'star__gt': 3, 'content__contains': key}
    tableData = serializers.serialize("json", queryset.filter(**conditions), ensure_ascii=False) 

    return JsonResponse(tableData, safe=False)
