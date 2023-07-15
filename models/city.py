from models.base_model import BaseModel

"""Define City class"""


class City(BaseModel):
    """Initialize Class attributes"""
    state_id = ""
    name = " "

    def __int__(self, *args, **kwargs):
        """Passing City arguments to BaseModel class"""
        super().__init__(*args, **kwargs)