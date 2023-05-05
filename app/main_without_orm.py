# from fastapi import FastAPI,Response,status,HTTPException
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

# app=FastAPI()

# class Post(BaseModel):
#     title:str
#     content:str
#     published:bool=False

# while True:
#     try:
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='pk123456',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("connected")
#         break
#     except Exception as error:
#         print("Connecting todatabase failed")
#         print(f"error: {error}")
#         time.sleep(2)



# my_posts=[{"title":"sfi post 1","content":"content of post 1","id":1},
#           {"title":'title2',"content":"jo tu mera humdard","id":2}]

# @app.get("/")
# def root():
#     return {"'message":"hello pk...lets do this"}

# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts=cursor.fetchall()
    
#     return {"data":posts}

# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_posts(post:Post):
#     cursor.execute(""" INSERT INTO posts (title,content) VALUES (%s,%s) RETURNING *""",(post.title,post.content))
#     new_post=cursor.fetchone()
#     conn.commit()
    
#     return {"post":new_post}

# def find_post(id):
#     for p in my_posts:
#         if p["id"]==id:
#             return p
    
# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id']==id:
#             return i


# @app.get("/posts/{id}")
# def get_post(id:int):
#     cursor.execute("""SELECT * FROM posts where id=%s""",str(id))
#     post=cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"not here {id}")
#     return {"post detail":post}

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_posts(id:int):
#     cursor.execute("""DELETE FROM posts WHERE id=%s returning *""",str(id))
#     deleted_post=cursor.fetchone()
#     conn.commit()
#     if deleted_post==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not thereb ")
    
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_posts(id:int,post:Post):

#     cursor.execute("""UPDATE posts SET title=%s,content=%s WHERE id=%s returning *""",(post.title,post.content,str(id)))

#     updated_post=cursor.fetchone()
#     conn.commit()

    
#     if updated_post is None:

#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not thereb ")
    
#     return {"data":updated_post}