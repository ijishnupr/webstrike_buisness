from datetime import datetime
from blog.service import get_blogs
from fastapi import Depends
from shared.db import get_connection
route = APIRoute()

@route.post("/category")
async def create_category_route():
    pass

@router.get("/blog")
async def get_blogs_route(db=Depends(get_connection),category:str|None=None,date:datetime|None=None ):
    return await get_blogs(category,date, db)