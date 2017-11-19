"""
https://docs.djangoproject.com/en/1.11/topics/http/views/
https://docs.djangoproject.com/en/1.11/topics/http/decorators/
https://docs.djangoproject.com/en/1.11/ref/class-based-views/
https://docs.djangoproject.com/en/1.11/ref/request-response/
"""
from django.views import generic
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models

# Create your views here.
#Function Based Views
def index(request):
    blog_list = get_list_or_404(models.Blog)
    context = {'blog_list': blog_list}
    return render(request=request, template_name='index.html', context=context)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk =blog_id)
    context = {'blog': blog}
    return render(request, 'detail.html', context)

@login_required(login_url='blog:index')
def create_blog(request):
    if request.method == 'POST':
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    elif request.method == 'GET':
        form = forms.BlogForm()
        return render(request, 'create_blog.html', {'form':form})

#Class Based Views
class IndexView(generic.ListView):
    model = models.Blog
    template_name = 'index.html' #default is 'blog_list.html'
    cotext_object_name = 'blog_list' #the default context name is 'object_list'

class BlogView(generic.DetailView):
    model = models.Blog
    template_name= 'detail.html'
    context_object_name = 'blog'

class CreateBlogView(generic.FormView):
    form_class = forms.BlogForm
    template_name = 'create_blog.html'
    success_url = '/blog/'
    def form_valid(self, form): #The default implementation for form_valid() simply redirects to the success_url.
        form.save()
        return super(CreateBlogView, self).form_valid(form)
