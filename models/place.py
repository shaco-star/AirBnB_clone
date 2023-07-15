from models.base_model import BaseModel

"""Define Place class"""


class Place(BaseModel):
    """Initialize Class attributes"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __int__(self, *args, **kwargs):
        """Passing Place arguments to BaseModel class"""
        super().__init__(*args, **kwargs)
