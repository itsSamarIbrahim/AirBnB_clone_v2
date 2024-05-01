#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            #from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    if isinstance(value, str):
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__' and hasattr(self.__class__, key):
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        #added (moved from init)
        storage.new(self)
        storage.save()

#    def to_dict(self):
#        """Convert instance into dict format"""
#        dictionary = {}
#        dictionary.update(self.__dict__)
#        dictionary.update({'__class__':
#                          (str(type(self)).split('.')[-1]).split('\'')[0]})
#        for key, value in self.__dict__.items():
#            if key != '_sa_instance_state':
#                dictionary[key] = value
#        dictionary['__class__'] = type(self).__name__
#        dictionary['created_at'] = self.created_at.isoformat()
#        dictionary['updated_at'] = self.updated_at.isoformat()
#        dictionary.pop('_sa_instance_state')
#        return dictionary
    
    def to_dict(self):
        """Converts the object into a dictionary representation"""
        obj_dict = self.__dict__.copy()

        # Remove non-serializable attributes
        non_serializable_attrs = ['_sa_instance_state']  # Add any other non-serializable attributes here
        for attr in non_serializable_attrs:
            obj_dict.pop(attr, None)

        # Convert datetime objects to string representations
        for key, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()

        # Add the class name and id to the dictionary
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['id'] = self.id

        return obj_dict
    
    def delete(self):
        """
        
        """
        from models import storage
        storage.delete(self)
