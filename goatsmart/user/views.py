from django.http import JsonResponse
from .services import UserService
from .repository import UserRepository

user_service = UserService(UserRepository())

def get_user(request, user_id):
    user = user_service.get_user(user_id)    
    return JsonResponse(user)

def create_user(request):
    user = request.POST
    user_id = user_service.create_user(user)
    return JsonResponse(user_id)

def update_user(request, user_id):
    user = request.POST
    user_id = user_service.update_user(user_id, user)
    return JsonResponse(user_id)

def delete_user(request, user_id):
    user_id = user_service.delete_user(user_id)
    return JsonResponse(user_id)

def get_all_users(request):
    users = user_service.get_all_users()
    return JsonResponse(users)

def get_user_by_email(request, email):
    user = user_service.get_user_by_email(email)
    return JsonResponse(user)

def get_user_by_username(request, username):
    user = user_service.get_user_by_username(username)
    return JsonResponse(user)

def get_user_by_credentials(request, email, password):
    user = user_service.get_user_by_credentials(email, password)
    return JsonResponse(user)




