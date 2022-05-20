from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q' : q,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    
    return render(request, 'instagram/post_detail.html', {
        'post': post,
    })
