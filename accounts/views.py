from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/index')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})

from .models import Member
from django.utils import timezone
from django.http import HttpResponse
def signup_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')
        m = Member(
            user_id=user_id, user_pw=user_pw, user_name=user_name)
        m.date_joined = timezone.now()
        m.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s' % (user_id, user_pw, user_name))
    else:
        return render(request, 'accounts/signup_custom.html')
    
def logout(request):
    if request.method == 'POST':
        redirect('index/')
    return render(request, 'mbti/index.html')
