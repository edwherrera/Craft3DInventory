import os

from peewee import *

db = SqliteDatabase('resources/craft3d_orders.db')


class _BaseModel(Model):
    """Base class for all the Data Models"""

    class Meta:
        database = db


class Printer(_BaseModel):
    """Data model for printer info"""

    model = CharField(max_length=20, unique=True)


class Material(_BaseModel):
    """Data model for material info"""

    name = CharField(max_length=20, unique=True)


class Order(_BaseModel):
    """Data model for Order info"""
    
    order_date = DateField()
    client_name = CharField(max_length=50)
    completed_date = DateField()
    file_name = CharField(max_length=20)
    printer = ForeignKeyField(Printer, related_name='orders')
    material = ForeignKeyField(Material, related_name='orders')
    grams = IntegerField()
    material_quote = DecimalField(decimal_places=2)
    printing_time = DecimalField(decimal_places=2)
    time_quote = DecimalField(decimal_places=2)
    energy_quote = DecimalField(decimal_places=2)
    paint_quote = DecimalField(decimal_places=2)


if not os.path.exists("resources"):
    os.makedirs("resources")

db.connect()
db.create_tables([Printer, Material, Order, ], safe=True)
