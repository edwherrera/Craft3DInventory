import data.model as model


class _BaseRepository:
    def __init__(self, object_model):
        self.object_model = object_model

    def create(self, **values):
        self.object_model.create(**values)

    def get_all(self):
        return self.object_model.select()

    def get(self, **query):
        return self.get_all().get(**query)


class Printer(_BaseRepository):
    def __init__(self):
        super().__init__(model.Printer)


class Material(_BaseRepository):
    def __init__(self):
        super().__init__(model.Material)


class Order(_BaseRepository):
    def __init__(self):
        super().__init__(model.Order)

    def get_all(self):
        return self.object_model.select().join(model.Printer).switch(self.object_model).join(model.Material)