from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import User

class Post(models.Model):   
    author              = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title               = models.CharField(max_length=250)
    slug                = models.SlugField(max_length=250)
    content             = models.TextField(blank=True,null=True)
    date_posted         = models.DateTimeField(auto_now_add=True)
    datedate_updated    = models.DateTimeField(auto_now=True, verbose_name='date updated')
    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    
    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 1000 or img.width > 1000:
    #         output_size = (1000, 1000)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
            
    class Meta:
        db_table = 'blogs'
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'   
