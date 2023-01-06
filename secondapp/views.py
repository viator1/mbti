
from django.shortcuts import render

from file.models import Mbtidata
from secondapp.models import MbtiDetail


def ISTJ(request):
    return render(request, 'mbti/ISTJ.html')
def ISFJ(request):
    return render(request, 'mbti/ISFJ.html')
def INFJ(request):
    return render(request, 'mbti/INFJ.html')
def INTJ(request):
    return render(request, 'mbti/INTJ.html')
def ISTP(request):
    return render(request, 'mbti/ISTP.html')
def ISFP(request):
    return render(request, 'mbti/ISFP.html')
def INFP(request):
    return render(request, 'mbti/INFP.html')
def INTP(request):
    return render(request, 'mbti/INTP.html')
def ESTP(request):
    return render(request, 'mbti/ESTP.html')
def ESFP(request):
    return render(request, 'mbti/ESFP.html')
def ENFP(request):
    return render(request, 'mbti/ENFP.html')
def ENTP(request):
    return render(request, 'mbti/ENTP.html')
def ESTJ(request):
    return render(request, 'mbti/ESTJ.html')
def ESFJ(request):
    return render(request, 'mbti/ESFJ.html')
def ENFJ(request):
    return render(request, 'mbti/ENFJ.html')
def ENTJ(request):
    return render(request, 'mbti/ENTJ.html')
def what(request):
    return render(request, 'mbti/what.html')
def kinds(request):
    return render(request, 'mbti/kinds.html')
def freeboard(request):
    return render(request, 'mbti/freeboard.html')
def counseling(request):
    return render(request, 'mbti/counseling.html')
def bd(request):
    return render(request, 'mbti/bd.html')

def post_detail(request):
  page=request.GET.get('page')
  if not page: page='1'

  page=int(page)
  end = page*10
  start = end-10

  s_page = (page-1)//10*10+1 
  e_page = s_page+9
  page_info = range(s_page, e_page+1)

  data_list = Mbtidata.objects.order_by('-id')
  data_list = data_list[start:end]
  context = { 
    'data_list' : data_list,
    'page_info' : page_info
  }
  return render(request, 'secondapp/detail.html', context)
    