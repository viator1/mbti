from django.shortcuts import render

def what(request):
    return render(request, 'mbti/what.html')
