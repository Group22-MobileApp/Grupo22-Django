from item.models import Item
from item.repository import ItemRepository

class ItemService:
    def __init__(self):
        self.item_repository = ItemRepository()

    def get_item(self, item_id):
        return self.item_repository.get_item(item_id)
    
    def create_item(self, data):    
        item_created = self.item_repository.create_item(item=data)
        return item_created.item_id
    
    def update_item(self, item_id, item):
        return self.item_repository.update_item(item_id, item)
    
    def delete_item(self, item_id):
        return self.item_repository.delete_item(item_id)
    
    def get_all_items(self):
        items_query = self.item_repository.get_all_items()        
        items_query_red = items_query.values('name', 'description', 'price')
        # Transform the query into a list
        return list(items_query_red)        
        
    def get_item_by_name(self, name):
        return self.item_repository.get_item_by_name(name)
    
    def get_item_by_description(self, description):
        return self.item_repository.get_item_by_description(description)
    
    def get_item_by_price(self, price):
        return self.item_repository.get_item_by_price(price)