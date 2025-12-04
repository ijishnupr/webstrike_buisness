
from auth.model import LoginRequest
import jwt
from argon2 import PasswordHasher

async def user_login(request:LoginRequest, db):
    conn,cur = db
    get_user_query = """
    SELECT
        user_code,
        password
    FROM
        app_user
    WHERE
        user_code = %(user_code)s
    """
    await cur.execute(get_user_query, {"user_code": request.username})
    user_record = await cur.fetchone()
    if not user_record:
        return {"error": "Invalid usercode"}
    password = user_record['password']
    ph = PasswordHasher()
    ph.verify(password, request.password)
    token = jwt.encode({"user_code": request.username}, "your_secret_key", algorithm="HS256")
    return {"token": token}