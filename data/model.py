from peewee import *

db = SqliteDatabase('resources/craft3d_orders.db')


class _BaseModel(Model):
    class Meta:
        database = db


class Printer(_BaseModel):
    model = CharField(max_length=20, unique=True)


class Material(_BaseModel):
    name = CharField(max_length=20, unique=True)


class Order(_BaseModel):
    order_date = DateField()
    client_name = CharField(max_length=50)
    completed_date = DateField()
    file_name = CharField(max_length=20)
    printer = ForeignKeyField(Printer, related_name='orders')
    material = ForeignKeyField(Material, related_name='orders')
    grams = IntegerField(default=None)
    material_quote = DecimalField(decimal_places=2)
    printing_time = FloatField()
    time_quote = DecimalField(decimal_places=2)
    energy_quote = DecimalField(decimal_places=2)
    paint_quote = DecimalField(decimal_places=2)


db.connect()
db.create_tables([Printer, Material, Order, ], safe=True)