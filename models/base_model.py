#!/usr/bin/python3
"""
    Base Module that will host commin:
    attributes and methods for other classes
"""

import  uuid
from  datetime import datetime
class BaseModel():
    """
        BaseModel Class to host ID, Created at, Updated at attributes

        Args:
            id (str): object id
            created_at (str): created at this date
            updated_at (str): update all date
        """


    def __init__(self):
        self.id = uuid.uuid4() 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict


