from data import repository
from service import model


class _BaseService:
    def __init__(self, service_repository, service_model):
        self.repository = service_repository
        self.model = service_model

    def create(self, **params):
        self.repository.create(**params)

    def get_all(self):
        return [self.model(data_model) for data_model in self.repository.get_all()]

    def get(self, **query):
        try:
            result = self.repository.get(**query)
        except self.repository.object_model.DoesNotExist:
            result = None
        else:
            result = self.model()

        return result


class Printer(_BaseService):
    def __init__(self):
        super().__init__(repository.Printer(), model.Printer)


class Material(_BaseService):
    def __init__(self):
        super().__init__(repository.Material(), model.Material)


class Order(_BaseService):
    def __init__(self):
        super().__init__(repository.Order(), model.Order)
