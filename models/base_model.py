#!/usr/bin/python3
"""
Base Model for AirBnB
"""
import datetime
import json
from uuid import uuid4


class BaseModel:
	"""Class that defines all common attr/methods for other classes"""

	def __init__(self, id=None):
		"""Initialization of Class"""

		self.id = str(uuid4())
		self.created_at = datetime.today()
		self.updated_at = datetime.today()

	def __str__(self):
		""" String Representation """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
