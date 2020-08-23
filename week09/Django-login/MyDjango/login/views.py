from django.shortcuts import render
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user: 
                login(request, user)
                return render(request, 'index.html', {'username': cd['username']})
            else: 
                return render(request, 'return.html')
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'form.html', { 'form': login_form })

