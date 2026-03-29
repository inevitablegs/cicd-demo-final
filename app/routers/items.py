from fastapi import APIRouter, HTTPException, Depends
from app.models import Item
from app.crud import get_item, create_item
from app.dependencies import get_settings

router = APIRouter()

@router.get("/{item_id}")
def read_item(item_id: int, settings = Depends(get_settings)):
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/")
def add_item(item: Item):
    return create_item(item)