from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html')
        else:
            return render(request, 'login.html')
        

