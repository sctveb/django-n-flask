from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from groups.models import GroupMember
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
# Create your views here.

User = get_user_model()

class PostList(ListView):
    model = Post
    
class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ('title','message','group')
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
        
class PostDetail(DetailView):
    model = Post
    
class UserPosts(ListView):
    model = Post
    template_name = 'posts/user_post_list.html'
    
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('post_set').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.post_set.all()
            
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context
        
class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)
        
    
class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ('message',)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)