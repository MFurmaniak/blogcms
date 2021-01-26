from django.db import models

from django.contrib.auth.models import User 
  

STATUS = ( 
    (0,"Draft"), 
    (1,"Publish"), 
    (2, "Delete") 
) 
 
class Blog(models.Model): 
    
    title = models.CharField(max_length=200, unique=True) 
   
    slug = models.SlugField(max_length=200, unique=True) 

    author = models.ForeignKey(User, on_delete= models.CASCADE) 
 
    updated_on = models.DateTimeField(auto_now= True) 
    created_on = models.DateTimeField(auto_now_add=True) 

  
    # meta for the class 
    class Meta: 
        ordering = ['-created_on'] 
    # used while managing models from terminal 
    def __str__(self): 
        return self.title 
	 

class posts(models.Model): 
    
    title = models.CharField(max_length=200, unique=True) 
   
    slug = models.SlugField(max_length=200, unique=True) 

    author = models.ForeignKey(User, on_delete= models.CASCADE) 
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE) 

    updated_on = models.DateTimeField(auto_now= True) 
    created_on = models.DateTimeField(auto_now_add=True) 

    content = models.TextField() 

    metades = models.CharField(max_length=300, default="new post") 

    status = models.IntegerField(choices=STATUS, default=0) 
  
    vote = models.IntegerField( default=0) 
    # meta for the class 
    class Meta: 
        ordering = ['-created_on'] 
    # used while managing models from terminal 
    def __str__(self): 
        return self.title 
		

	
class Comment(models.Model): 
    
    
    author = models.ForeignKey(User, on_delete= models.CASCADE) 
    post = models.ForeignKey(posts, on_delete= models.CASCADE) 

    updated_on = models.DateTimeField(auto_now= True) 
    created_on = models.DateTimeField(auto_now_add=True) 

    content = models.TextField() 


    status = models.IntegerField(choices=STATUS, default=0) 
  
    # meta for the class 
    class Meta: 
        ordering = ['-created_on'] 
    # used while managing models from terminal 
    def __str__(self): 
        return self.title 
		