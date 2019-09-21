from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import IntegrityError
from .models import Group, GroupMember

# Create your views here.
class GroupList(ListView):
    model = Group
    
class GroupCreate(LoginRequiredMixin,CreateView):
    model = Group
    fields = ('name','description')
    
class GroupDetail(DetailView):
    model = Group
    
class GroupJoin(LoginRequiredMixin,RedirectView):
    #코드 실행 후 리다이렉트 할 주소 설정
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:detail', kwargs={'slug':self.kwargs.get('slug')})
    #코드 실행
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,"실패")
        else:
            messages.success(self.request,"성공")
            
        return super().get(request,*args,**kwargs)
        
class GroupLeave(LoginRequiredMixin,RedirectView):
    
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:detail', kwargs={'slug':self.kwargs.get('slug')})
        
    def get(self,request,*args,**kwargs):
        
        try:
            membership = GroupMember.objects.filter(user= self.request.user,group__slug=self.kwargs.get('slug')).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request,"없음")
        else:
            membership.delete()
            messages.success(self.request,"지움")
            
        return super().get(request,*args,**kwargs)