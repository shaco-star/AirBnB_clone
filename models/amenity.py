from models.base_model import BaseModel

"""Define Amenity class"""


class Amenity(BaseModel):
    """Initialize Amenity class attributes"""
    name = " "

    def __int__(self, *args, **kwargs):
        """Passing Amenity arguments to BaseModel class"""
        super().__init__(*args, **kwargs)
