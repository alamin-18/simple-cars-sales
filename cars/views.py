from django.shortcuts import render
from django.views.generic import DetailView
from .import forms

from . import models

# Create your views here.

class CarsDetails(DetailView):
    model = models.Cars
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'c'
    
    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentsForms(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.cars = post
            new_comment.save()
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars =self.object
        comments = cars.comments.all()
        comment_form = forms.CommentsForms()
        context['comments']=comments
        context['comments_form'] =comment_form
        return context
