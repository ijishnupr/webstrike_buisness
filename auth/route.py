
from fastapi import Depends
from fastapi.routing import APIRoute

from auth.model import LoginRequest
from auth.service import user_login
from db import get_connection

# only use this auth for admin 
route = APIRoute()

@route.get("/login")
async def login_route(request:LoginRequest,db=Depends(get_connection)):
    return await user_login(request,db)

