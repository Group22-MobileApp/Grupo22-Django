from item.models import Item

class ItemRepository:
    def get_item(self, item_id):
        return Item.objects.get(id=item_id)
    
    def create_item(self, item):
        return Item.objects.create(**item)
    
    def update_item(self, item_id, item):
        return Item.objects.filter(id=item_id).update(**item)
    
    def delete_item(self, item_id):
        return Item.objects.filter(id=item_id).delete()
    
    def get_all_items(self):
        return Item.objects.all()
    
    def get_item_by_name(self, name):
        return Item.objects.get(name=name)
    
    def get_item_by_description(self, description):
        return Item.objects.get(description=description)
    
    def get_item_by_price(self, price):
        return Item.objects.get(price=price)