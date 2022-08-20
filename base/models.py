from email.policy import default
from django.db import models

# Create your models here.





class Obrazok(models.Model):
    title = models.CharField(max_length=200, blank=False)
    url = models.URLField(max_length=400)

    def __str__(self) -> str:
        return self.title

class Clanok(models.Model):
    title = models.CharField(max_length=200, blank=True)
    images = models.ManyToManyField(Obrazok, blank=True)

    # JSON quill
    body = models.JSONField(blank=True,null=True)
    #author = 
    post_date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True)
    

    def __str__(self) -> str:
        return "ID: %s | Title: %s" % (self.id,self.title) 


class Galeria(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    images = models.ManyToManyField(Obrazok, blank=True)
    post_date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True)

class PostComment(models.Model):
    author_name = models.CharField(max_length=100, null=True, blank=False)
    # zatial zbytocne body kedze serialize je na frontende
    body = models.TextField(null=True, blank=False)
    clanok = models.ForeignKey(Clanok,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self) -> str:
        return ("%s | %s" % (self.author_name,self.body))

class TopPosts(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    clanok =  models.OneToOneField(Clanok, on_delete=models.RESTRICT,null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Oznamy(models.Model):
    clanok =  models.OneToOneField(Clanok, on_delete=models.RESTRICT,null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id)