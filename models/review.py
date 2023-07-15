from models.base_model import BaseModel

"""Define Review class"""


class Review(BaseModel):
    """Initialize Class attributes"""
    place_id = ""
    user_id = ""
    text = ""

    def __int__(self, *args, **kwargs):
        """Passing Review arguments to BaseModel class"""
        super().__init__(*args, **kwargs)
