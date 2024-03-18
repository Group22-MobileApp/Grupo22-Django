from django.http import JsonResponse
from .services import UserService
from .repository import UserRepository
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json

user_service = UserService(UserRepository)

def get_user(request, user_id):
    user = user_service.get_user(user_id)    
    return JsonResponse(user)

@csrf_exempt
def create_user(request):
    data = json.loads(request.body)
    user_id = user_service.create_user(data)
    return JsonResponse(user_id)

@csrf_exempt
def update_user(request, user_id):
    data = json.loads(request.body)
    user_id = user_service.update_user(user_id, data)
    return JsonResponse(user_id)

def delete_user(request, user_id):
    user_id = user_service.delete_user(user_id)
    return JsonResponse(user_id)

def get_all_users(request):
    users = user_service.get_all_users()
    return JsonResponse(users, safe=False)

def get_user_by_email(request, email):
    user = user_service.get_user_by_email(email)
    return JsonResponse(user)

def get_user_by_username(request, username):
    user = user_service.get_user_by_username(username)
    return JsonResponse(user)

def get_user_by_credentials(request, email, password):
    user = user_service.get_user_by_credentials(email, password)
    return JsonResponse(user)

