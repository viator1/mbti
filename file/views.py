from django.shortcuts import redirect, render
from .models import Mbtidata

def insert(request):
    if request.method == 'GET':
        return render(
            request,
            'mbti/insert.html')
    name=request.POST.get('name')
    mbti=request.POST.get('mbti')
    description=request.POST.get('description')
    m=Mbtidata()
    m.name=name
    m.mbti=mbti
    m.description=description
    m.save()
    return redirect('/file/show/')


def show(request):
    mbtidata=Mbtidata.objects.all()

    return render(request, 'mbti/show.html', {
        'data': mbtidata })


def index(request):
    page=request.GET.get('page')
    if not page: page='1'

    page=int(page)
    end = page*10
    start = end-10

    s_page = (page-1)//10*10+1 
    e_page = s_page+9

    total_count = Mbtidata.objects.all().count()
    total_page = total_count//10
    if page > total_page:
        page = total_page
        end = page*10
        start = end - 10
    
    page_info = range(s_page, e_page+1)
    data= Mbtidata.objects.order_by('-id')
    data = data[start:end]
    context = { 
        'data' : data,
        'page_info' : page_info
    }
    return render(request, 'file/index.html', context)