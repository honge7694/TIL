from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView




# CBV decorator 방법1
# @method_decorator(login_required(), name='dispatch')
# class PostListView(ListView):
#     model = Post
#     paginate_by = 10


# post_list = PostListView.as_view()


# CBV decorator 방법2
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()


# FBV decorator 방법1
# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))


# FBV decorator 방법2
# @login_required()
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
    
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q' : q,
#     })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    '''
    try :
        post = Post.objects.get(pk=pk) # DoesNotExist 예외 
    except Post.DoesNotExist:
        raise Http404
    '''
    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'instagram/post_detail.html', {
        'post': post,
    })


post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)