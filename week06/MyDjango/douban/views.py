from django.shortcuts import render

# Create your views here.
from .models import Shorts 

def movies_short(request):
    queryset = Shorts.objects.all()
    conditions = {'star__gt': 3}
    tableData = queryset.filter(**conditions)

    return render(request, 'result.html', locals())
