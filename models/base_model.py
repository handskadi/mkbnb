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
        """ Init baseModel Class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ string representation of an instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ updating public instance of updated at """
        self.update_at = datetime.now()

    def to_dict(self):
        """ prepares a dic represenation of the instance """
        mydict = self.__dict__.copy()
        mydict['__class__'] = type(self).__name__
        mydict['created_at'] = mydict['created_at'].isoformat()
        mydict['updated_at'] = mydict['updated_at'].isoformat()

        return mydict


