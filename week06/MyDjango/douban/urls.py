from django.urls import path
from . import views


urlpatterns = [
    # index页导出templates网页
    path('index', views.movies_short),
    # data页拿到所有数据
    path('data/', views.short_list),
    # data后接key关键词用于筛选评论
    path('data/<str:key>', views.filted_list),
]