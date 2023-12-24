from fastapi import Body, Depends, FastAPI, Query
from pydantic import BaseModel

from config.registry import Registry
from services.get_list_items import GetListItemService
from services.save_new_item import SaveItemService

app = FastAPI()


class RequestPayload(BaseModel):
	value: int


@app.get("/items")
def define_restaurant_open_hours(
		id: int = Query(...),
		service: GetListItemService = Depends(Registry.get_single_item_service)
):
	return service(id)


@app.get("/items/list")
def define_restaurant_open_hours(
		service: GetListItemService = Depends(Registry.get_list_item_service)
):
	return service()


@app.post("/items")
def define_restaurant_open_hours(
		payload: RequestPayload = Body(...),
		service: SaveItemService = Depends(Registry.save_item_service)
):
	return service(payload.value)
