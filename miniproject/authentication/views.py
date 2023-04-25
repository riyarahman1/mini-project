from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View
# Create your views here.








class Login(View):
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'authenticate/login.html')
        else:
            return render(request, 'login.html')
