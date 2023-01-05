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
    datas = Mbtidata.objects.all()
    context = {'datas': datas}
    return render(request, 'file/index.html', context)
