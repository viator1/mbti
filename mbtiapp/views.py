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
      return redirect('/')
    except:
      return render(request, 'mbtiapp/login_fail.html')
  return render(request, 'mbtiapp/login.html')

def logout(request):
   
  request.session.flush()  

  return redirect('/')



# 게시판 기본화면
from mbtiapp.models import Article

def freeboard(request):
  page=request.GET.get('page')
  if not page: page='1'

  page=int(page)
  end = page*10
  start = end-10

  s_page = (page-1)//10*10+1 
  e_page = s_page+9
  page_info = range(s_page, e_page+1)

  article_list = Article.objects.order_by('-id')
  article_list = article_list[start:end]
  context = { 
    'article_list' : article_list,
    'page_info' : page_info
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

def detail(request, id):
  article = Article.objects.get(id=id)
  context = { 
    'article' : article 
  }
  return render(request, 'mbtiapp/detail.html', context)

def detail(request, id):
  article = Article.objects.get(id=id)
  context = { 
    'article' : article 
  }
  return render(request, 'mbtiapp/detail.html', context)

def edit(request, id):
  article = Article.objects.get(id=id)

  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    try:
      article.title = title
      article.content = content
      article.save()
      return redirect('/freeboard/')
    except:
      return render(request, 'mbtiapp/edit_fail.html')

  context = { 
    'article' : article 
  }
  return render(request, 'mbtiapp/edit.html', context)

def delete(request, id):
  try:
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/freeboard/')
  except:
    return render(request, 'mbtiapp/delete_fail.html')