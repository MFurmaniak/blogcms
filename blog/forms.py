from django.forms import ModelForm
from .models import posts, Blog, Comment

class BlogForm(ModelForm):
    class Meta:
	    model=Blog
	    fields = ['title', 'slug','look' ]
		
class PostForm(ModelForm):
    class Meta:
	    model=posts
	    fields = ['title', 'slug','content','status']

class CommentForm(ModelForm):
    class Meta:
	    model=Comment
	    fields = ['content']

