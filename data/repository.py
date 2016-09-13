from data import model
from exception import exception

from peewee import IntegrityError


class _BaseRepository:
    """Base class for all repositories"""

    def __init__(self, object_model: model):
        """Initializes based on a specified data model
        
        :param object_model: Data model the repository will use to handle queries
        """
        self.object_model = object_model

    def create(self, **values):
        """Creates and returns a new object of the related Data Model with the specified values
        
        :param values: fields and values with which the new object will be created
        """
        try:
            return self.object_model.create(**values)
        except IntegrityError:
            raise exception.ObjectAlreadyExistsException()

    def get_all(self):
        """Returns a query with all the objects of the represented table"""
        return self.object_model.select()

    def get(self, **query):
        """Returns a query search for the first object that matches the specifies query fields and values

        :param query: fields and values on which the search will be performed
        """
        try:
            return self.object_model.get(**query)
        except self.object_model.DoesNotExist:
            raise exception.ObjectNotFoundException()


class Printer(_BaseRepository):
    def __init__(self):
        super().__init__(model.Printer)


class Material(_BaseRepository):
    def __init__(self):
        super().__init__(model.Material)


class Order(_BaseRepository):
    def __init__(self):
        super().__init__(model.Order)
