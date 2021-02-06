# importing models and libraries 
from django.shortcuts import render 
from .models import posts, Blog, Comment
from .forms import BlogForm, CommentForm, PostForm
from django.views import generic 
from django.views.decorators.http import require_GET 
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
from django.http import  HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin
 
# class based views for posts 
class postslist(generic.ListView): 
    model = posts
    template_name = 'home.html'
    paginate_by = 4
    def get_queryset(self):
        self.blog = get_object_or_404(Blog, slug=self.kwargs['blog'])
        return posts.objects.filter(status=1).filter(blog=self.blog).order_by('-created_on')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.blog = get_object_or_404(Blog, slug=self.kwargs['blog'])
        context['Blog'] = self.blog
        return context
 
class blogDeleteView(generic.DeleteView): 
    model = Blog 
    template_name = "delete.html"
    success_url ="/"
	
class postseditlist(generic.ListView): 
    model = posts
    template_name = 'posts_edit.html'
    paginate_by = 4
    def get_queryset(self):
        self.blog = get_object_or_404(Blog, slug=self.kwargs['blog'])
        return posts.objects.filter(blog=self.blog).order_by('-created_on')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.blog = get_object_or_404(Blog, slug=self.kwargs['blog'])
        context['Blog'] = self.blog
        return context
		
class postDeleteView(UserPassesTestMixin,generic.DeleteView): 
    model = posts 
    template_name = "delete.html"
    success_url ="/"		
    def test_func(self):
        return self.request.user.is_superuser

class deletecommentView(UserPassesTestMixin, generic.DeleteView): 
    model = Comment
    template_name = "delete.html"
    success_url ="/"	
    def test_func(self):
        return self.request.user.is_superuser
	
class postEditView(UserPassesTestMixin, generic.UpdateView): 
    model = posts 
    template_name = "post_edit.html"
    fields = ['title', 'slug','content','status']
    success_url ="/"	
    def test_func(self):
        return self.request.user.is_superuser
	
class blogEditView(UserPassesTestMixin, generic.UpdateView): 
    model = Blog 
    template_name = "post_edit.html"
    fields = ['title', 'slug','look']
    success_url ="/"	
    def test_func(self):
        return self.request.user.is_superuser	
	
class bloglist( generic.ListView): 
    model = Blog
    template_name = 'blogs.html'
    paginate_by = 4
    queryset= Blog.objects.order_by('-created_on') 	

	
class editbloglist(UserPassesTestMixin, generic.ListView): 
    model = Blog
    template_name = 'blogs_edit.html'
    paginate_by = 4
    def get_queryset(self):
        return Blog.objects.order_by('-created_on')  	
    def test_func(self):
        return self.request.user.is_superuser
		
class postdetail( generic.DetailView): 
    model = posts 
    template_name = "post.html"
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        self.post = get_object_or_404(posts, slug=self.kwargs['slug'])
        context['comments'] = Comment.objects.filter(post=self.post).order_by('-created_on') 
        context['Blog'] = get_object_or_404(Blog, slug=self.post.blog)
        return context
		
    def post(self, request,**kwargs):
        self.post = get_object_or_404(posts, slug=self.kwargs['slug'])
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post=self.post 
            obj.author=request.user
            obj.author_id=request.user.id
            obj.save()
        return HttpResponseRedirect(request.path_info)

		
def create_Post(request, blog):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if request.user.is_superuser:
            form = PostForm(request.POST)
    
        # check whether it's valid:
            if form.is_valid():    
                obj = form.save(commit=False)
                obj.blog=get_object_or_404(Blog, slug=blog)
                obj.author=request.user
                obj.author_id=request.user.id
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
                obj.save()
                return HttpResponseRedirect('/'+blog)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'edit_post.html', {'form': form})

def upvote(request, blog, slug):
    obj = posts.objects.get(slug = slug)
    obj.vote+=1
    obj.save()
    return HttpResponseRedirect('/'+blog+'/post/'+slug)

	
def create_blog(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BlogForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author=request.user
            obj.author_id=request.user.id
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            obj.save()
            return HttpResponseRedirect('admin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BlogForm()
        form.look="""#container img { 
border-radius: 29px; 
width: 100%; 
height: 360px; 
opacity: 0.7; 
align-content: center; 
} 
#container img { 
opacity: 1.0; } 
a {text-align: center; text-decoration: none;}"""
    return render(request, 'blog.html', {'form': form})