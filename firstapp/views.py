
from django.shortcuts import render

def index(request):
    return render(request, 'mbti/index.html')
def main(request):
    return render(request, 'mbti/main.html')