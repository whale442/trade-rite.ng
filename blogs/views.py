from django.shortcuts import render
from accounts.models import User

from blogs.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView, View)


def blog(request):
    blogs = Post.objects.all()
    context = {
        'blogs':blogs
    }
   
    return render(request, 'blogs/blog.html',context)

class UserPostListView(ListView):
    model = Post
    template_name = 'blogs/user_blogs.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')    


class PostDetailView(DetailView):
    model = Post