from data import repository
from service import model


class _BaseService:
    def __init__(self, service_repository, model):
        self.repository = service_repository
        self.model = model

    def create(self, **params):
        self.repository.create(**params)

    def get_all(self):
        return [self.model(data_model) for data_model in self.repository.get_all()]

    def get(self, **query):
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
