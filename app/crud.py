from app.models import Item

_items_db = {}

def get_item(item_id: int) -> Item | None:
    return _items_db.get(item_id)

def create_item(item: Item) -> Item:
    _items_db[item.id] = item
    return item