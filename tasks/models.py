from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100) # max length of 100 characters
    description = models.TextField(blank=True) # blank and null are optional
    created  = models.DateTimeField(auto_now_add=True) # auto_now_add is the date and time of creation
    datecompleted = models.DateTimeField(null=True, blank=True) # null and blank are optional
    important = models.BooleanField(default=False) # default is false
    user = models.ForeignKey(User, on_delete= models.CASCADE) # on_delete is what happens when the user is deleted

    def __str__(self):
        return self.title + "- by " + self.user.username