from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("auth.user", verbose_name = "نویسنده", on_delete=models.PROTECT)
    title=models.CharField(max_length=120,verbose_name='عنوان')
    content=RichTextField(verbose_name='متن')
    published_date=models.DateTimeField(verbose_name='تاریخ انتشار',auto_now_add=True)
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'id':self.id})

    def get_update_url(self):
        return reverse('post:update',kwargs={'id':self.id})
    
    def get_delete_url(self):
        return reverse('post:delete',kwargs={'id':self.id})

    class Meta:
        ordering=['-published_date']


class Comment(models.Model):
    post=models.ForeignKey("post.Post",related_name="comments", on_delete=models.CASCADE)
    name=models.CharField(max_length=120, verbose_name="نام")
    content=models.TextField(verbose_name="دیدگاه")
    created_date=models.DateTimeField(auto_now_add=True)