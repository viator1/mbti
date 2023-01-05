from django.shortcuts import redirect, render
from mbtiapp.models import User , Comment

# 회원가입,로그인,로그아웃

def signup(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    user = User(email=email, name=name, pwd=pwd)
    user.save()
    return redirect('/index/')
  return render(request, 'mbtiapp/signup.html')


def login(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    try:
      user = User.objects.get(email=email, pwd=pwd)
      request.session['email'] = email
      return redirect('/index')
    except:
      return render(request, 'mbtiapp/login_fail.html')
  return render(request, 'mbtiapp/login.html')

def logout(request):
   
  request.session.flush()  

  return redirect('/index/')



# 게시판 기본화면
from mbtiapp.models import Article

def freeboard(request):
  article_list = Article.objects.order_by('-id')
  context = { 
    'article_list' : article_list 
  }
  return render(request, 'mbtiapp/freeboard.html', context)


def write(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    try:
      email = request.session['email']
      user = User.objects.get(email=email)
      article = Article(title=title, content=content, user=user)
      article.save()
      return redirect('/freeboard/')
    except:
      return render(request, 'mbtiapp/write_fail.html')

  return render(request, 'mbtiapp/write.html')


