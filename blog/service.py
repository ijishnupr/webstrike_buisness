
from datetime import datetime


async def get_blogs(db,category:str|None = None,date:datetime|None = None):
    conn,cur = db
    get_blogs_query = """
    SELECT
        id,
        title,
        content,
        category
    FROM
        blog_post
    WHERE 1=1
    """
    params = {}
    if category:
        get_blogs_query += " AND category = %(category)s"
        params["category"] = category
    if date:
        
        get_blogs_query += " AND DATE(created_at) = %(date)s"
        params["date"] = date.date()
    await cur.execute(get_blogs_query, params)
    blogs = await cur.fetchall()
    return {"blogs": blogs}