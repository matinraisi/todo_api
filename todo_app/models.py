from django.db import models
from django.utils import timezone


class category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class todo_list(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField(blank=True)
    created = models.DateField(default=timezone.now())
    category =  models.ForeignKey(category,default='general' ,on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
        
