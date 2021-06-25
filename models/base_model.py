#!/usr/bin/python3
"""
Base Model for AirBnB
"""
from datetime import datetime
import json
from uuid import uuid4


class BaseModel:
	"""Class that defines all common attr/methods for other classes"""
	def __init__(self, *args, **kwargs):
		"""Initialization of Class"""
		self.id = str(uuid4())
		self.created_at = datetime.today()
		self.updated_at = datetime.today()
	
	def __str__(self):
		"""String representation"""
		return ("[{}] ({}) {}".format(self.__class__.__name__,
									  self.id, self.__dict__))

	def save(self):
		""" updates the public instance attribute with the current datetime """
		today = datetime.today()
		self.updated_at = today
	
	def to_dict(self):
		""" returns a dictionary containing all keys/values of the instance"""
		new = dict(self.__dict__)
		new["created_at"] = self.created_at.isoformat()
		new["updated_at"] = self.updated_at.isoformat()
		new["__class__"] = self.__class__.__name__
		return new