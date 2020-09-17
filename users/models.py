from django.db import models  
class User(models.Model):  
    username = models.CharField(max_length=100)  
    email = models.EmailField()  
    password = models.CharField(max_length=20)  
    class Meta:  
        db_table = "users"  