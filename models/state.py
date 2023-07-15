from models.base_model import BaseModel

"""Define State class"""


class State(BaseModel):
    """Initialize Class attributes"""

    name = ""

    def __int__(self, *args, **kwargs):
        """Passing State arguments to BaseModel class"""
        super().__init__(*args, **kwargs)
