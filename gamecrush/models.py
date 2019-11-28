from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    ''' 
    name = models.CharField(max_length = 50)
    describe = models.CharField(max_length = 300)
    birthdate = models.DateField(blank=True, null=True)
    password = models.CharField(max_length = 30)
    email = models.EmailField(blank = False)
    def __str__(self):
        return self.name