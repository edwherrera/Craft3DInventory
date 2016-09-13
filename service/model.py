from decimal import Decimal

TAX_PERCENTAGE = Decimal('0.15')
LMP_TO_DOLLAR_CONVERSION_RATE = Decimal('23.1')


class Printer:
    def __init__(self, data_model):
        self.model = data_model.model

    def __str__(self):
        return self.__dict__.__str__()


class Material:
    def __init__(self, data_model):
        self.name = data_model.name


class Order:
    def __init__(self, data_model):
        self.order_date = data_model.order_date
        self.printer = Printer(data_model.printer)
        self.material = Material(data_model.material)
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
        self.tax = self.total_quote * TAX_PERCENTAGE
        self.final_quote = self.total_quote + self.tax
        self.income = self.total_quote - self.material_quote - self.energy_quote - (self.printing_time / 2)
        self.lempiras = self.total_quote * LMP_TO_DOLLAR_CONVERSION_RATE

    def __str__(self):
        return self.__dict__.__str__()
