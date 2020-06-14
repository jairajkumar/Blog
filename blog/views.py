from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'blog/blogindex.html')

def blog(request):
    return HttpResponse('this is blog')
