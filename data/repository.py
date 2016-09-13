from data import model


class _BaseRepository:
    """Base class for all repositories"""
    def __init__(self, object_model: model):
        """Initializes based on a specified data model
        
        object_model: Data model the repository will use to handle queries

        """
        self.object_model = object_model

    def create(self, **values):
        """Creates a new object of the related Data Model with the specified values
        
        values: fields and values with which the new object will be created

        """
        self.object_model.create(**values)

    def get_all(self):
        """Returns a query with all the objects of the represented table"""
        return self.object_model.select()

    def get(self, **query):
        """Returns a query search for the first object that matches the specifies query fields and values

        query: fields and values on which the search will be performed

        """
        return self.object_model.get(**query)


class Printer(_BaseRepository):
    def __init__(self):
        super().__init__(model.Printer)


class Material(_BaseRepository):
    def __init__(self):
        super().__init__(model.Material)


class Order(_BaseRepository):
    def __init__(self):
        super().__init__(model.Order)
