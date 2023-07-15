from models.base_model import BaseModel


class User(BaseModel):
    """Initialization of a User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
