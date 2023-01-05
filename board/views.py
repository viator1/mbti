from django.shortcuts import render
from board.models import Post

# Create your views here.
def freeboard(request):
  page=request.GET.get('page')
  if not page: page='1'

  page=int(page)
  end = page*10
  start = end-10

  s_page = (page-1)//10*10+1 
  e_page = s_page+9

  total_count = Post.objects.all().count()
  total_page = total_count//10
  if page > total_page:
    page = total_page
    end = page*10
    start = end - 10
  
  page_info = range(s_page, e_page+1)
  post= Post.objects.order_by('-id')
  post = post[start:end]
  context = { 
    'post' : post,
    'page_info' : page_info
  }
  return render(request, 'board/freeboard.html', context)
  
from django.contrib.auth.models import User

def write(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')

    try:
      email = request.session['email']
      user = User.objects.get(email=email)
      post = Post(title=title, content=content, user=user)
      post.save()
      return render(request, 'board/write_success.html')
    except:
      return render(request, 'board/write_fail.html')
  return render(request, 'board/write.html')

  
  
  