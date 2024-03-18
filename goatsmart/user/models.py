from django.db import models

# Create your models here. The model represents the structure of the database table. 

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    university_major = models.CharField(max_length=50)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['username']

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')
#     bio = models.TextField(max_length=500, blank=True)
#     major = models.CharField(max_length=50, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username

#     class Meta:
#         db_table = 'profile'
#         verbose_name = 'profile'
#         verbose_name_plural = 'profiles'
#         ordering = ['user']

        