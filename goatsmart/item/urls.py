from django.urls import path
from . import views

urlpatterns = [
    path('get_item/<int:item_id>', views.get_item),
    path('create_item', views.create_item),
    path('update_item/<int:item_id>', views.update_item),
    path('delete_item/<int:item_id>', views.delete_item),
    path('get_all_items', views.get_all_items),
    path('get_item_by_name/<str:name>', views.get_item_by_name),
    path('get_item_by_description/<str:description>', views.get_item_by_description),
    path('get_item_by_price/<int:price>', views.get_item_by_price),
]