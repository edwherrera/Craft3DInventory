from data import repository
from service import model


class _BaseService:
    """Base class for the Services"""

    def __init__(self, service_repository, service_model):
        """
        :param service_repository: instance of the repository from which the service will get results
        :param service_model: Service Class type used to initialize the model return to the caller
        """
        self.repository = service_repository
        self.model = service_model

    def create(self, **params):
        """Invokes the create method on the stored repository with the specified values and returns the newly created object
        or None if the object creation was not valid

        :param params: fields with their respective values with which the new object will be built
        """
        return self.model(self.repository.create(**params))

    def get_all(self):
        """Invokes the get_all method for the stored repository"""
        return [self.model(data_model) for data_model in self.repository.get_all()]

    def get(self, **query):
        """Invokes the get method in the stored repository. raises an ObjectNotFoundException if no item was found 
        with the specified query

        :param query: fields and values used in the search
        """
        return self.model(self.repository.get(**query))


class Printer(_BaseService):
    def __init__(self):
        super().__init__(repository.Printer(), model.Printer)


class Material(_BaseService):
    def __init__(self):
        super().__init__(repository.Material(), model.Material)


class Order(_BaseService):
    def __init__(self):
        super().__init__(repository.Order(), model.Order)
