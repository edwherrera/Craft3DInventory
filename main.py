from service import service
from datetime import date

order_service = service.Service.Order()

# service.Service.Printer().create(model='printer')
# service.Service.Material().create(name='material')


# order_service.create(order_date=date.today(), client_name='Edwin', completed_date=date.today(), file_name='somefile', printer=1, 
#     material=1, grams=0.0, material_quote=0.0, printing_time=1.5, time_quote=0.0, energy_quote=0.0, paint_quote=0.0)

orders = order_service.get_all()
for order in orders:
    print(order)