from app.models.post import Post

from app.schemas.post import PostCreate, PostUpdate
from app.crud.base import CRUDBase


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    pass


post = CRUDPost(Post)
