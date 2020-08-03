# 学习笔记
## Django Web开发
### Django环境配置
1. 安装指定版本Django
```
pip install --upgrade django==xxxxx
```

2. 修改MyDjango/settings.py的数据库信息
```
DATABASES = {
    'default': {
        # 使用mysql数据库
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'douban',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
3. 创建自己的app，并注册在settings.py的INSTALLED_APPS里
```
python manage.py startapp xxx
```
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 新增app放在最后
    'index',
    'douban',
]
```

### 配置访问路径url
1. 修改MyDjango下的urls.py，配置路径链接到自建app的urls
```
urlpatterns = [
    path('admin/', admin.site.urls),
    # 引入别的app下的urls
    path('douban/', include('douban.urls')),
]
```
2. 配置urls，将路径与views内相应的函数绑定
```
urlpatterns = [
    # index页导出templates网页
    path('index', views.movies_short),
    # data页拿到所有数据
    path('data/', views.short_list),
    # data后接key关键词用于筛选评论
    path('data/<str:key>', views.filted_list),
]
```

### 使用ORM创建数据表
- 修改models.py，新建继承自models.Model的类，定义数据表的结构
```
class Shorts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=50)
    star = models.IntegerField()
    content = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'shorts'
```

### view视图编写
- 修改views.py，定义函数接收request以及url中获取的参数，返回templates或数据
```
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
```

### templates编写
- result.html
    - 引入react和antd，设置‘root’根节点，剩下的交给index.js
```
<!DOCTYPE html>
<html>

<head>
    {% block head %}
        <meta charset="UTF-8" />
        <title>豆瓣短评</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/antd/3.0.2/antd.css" />
        {% load static %}
    {% endblock %}
</head>

<body>

    <div id="root"></div>

    {% block js %}
        <script src="https://unpkg.com/react@16/umd/react.production.min.js" crossorigin></script>
        <script src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js" crossorigin></script>
        <script src="https://cdn.bootcss.com/babel-standalone/6.26.0/babel.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.20.1/moment.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/antd/3.0.2/antd.js"></script>
        <script type="text/babel" src="{% static 'js/index.js' %}"></script>
    {% endblock %}
</body>

</html>
```

- static/js/index.js
    - 发送ajax请求data路径的url，得到返回的JSON数据，再根据该数据渲染Table组件的内容，使用ReactDom挂载组件到root根节点上
    - 在搜索按钮Button组件上绑定click事件，获取input输入框的内容，并以此为key重新发送ajax请求，刷新root节点，达到搜索目的
```javascript
const columns = [
  {
    title: '用户名',
    dataIndex: 'user',
    key: 'user',
  },
  {
    title: '打分',
    dataIndex: 'star',
    key: 'star',
  },
  {
    title: '评论',
    dataIndex: 'content',
    key: 'content',
  }
]

let dataSource = null

let xmlHttp = new XMLHttpRequest()

function getShort(key) {
  xmlHttp.onreadystatechange =callback
  xmlHttp.open("get", `http://127.0.0.1:8000/douban/data/${key}`, true)

  xmlHttp.send()
}

function callback() {
  if (xmlHttp.readyState == 4)
      if (xmlHttp.status == 200) {
          //取得返回的数据
          let data = xmlHttp.responseText;
          //json字符串转为json格式
          dataSource = JSON.parse(eval(data));
          dataSource = dataSource.map(item => item.fields)
          ReactDOM.render(
            <div className="App">
              <h1>《霸王别姬》短评</h1>
              <antd.Input placeholder="输入搜索内容" style={{ width: 200, marginBottom: 10, marginLeft: 10 }} />
              <antd.Button type="primary" onClick={_ => getShort(document.getElementsByTagName('input')[1].value)} style={{ marginLeft: 8 }}>
                搜索
              </antd.Button>
              <antd.Table dataSource={dataSource}  columns={columns} rowKey='user' />
            </div>,
            document.getElementById("root")
          );    
      }
}

getShort('')

```