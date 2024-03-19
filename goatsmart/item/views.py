from django.http import JsonResponse
from .services import ItemService
from django.views.decorators.csrf import csrf_exempt
import json

item_service = ItemService()

def get_item(request, item_id):
    item = item_service.get_item(item_id)
    return JsonResponse(item)

@csrf_exempt
def create_item(request):
    data = json.loads(request.body)
    item_id = item_service.create_item(data=data)
    return JsonResponse(item_id, safe=False)

@csrf_exempt
def update_item(request, item_id):
    data = json.loads(request.body)
    item_id = item_service.update_item(item_id, data)
    return JsonResponse(item_id)

def delete_item(request, item_id):
    item_id = item_service.delete_item(item_id)
    return JsonResponse(item_id)

def get_all_items(request):
    items = item_service.get_all_items()
    return JsonResponse(items, safe=False)

def get_item_by_name(request, name):
    item = item_service.get_item_by_name(name)
    return JsonResponse(item)

def get_item_by_description(request, description):
    item = item_service.get_item_by_description(description)
    return JsonResponse(item)

def get_item_by_price(request, price):
    item = item_service.get_item_by_price(price)
    return JsonResponse(item)



# Create your views here.
