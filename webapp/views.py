from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, "signup.html")

def success(request):
    return render(request, "success.html")

def signup(request):
    return render(request, "signup.html")


def join_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        
        # Parola doğrulamasını kontrol edin
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('join_form')  # join_form.html dosyasının URL'sini belirtin
        
        # Kullanıcı oluştur ve kaydet
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('success.html')  # login sayfasının URL'sini belirtin
    
    return render(request, 'signup.html')