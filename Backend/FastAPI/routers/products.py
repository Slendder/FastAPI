from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"Message": "Not Found"}})

products_list = ["Product 1", "Product 2", "Product 3", "Product 4"]


@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]
