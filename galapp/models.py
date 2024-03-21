from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=False)
    def str_self():
        return self.name

class Photo(models.Model):
    cataeory=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    def str_self():
        return self.image
