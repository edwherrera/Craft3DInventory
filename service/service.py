import data.model
import data.repository as repository
from decimal import Decimal


class Model:
    class Printer:
        def __init__(self, data_model):
            self.model = data_model.model

        def __str__(self):
            return "model: {}".format(self.model)


    class Material:
        def __init__(self, data_model):
            self.name = data_model.name


    class Order:
        def __init__(self, data_model):
            self.order_date = data_model.order_date 
            self.printer = Model.Printer(data_model.printer)
            self.material = Model.Material(data_model.material)
            self.client_name = data_model.client_name
            self.completed_date = data_model.completed_date
            self.file_name = data_model.file_name
            self.grams = data_model.grams
            self.material_quote = data_model.material_quote
            self.printing_time = data_model.printing_time
            self.time_quote = data_model.time_quote
            self.energy_quote = data_model.energy_quote
            self.paint_quote = data_model.paint_quote
            self.total_quote = self.paint_quote + self.energy_quote + self.time_quote + self.material_quote
            self.tax = self.total_quote * Decimal('0.15')
            self.final_quote = self.total_quote + self.tax
            self.income = self.total_quote - self.material_quote - self.energy_quote - Decimal(self.printing_time * 0.5)
            self.lmps = self.total_quote * Decimal('23.1')

        def __str__(self):
            return self.__dict__.__str__()


class Service:
    class _BaseService:
        def __init__(self, repository, model):
            self.repository = repository
            self.model = model

        def create(self, **params):
            self.repository.create(**params)

        def get_all(self):
            return [self.model(data_model) for data_model in self.repository.get_all()]

        def get(self, **query):
            return self.model(self.repository.get(**query))


    class Printer(_BaseService):
        def __init__(self):
            super().__init__(repository.Printer(), Model.Printer)


    class Material(_BaseService):
        def __init__(self):
            super().__init__(repository.Material(), Model.Material)


    class Order(_BaseService):
        def __init__(self):
            super().__init__(repository.Order(), Model.Order)
            