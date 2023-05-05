from fastapi import FastAPI, Response, status, HTTPException, Depends,APIRouter
from .. import models,schema
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from .. import oauth2
from typing import Optional
router=APIRouter(prefix="/posts",tags=['posts'])
from sqlalchemy import func


@router.get("/",response_model=List[schema.PostOut])
def get_posts(db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""):
    # cursor.execute("""SELECT * FROM posts""")
    # posts=cursor.fetchall()
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # print(posts)
    return results


# @router.get("/")
# def test_posts(db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user):
#     posts = db.query(models.Post).all()
#     return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_posts(post: schema.PostCreate, db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute(""" INSERT INTO posts (title,content) VALUES (%s,%s) RETURNING *""",(post.title,post.content))
    # new_post=cursor.fetchone()
    # conn.commit()

    new_post = models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schema.PostOut)
def get_post(id: int, db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post=db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    # cursor.execute("""SELECT * FROM posts where id=%s""",str(id))
    # post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"not here {id}")
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int, db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id=%s returning *""",str(id))
    # deleted_post=cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"not thereb ")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schema.Post)
def update_posts(id: int, updated_post: schema.PostUpdate, db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    # cursor.execute("""UPDATE posts SET title=%s,content=%s WHERE id=%s returning *""",(post.title,post.content,str(id)))

    # updated_post=cursor.fetchone()
    # conn.commit()

    if post is None:  

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"not thereb ")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED)
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
  