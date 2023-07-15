from models.base_model import BaseModel

"""Define User class"""


class User(BaseModel):
    """Initialization of a User class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __int__(self, *args, **kwargs):
        """Passing user arguments to BaseModel class"""
        super().__init__(*args, **kwargs)