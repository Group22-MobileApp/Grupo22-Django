# Paths for CRUD operations on user model
from django.urls import path
from . import views

urlpatterns = [
    path('get_user/<int:user_id>', views.get_user),
    path('create_user', views.create_user),
    path('update_user/<int:user_id>', views.update_user),
    path('delete_user/<int:user_id>', views.delete_user),
    path('get_all_users', views.get_all_users),
    path('get_user_by_email/<str:email>', views.get_user_by_email),
    path('get_user_by_username/<str:username>', views.get_user_by_username),
    path('get_user_by_credentials/<str:email>/<str:password>', views.get_user_by_credentials),
]