# from django.shortcuts import render,HttpResponse

# # Create your views here.
# def home(request):
#     return render(request, 'blog/blogindex.html')

# def blog(request):
#     return HttpResponse('this is blog')


from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blogs.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'